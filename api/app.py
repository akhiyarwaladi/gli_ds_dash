from flask import Flask, jsonify, request
from sqlalchemy import event,create_engine,types

import pandas as pd
import numpy as np
import os
import json
import ast
import time

from joblib import dump, load
from helper import transform_to_rupiah_format,transform_format,transform_to_rupiah,rupiah_format

from dateutil import parser

driver = 'cx_oracle'
server = '10.234.152.61' 
database = 'alfabi' 
username = 'report' 
password = 'justd0it'
engine_stmt = "oracle://%s:%s@%s/%s" % ( username, password, server, database )


app = Flask(__name__)
def get_promo_feature():
	with open('/home/server/gli-data-science/akhiyar/sales_prediction/feature/promo_feature_stag_1.json','r') as f:
	    s = f.read()

	promo_feature = dict(ast.literal_eval(s))


	with open('/home/server/gli-data-science/akhiyar/sales_prediction/feature/promo_feature_offline.json','r') as f:
		s = f.read()

	promo_feature_offline = dict(ast.literal_eval(s))

	with open('/home/server/gli-data-science/akhiyar/sales_prediction/feature/promo_feature_map.json','r') as f:
		s = f.read()

	promo_feature_map = dict(ast.literal_eval(s))
	return promo_feature, promo_feature_offline, promo_feature_map

promo_feature, promo_feature_offline, promo_feature_map = get_promo_feature()




@app.route('/predict', methods=['POST'])
def infer_sales():
    # Catch the image file from a POST request



	promo_start_date = request.args.get('promo_start_date', None)
	promo_end_date = request.args.get('promo_end_date', None)
	input_min_amount = request.args.get('input_min_amount', None)
	input_min_qty = request.args.get('input_min_qty', None)
	input_extra_star = request.args.get('input_extra_star', None)
	input_extra_point = request.args.get('input_extra_point', None)
	input_discount_amount = request.args.get('input_discount_amount', None)
	input_num_target = request.args.get('input_num_target', default=None, type=int)
	pred_promo_type = request.args.get('pred_promo_type', default=None, type=str)
	pred_plu = request.args.get('pred_plu', None)
	pred_app = request.args.get('pred_app', type=str)
	# Return on a JSON format

	print(promo_start_date)
	print(promo_end_date)
	print(input_min_amount)

	print(pred_promo_type)
	print(promo_feature)
	print(promo_feature[pred_promo_type])

	print(pred_app)

	if pred_app == 'alfagift':
		print('in alfagift flow')
		try:
			parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
			modul_path = '{}/model/plu_linear_test/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)


			##### FORM
			pred_df = pd.DataFrame()

			date_object = parser.parse(promo_start_date)
			promo_start_date_str = date_object.strftime('%Y-%m-%d')

			date_object = parser.parse(promo_end_date)
			promo_end_date_str = date_object.strftime('%Y-%m-%d')

			pred_df['tbmproi_start_date'] = [promo_start_date_str]
			pred_df['tbmproi_end_date'] = [promo_end_date_str]

			pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
			pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
			pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
			pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
			                            .astype('timedelta64[D]') + 1).astype(int)


			pred_df['tbmproi_min_purchase_amount'] = [input_min_amount]
			pred_df['tbmproi_min_purchase_qty'] = [input_min_qty]
			pred_df['tbmproi_star'] = [input_extra_star]
			pred_df['tbmproi_extra_point'] = [input_extra_point]
			pred_df['tbmproi_disc_amount'] = [input_discount_amount]
			pred_df['count_branch'] = 32
			pred_df['Non Member'] = 1
			pred_df['SSP Member'] = 1
			pred_df['Regular'] = 1
			pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9

			### #END FORM
			if not os.path.exists(modul_path):
				engine = create_engine(engine_stmt)
				q = '''
				SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
				FROM(
				    SELECT 
				        ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
				    FROM TEMP_SALES_PROMO_ALFAGIFT
				    WHERE PLU = {}
				)


				'''.format(pred_plu)
				con = engine.connect()
				try:
				    res_avg = pd.read_sql_query(q,con)
				except Exception as e:
				    if is_debug:
				        print(e)
				    pass
				con.close()
				engine.dispose()
				print(res_avg)
				print(len(res_avg))

				if res_avg['avg_daily'][0] is None:
					res = {
						'error':'historical PLU data this promo type not exists',
						'sales':0
					}
					return jsonify(res)

				res = {
					'sales':rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
					'sales_increase_by':[]

				}
				return jsonify(res)
			####    
			clf = load(modul_path)
			adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

			df_res = pd.concat([pd.DataFrame(promo_feature[pred_promo_type], columns=['variabel']), 
			           pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)
			li_adder_plus = [promo_feature_map[i] for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
			li_adder_min = [promo_feature_map[i] for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

			####

			engine = create_engine(engine_stmt)
			q = '''
			    SELECT AVG(NUM_MEMBER) AS AVG_NUM_MEMBER
			    FROM TEMP_SALES_PROMO_ALFAGIFT tspa 
			    WHERE tspa.PLU = {}
			    AND tspa.TYPE = {}

			'''.format(pred_plu, pred_promo_type)
			con = engine.connect()
			try:
			    res_avg = pd.read_sql_query(q,con)
			except Exception as e:
			    if is_debug:
			        print(e)
			    pass
			con.close()
			engine.dispose()


			if len(res_avg) > 0:
			    num_target_avg =  int(res_avg['avg_num_member'][0])
			else:
			    num_target_avg =  100

			pred_val = clf.predict(pred_df[promo_feature[pred_promo_type]])[0]
			pred_val = (input_num_target / num_target_avg) * pred_val
			if pred_val < 0:
			    pred_val = 0

			time.sleep(1)
			print(pred_val)

			res = {
				'sales':rupiah_format(pred_val, with_prefix=True),
				'sales_increase_by':li_adder_plus

			}
			return jsonify(res)
		    
		except Exception as e:
			print('='*30)
			print(e)

			# engine = create_engine(engine_stmt)
			# q = '''
			# SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
			# FROM(
			#     SELECT 
			#         ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
			#     FROM TEMP_SALES_PROMO_ALFAGIFT
			#     WHERE PLU = {}
			# )


			# '''.format(pred_plu)
			# con = engine.connect()
			# try:
			#     res_avg = pd.read_sql_query(q,con)
			# except Exception as e:
			#     if is_debug:
			#         print(e)
			#     pass
			# con.close()
			# engine.dispose()

			# res = {
			# 	'sales':rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
			# 	'sales_increase_by':[]

			# }
			# return jsonify(res)
			res = {
				'error':e,
				'sales':0
			}
			return jsonify(res)

	elif pred_app == 'alfamart':
		print('in alfamart flow')
		try:
			parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
			modul_path = '{}/model/plu_linear_offline/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)


			if not os.path.exists(modul_path):
				res = {
					'error':'model not exists',
					'sales':0
				}
				return jsonify(res)

			clf = load(modul_path)


			adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

			df_res = pd.concat([pd.DataFrame(promo_feature_offline[pred_promo_type], columns=['variabel']), 
			           pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)

			li_adder_plus = [i for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
			li_adder_min = [i for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

			pred_df = pd.DataFrame()


			date_object = parser.parse(promo_start_date)
			promo_start_date_str = date_object.strftime('%Y-%m-%d')

			date_object = parser.parse(promo_end_date)
			promo_end_date_str = date_object.strftime('%Y-%m-%d')

			pred_df['tbmproi_start_date'] = [promo_start_date_str]
			pred_df['tbmproi_end_date'] = [promo_end_date_str]

			pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
			pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
			pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
			pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
			                            .astype('timedelta64[D]') + 1).astype(int)



			pred_df['MIN_QTY'] = [input_min_qty]
			if pred_promo_type == '807':
			    pred_df['POT'] = [input_extra_point]
			elif pred_promo_type == '201':
			    pred_df['POT'] = [input_discount_amount]
			pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9



			pred_val = clf.predict(pred_df[promo_feature_offline[pred_promo_type]])[0]
			if pred_val < 0:
			    pred_val = 0

			print(pred_val)
			res = {
				'sales':rupiah_format(pred_val, with_prefix=True),
				'sales_increase_by':li_adder_plus

			}
			return jsonify(res)


		except Exception as e:
			res = {
				'error':e,
				'sales':0
			}
			return jsonify(res)



@app.route('/list_plu', methods=['POST'])
def infer_plu():

	pred_app = request.args.get('pred_app', type=str)

	pred_app = 'alfamart'
	if pred_app == 'alfagift':
		parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_linear_test/'

		tree_split = [li.split('_')[0] for li in os.listdir(parent_path)]

	elif pred_app == 'alfamart':
		parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_linear_offline/'

		tree_split = [li.split('_')[0] for li in os.listdir(parent_path)]


	res = {
		'list_plu':tree_split

	}
	return jsonify(res)




@app.route('/', methods=['GET'])
def index():
	return 'Machine Learning Inference'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8049, debug=True)