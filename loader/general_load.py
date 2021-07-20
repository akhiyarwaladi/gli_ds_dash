import pandas as pd
from helper import transform_to_rupiah_format,transform_format, transform_to_format

def get_member_count():
	am = pd.read_csv('/home/server/gli-data-science/akhiyar/data_req/member_count.csv', sep='\t')
	am['index'] = pd.to_datetime(am['index'], format='%Y%m%d')
	am['count_format'] = am['count'].astype(float).apply(transform_to_format)

	return am

def get_sapa_count():
	am = pd.read_csv('/home/server/gli-data-science/akhiyar/data_req/sapa_count.csv', sep='\t')
	am['index'] = pd.to_datetime(am['index'], format='%Y%m%d')
	am['count_format'] = am['count'].astype(float).apply(transform_to_format)

	return am