import pandas as pd
import json
import ast



def get_promo_feature():
	with open('/home/server/gli-data-science/akhiyar/sales_prediction/feature/promo_feature.json','r') as f:
	    s = f.read()

	promo_feature = dict(ast.literal_eval(s))
	return promo_feature

	

def get_plu_list():

	low_label = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_list.csv'
		, skiprows=[0],  names=['value','label'])
	label = low_label.to_dict(orient='records')

	return label, ''