import numpy as np 
import pandas as pd

import textwrap
def split_label(list_label):
    list_label = list(list_label)
    list_label = ["<br>".join(textwrap.wrap(t, width=12)) for t in list_label ]
    return list_label


import plotly.express as px
import plotly.graph_objs as go

import dash_table
import dash_html_components as html

from datetime import date, timedelta, datetime
from helper import transform_to_rupiah_format,transform_to_format,transform_format

import os




parent_path = '/home/server/gli-data-science/akhiyar'
### place for ski data

res_vcr_oshop_g = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/res_vcr_oshop_g.csv'), sep='\t')

df_c1 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_1.csv'), sep='\t')
df_c2 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_2.csv'), sep='\t')
df_c3 = pd.read_csv(os.path.join(parent_path, 'out_plot/voucher_refund/c_3.csv'), sep='\t')

###

###

df_m_2802 = pd.read_csv(os.path.join(parent_path, 'out_plot/df_m_2802.csv'), sep='\t')
df_m_3101 = pd.read_csv(os.path.join(parent_path, 'out_plot/df_m_3101.csv'), sep='\t')

###

## general monitoring
store_type_sales = pd.read_csv(os.path.join(parent_path, 'out_plot/store_type_sales_alfagift_oshop_test.csv'), sep='\t')
store_type_sales['TRO_DATE_ORDER'] = pd.to_datetime(store_type_sales['TRO_DATE_ORDER'])\
										.dt.strftime('%Y-%m')

application_type_sales = pd.read_csv(os.path.join(parent_path, 'out_plot/application_type_sales_alfagift_oshop_test.csv'), sep='\t')
application_type_sales['TRO_DATE_ORDER'] = pd.to_datetime(application_type_sales['TRO_DATE_ORDER'])\
											.dt.strftime('%Y-%m')

order_status = pd.read_csv(os.path.join(parent_path, 'out_plot/order_status.csv'), sep='\t')
order_status['tbto_create_date'] = pd.to_datetime(order_status['tbto_create_date'])\
											.dt.strftime('%Y-%m')
order_status['final_stat_count_str'] = order_status['final_stat_count'].astype('float')\
											.apply(transform_format)

#################################


## member monitoring
sapa_notsapa = pd.read_csv(os.path.join(parent_path, 'out_plot/sapa_notsapa.csv'), sep='\t')
plus_minus = pd.read_csv(os.path.join(parent_path, 'out_plot/plus_minus.csv'), sep='\t', dtype='object')
plus_minus = pd.concat([pd.DataFrame([['2020-10','decrease sales','0','Rp 0','0'],\
										['2020-10','increase sales','0','Rp 0','0']],\
            columns=list(plus_minus)),plus_minus])

oos_status = pd.read_csv(os.path.join(parent_path, 'out_plot/oos_status_spread.csv'), sep='\t')
oos_count = pd.read_csv(os.path.join(parent_path, 'out_plot/order_oos_count.csv'), sep='\t')



oos_consecutive_order = pd.read_csv(os.path.join(parent_path, 'out_plot/consecutive_order_item.csv'), sep='\t')
oos_time_spend = pd.read_csv(os.path.join(parent_path, 'out_plot/time_spend_oos.csv'), sep='\t')


oos_status['month'] = pd.to_datetime(oos_status['month']).dt.strftime('%b%y')
oos_count['month'] = pd.to_datetime(oos_count['month']).dt.strftime('%b%y')
oos_count['value_str'] = oos_count['value'].astype('float').apply(transform_format)
oos_consecutive_order['month'] = pd.to_datetime(oos_consecutive_order['month']).dt.strftime('%b%y')
oos_time_spend['month'] = pd.to_datetime(oos_time_spend['month']).dt.strftime('%b%y')



##################################


def multi_plot(df, addAll = True):
    fig = go.Figure()

    for column in df.columns.to_list():

        fig.add_trace(
            go.Scatter(
                x = df.index,
                y = df[column],
                name = column
            )
        )
        

    button_all = dict(label = 'All',
                      method = 'update',
                      args = [{'visible': df.columns.isin(df.columns),
                               'title': 'All',
                               'showlegend':True}])

    def create_layout_button(column):
        return dict(label = column,
                    method = 'update',
                    args = [{'visible': df.columns.isin([column,column]),
                             'title': column,
                             'showlegend': True}])
    legend=dict(
        x = 0,
        xanchor = 'left',
        y = 1.2,
        yanchor = 'top',
        traceorder="normal",
        title_font_family="Roboto",
        font=dict(
            family="Courier",
            size=14,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=1,
        tracegroupgap=0
    )
    
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b%y",
        showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
    )
    fig.update_yaxes(

        showgrid=True, gridwidth=1, gridcolor='LightPink'
    )
    
    fig.update_layout(
        updatemenus=[go.layout.Updatemenu(
            active = 0,
            buttons = ([button_all] * addAll) + list(df.columns.map(lambda column: create_layout_button(column))),
            x = 0.5,
            xanchor = 'left',
            y = 1.2,
            yanchor = 'top',
            font=dict(
                family="Courier",
                size=14,
                color="black"
            ),
            )
        ], template='presentation', legend=legend)
    
    return fig



def plot_store_type_sales():
	
	fig = px.line(store_type_sales, x='TRO_DATE_ORDER', y='sales_amount', template='presentation', \
	              text='sales_amount_rp', color='store_type')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')
	for ix, trace in enumerate(fig.data):
	    if ix == 1:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig


def plot_application_type_sales():
	fig = px.line(application_type_sales, x='TRO_DATE_ORDER', y='sales_amount', template='presentation', \
	              text='sales_amount_rp', color='store_type')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig

def plot_order_status():
	fig = px.line(order_status, x='tbto_create_date', y='final_stat_count', template='presentation', \
	              text='final_stat_count_str', color='final_stat')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')
	for ix, trace in enumerate(fig.data):
	    if ix == 1:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#order'
	)

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))
	return fig



def plot_new_regular(new_regular, start_date, end_date):


	new_regular['TRO_DATE_ORDER'] = pd.to_datetime(new_regular['TRO_DATE_ORDER'])
	new_regular = new_regular[(new_regular['TRO_DATE_ORDER'] >= start_date) &
								(new_regular['TRO_DATE_ORDER'] <= end_date) ]
	new_regular['member_stat'] = new_regular['member_stat'].replace({'regular':'existing'})
	fig = px.line(new_regular, x='TRO_DATE_ORDER', y='TRO_NET', template='presentation', \
	              text='net_amount', color='member_stat')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{text}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))
	
	return fig

def plot_new_regular_trx(new_regular, start_date, end_date):


	new_regular['TRO_DATE_ORDER'] = pd.to_datetime(new_regular['TRO_DATE_ORDER'])
	new_regular = new_regular[(new_regular['TRO_DATE_ORDER'] >= start_date) &
								(new_regular['TRO_DATE_ORDER'] <= end_date) ]
	new_regular['member_stat'] = new_regular['member_stat'].replace({'regular':'existing'})
	new_regular['member_trx_format'] = new_regular['member_trx'].astype(float)\
									.apply(transform_format)
	fig = px.line(new_regular, x='TRO_DATE_ORDER', y='member_trx', template='presentation', \
	              text='member_trx_format', color='member_stat')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{text}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#member'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))
	
	return fig



def plot_plus_minus():

	fig = px.line(plus_minus, x='date', y='count_member', template='presentation', \
	                color='diff_sign', text='count_member_format')

	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
	for ix, trace in enumerate(fig.data):
	    if ix == 1:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict\
	                  , hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig

def plot_oos_status():

	fig = px.line(oos_status, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2d}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#trx'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_count():


	fig = px.line(oos_count, x='month', y='value', template='presentation', \
	              text='value_str', color='variable')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#attempt'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_oos_consecutive_order():
	fig = px.line(oos_consecutive_order, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text:.2f}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#order'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title = '',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_time_spend():
	
	fig = px.line(oos_time_spend, x='month', y='value', template='presentation', \
	              text='value', color='variable')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=12,
		hovertemplate='%{x}<br>%{y}')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%Y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#amount of time'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="reversed",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=14,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig



def plot_voucher_refund_status():
	df = res_vcr_oshop_g.copy()
	df['tbto_create_date'] = pd.to_datetime(df['tbto_create_date'])
	df = df.groupby([pd.Grouper(key='tbto_create_date',freq='D'), 'WS_DESCRIPTION'])\
	        .agg({'status':'sum'}).reset_index()

	# formatting for beauty
	df['tbtpp_name'] = 'SKI'
	df['tbto_create_date'] = df['tbto_create_date'].dt.strftime('%Y-%m-%d')
	df['tbtpp_name'] = pd.Series(split_label(df['tbtpp_name'])).str.split('&').str[0]


	period_upper = date.today()
	period_lower = (period_upper - timedelta(days=5)) 
	period_upper = period_upper.strftime('%Y-%m-%d')
	period_lower = period_lower.strftime('%Y-%m-%d')


	df = df[(df['tbto_create_date'] >= period_lower) \
	   & (df['tbto_create_date'] <= period_upper)]

	fig = go.Figure()



	colors = ["#B6E2D3", "#e4bad4", '#E7D2CC', '#FFA384', '#D6AD60', '#18A558']
	colors = colors[0:len(df.WS_DESCRIPTION.unique())]
	for r, c in zip(df.WS_DESCRIPTION.unique(), colors):
	    plot_df = df[df.WS_DESCRIPTION == r]
	    #display(plot_df)
	    fig.add_trace(
	        go.Bar(x=[plot_df.tbto_create_date, plot_df.tbtpp_name], y=plot_df.status, \
	               name=r, marker_color=c),
	    )


	legend=dict(
	    x = 0,
	    xanchor = 'left',
	    y = 1.2,
	    yanchor = 'top',
	    traceorder="normal",
	    title_font_family="Roboto",
	    font=dict(
	        family="Courier",
	        size=14,
	        color="black"
	    ),
	    bgcolor="LightSteelBlue",
	    bordercolor="Black",
	    borderwidth=1,
	    tracegroupgap=0
	)
	fig.update_layout(
	    template="presentation",
	    xaxis=dict(
	        title_text="Week",title='',
	        dtick="M1",
	        tickformat="%b%y",
	        showgrid=True, gridwidth=1, gridcolor='LightPink'),
	    yaxis=dict(title_text="#Order",showgrid=True, gridwidth=1),
	    barmode="stack",
	    legend=legend,
	    margin={'l':70, 'r':30, 't':30, 'b':70}
	)

	status_count = res_vcr_oshop_g.groupby('WS_DESCRIPTION').agg({'status':'sum'}).to_dict()['status']
	return fig, status_count




def plot_voucher_refund_c1():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c1)
	df_init['id'] = list(df_c1)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c1.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c1)

def plot_voucher_refund_c2():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c2)
	df_init['id'] = list(df_c2)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c2.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c2)
def plot_voucher_refund_c3():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_c3)
	df_init['id'] = list(df_c3)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=df_c3.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), len(df_c3)


def plot_df_m_2802():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_m_2802)
	df_init['id'] = list(df_m_2802)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	unique_item_ag = df_m_2802[df_m_2802['m_item_ag_len'] > 0].shape[0]
	change_to_online = df_m_2802[df_m_2802['m_online_len'] > 0].shape[0]
	return dash_table.DataTable(


		columns=columns,
		data=df_m_2802.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), unique_item_ag, change_to_online

def plot_df_m_3101():
	df_init = pd.DataFrame()
	df_init['name'] = list(df_m_3101)
	df_init['id'] = list(df_m_3101)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	unique_item_ag = df_m_3101[df_m_3101['m_item_ag_len'] > 0].shape[0]
	change_to_online = df_m_3101[df_m_3101['m_online_len'] > 0].shape[0]
	return dash_table.DataTable(


		columns=columns,
		data=df_m_3101.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'height': '300px', 'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	), unique_item_ag, change_to_online	


