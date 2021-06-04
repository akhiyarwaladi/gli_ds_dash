import pandas as pd


def get_app_update():
	app_update = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/general_moengage/app_update.csv')

	return app_update


def get_device_uninstall():
	device_uninstall = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/general_moengage/device_uninstall.csv')

	return device_uninstall

