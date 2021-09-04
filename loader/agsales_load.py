import pandas as pd
from datetime import datetime, timedelta
import pickle
import json
from prophet.serialize import model_to_json, model_from_json

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

# def get_agsales_promo():
#     sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/payday_gantung.csv')
#     return sales_plot


def get_agsales_promo():


    sales_dict = {}

    
    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_jsm.csv')
    sales_plot = sales_plot.rename(columns={'TRO_DATE_ORDER':'ds','TRO_NET':'y'})
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['JSM (jumat-sabtu-minggu)'] = sales_plot


    promo_str_con = 'instore'
    df = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/train_data/all_{}.csv'.format(promo_str_con))
    df = df.rename(columns={'TRO_DATE_ORDER':'ds','TRO_NET':'y'})
    df['ds'] = pd.to_datetime(df['ds'])


    df_forecast = pd.read_csv('/home/server/gli-data-science/akhiyar/sales_prediction/train_data/all_{}_forecast.csv'.format(promo_str_con))
    df_forecast = df_forecast.rename(columns={'TRO_DATE_ORDER':'ds','TRO_NET':'y'})
    df_forecast['ds'] = pd.to_datetime(df_forecast['ds'])


    with open('/home/server/gli-data-science/akhiyar/sales_prediction/model/sales_{}_model.json'.format(promo_str_con), 'r') as fin:
        m = model_from_json(json.load(fin))  # Load model
    sales_dict['INSTORE (harga coret)'] = [df, df_forecast, m]


    sales_plot = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/all_gantung.csv')
    sales_plot = sales_plot.rename(columns={'TRO_DATE_ORDER':'ds','TRO_NET':'y'})
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    sales_dict['Gantung (gajian untung)'] = sales_plot


    return sales_dict