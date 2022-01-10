import pandas as pd
import json
import ast



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

	

def get_plu_list():

	low_label = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_list.csv'
		, skiprows=[0],  names=['value','label'])
	label_alfagift = low_label.to_dict(orient='records')

	low_label = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_list_offline.csv'
		, skiprows=[0],  names=['value','label'])
	label_offline = low_label.to_dict(orient='records')


	return label_alfagift, label_offline



sore mba maudi, aku bisa hadir besok (selasa) di jam 15.45