import pandas as pd





def get_plu_list():

	low_label = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_list.csv'
		, header=None,  names=['value','label'])
	label = low_label.to_dict(orient='records')

	return label, ''