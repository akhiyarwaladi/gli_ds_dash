import pandas as pd

def get_product():
	plu_group = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/product_group.csv',\
		sep='\t')

	plu_group['TRO_DATE_ORDER'] = pd.to_datetime(plu_group['TRO_DATE_ORDER'])
	label = [{'label': x, 'value': x} for x in plu_group['TRO_DATE_ORDER']\
	     .dropna().dt.strftime('%Y-%m').unique()]
	return plu_group, label


def get_general_event():
	sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/install_uninstall_update.csv')
	sales_plot['Event Time'] = pd.to_datetime(sales_plot['Event Time'])

	return sales_plot