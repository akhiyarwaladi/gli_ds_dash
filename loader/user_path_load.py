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