import pandas as pd
from helper import transform_format
def get_product_competitive():
	pc = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/product_competitive.csv', sep='\t')

	pc['diff_price'] = pc['comp_price'] - pc['our_price']
	# pc['diff_price'] = (pc['diff_price'].astype('float')).apply(transform_format)
	# pc['our_price'] = (pc['our_price'].astype('float')).apply(transform_format)
	# pc['comp_price'] = (pc['comp_price'].astype('float')).apply(transform_format)

	n_lower = pc['price_vs'].value_counts().to_dict()[True]
	n_higher = pc['price_vs'].value_counts().to_dict()[False]

	pc['price_vs'] = pc['price_vs'].map({True:'lower', False:'higher'})
	pc = pc[['plu', 'product_name_comp', 'our_price', 'comp_price', 'diff_price', 'url_comp', 'price_vs']]

	pc = pc.rename(columns={'our_price':'our (Rp.)', 'comp_price':'comp (Rp.)', 'diff_price':'diff (Rp.)'})
	return pc, n_lower, n_higher
