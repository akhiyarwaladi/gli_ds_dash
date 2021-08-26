import numpy as np
from datetime import datetime, timedelta

def adjust_feature_target(target_value, target_feat, df_tto_test):
	target = target_value
	feat_adjust = target_feat

	feat_bound = df_tto_test['TRO_DATE_ORDER'].min()
	feat_bound = datetime(feat_bound.year, feat_bound.month, feat_bound.day)

	df_tto_test[feat_adjust] = np.where(df_tto_test['TRO_DATE_ORDER'] > feat_bound, np.nan, df_tto_test[feat_adjust])
	df_tto_test[feat_adjust] = np.where(df_tto_test['TRO_DATE_ORDER'] == df_tto_test['TRO_DATE_ORDER'].max(), 
	                                    target, df_tto_test[feat_adjust])

	## find how many null value that we want to fill
	feat_bound_to_target = (df_tto_test['TRO_DATE_ORDER'].max() - timedelta(days=1) - feat_bound).days 
	## get lower value (last feature data that known actual value)
	feat_bound_val = df_tto_test[df_tto_test['TRO_DATE_ORDER'] == feat_bound][feat_adjust].astype(int).values[0]

	'''
	# sample case
	a = [1, np.nan, np.nan, np.nan, 10]
	np.arange(1, 10, 9/4)
	'''
	df_tto_test.loc[df_tto_test[feat_adjust].isnull(), feat_adjust] = \
	        list(np.arange(feat_bound_val, target, (target-feat_bound_val)/(feat_bound_to_target+1)))[1:]

	return df_tto_test
