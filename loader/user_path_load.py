import pandas as pd


def get_app_update():
	app_update = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/general_moengage/app_update.csv')

	return app_update


def get_device_uninstall():
	device_uninstall = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/general_moengage/device_uninstall.csv')

	return device_uninstall

def get_notification_received():

	notification_received = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/general_moengage/notification_received.csv')
	
	return notification_received

def get_df_3gram():
	df_3gram = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/df_3gram.csv', sep='\t')
	df_3gram['index'] = df_3gram['index'].astype(str)

	return df_3gram

def get_uninstall_review():
	df_det_ua = pd.read_csv('/home/server/gli-data-science/akhiyar/app_review/out_file/uninstall_review.csv'\
				, sep='\t')
	df_det_ua = df_det_ua.sample(n=len(df_det_ua), random_state=123)
	return df_det_ua, len(df_det_ua)

def get_review_trend():
	review_trend = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/review_trend.csv'\
				, sep='\t')
	review_trend['tbtdr_created_date'] = pd.to_datetime(review_trend['tbtdr_created_date'])
	return review_trend


def get_low_review():

	# low_review = pd.read_csv('/home/server/gli-data-science/akhiyar/app_review/out_file/low_review.csv'\
	# 			, sep='\t')

	# label = [{'label': x, 'value': x} for x in low_review['class'].unique()]

	low_review = pd.read_excel('/home/server/gli-data-science/akhiyar/app_review/out_file/low_review.xlsx'\
	            , sheet_name=0, skiprows=1)
	low_review = low_review[['tbtdr_created_date', 'tbtdr_rating', 'tbtdr_review', 'class']]\
	            .rename(columns={'tbtdr_created_date':'date','tbtdr_rating':'rating','tbtdr_review':'review'})

	low_label = pd.read_excel('/home/server/gli-data-science/akhiyar/app_review/out_file/low_review.xlsx'\
	            , sheet_name=1,  names=['value','label'])
	label = low_label.to_dict(orient='records')

	return low_review, label