import pandas as pd
from datetime import datetime, timedelta

def get_agsales():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales_plot_oshop_test.csv', \
                        sep='\t')


    lower_bond = datetime.today() - timedelta(days=90)
    lower_bond = lower_bond.strftime('%Y-%m-%d')

    # sales_plot = sales_plot[sales_plot['index'] > lower_bond]

    sales_plot['index'] = pd.to_datetime(sales_plot['index'])

    return sales_plot

def get_agsales_promo():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/payday_gantung.csv')
    return sales_plot


def get_agsales_jsm():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_jsm.csv')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    return sales_plot