import pandas as pd
from datetime import datetime, timedelta

def get_agsales():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales_plot_oshop.csv', \
                        sep='\t')


    lower_bond = datetime.today() - timedelta(days=90)
    lower_bond = lower_bond.strftime('%Y-%m-%d')

    sales_plot = sales_plot[sales_plot['index'] > lower_bond]

    sales_plot['index'] = pd.to_datetime(sales_plot['index'])

    return sales_plot
