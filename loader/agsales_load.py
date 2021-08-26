import pandas as pd
from datetime import datetime, timedelta
import pickle

def get_agsales():
    sales_dict = {}

    ## prophet
    member_pred = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/member_pred.csv')
    sapa_pred = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/sapa_pred.csv')
    df_tto_test = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/sales_general_forecast.csv')
    df = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/model/sales_general_train.csv')

    df_tto_test['TRO_DATE_ORDER'] = pd.to_datetime(df_tto_test['TRO_DATE_ORDER'])
    df['ds'] = pd.to_datetime(df['ds'])

    # read the Prophet model object
    with open('/home/server/gli-data-science/akhiyar/sales_prediction/model/sales_general_model.csv', "rb") as f:
        m = pickle.load(f)
    
    sales_dict['fbprophet'] = [
        member_pred, 
        sapa_pred,
        df_tto_test,
        df,
        m

    ]
    ## n-beats
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales_plot_oshop_test.csv', \
                        sep='\t')

    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['nbeats'] = sales_plot

    return sales_dict

def get_agsales_promo():
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/payday_gantung.csv')
    return sales_plot


def get_agsales_jsm():


    sales_dict = {}

    
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_jsm.csv')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['JSM (jumat-sabtu-minggu)'] = sales_plot


    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_instore.csv')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['INSTORE (harga coret)'] = sales_plot


    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_gantung.csv')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['Gantung (gajian untung)'] = sales_plot


    return sales_dict