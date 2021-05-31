import numpy as np 
import pandas as pd
import os
import textwrap

import plotly.express as px
import plotly.graph_objs as go
import dash_table
import dash_html_components as html
from datetime import date, timedelta, datetime

from helper import transform_to_rupiah_format,transform_to_format,transform_format


def split_label(list_label):
    list_label = list(list_label)
    list_label = ["<br>".join(textwrap.wrap(t, width=12)) for t in list_label ]
    return list_label


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
store_type_sales = pd.read_csv(os.path.join(parent_path, 'out_plot/store_type_sales.csv'), sep='\t')
store_type_sales['tbto_create_date'] = pd.to_datetime(store_type_sales['tbto_create_date']).dt.strftime('%Y-%m')

application_type_sales = pd.read_csv(os.path.join(parent_path, 'out_plot/application_type_sales.csv'), sep='\t')
application_type_sales['tbto_create_date'] = pd.to_datetime(application_type_sales['tbto_create_date']).dt.strftime('%Y-%m')

order_status = pd.read_csv(os.path.join(parent_path, 'out_plot/order_status.csv'), sep='\t')
order_status['tbto_create_date'] = pd.to_datetime(order_status['tbto_create_date']).dt.strftime('%Y-%m')
order_status['final_stat_count_str'] = order_status['final_stat_count'].astype('float').apply(transform_format)

##


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

###
res_g = pd.read_csv(os.path.join(parent_path, 'out_plot/res_g.csv'), sep='\t')
all_df_pred = pd.read_csv(os.path.join(parent_path, 'out_plot/all_df_pred.csv'), sep='\t')

res_unstack = res_g.set_index(["TRO_DATE", "DESCP_DEPT"])['TRO_NET'].unstack(level=1).fillna(0)
pred_unstack = all_df_pred.set_index(["TRO_DATE", "DESCP_DEPT"])['TRO_NET'].unstack(level=1).fillna(0)



###


###
general_push = pd.read_csv(os.path.join(parent_path, \
	'data_req/event/general_push.csv'), sep='\t')

g_push = pd.read_csv(os.path.join(parent_path, \
	'out_plot/g_push.csv'), sep='\t')
g_email = pd.read_csv(os.path.join(parent_path, \
	'out_plot/g_push.csv'), sep='\t')

general_inapp = pd.read_csv(os.path.join(parent_path, \
	'data_req/event/MOBILE_INAPP_alfagift_2021-04-21_04_37_38.555413.csv')).fillna(0)
###



view_product1 = pd.read_csv(os.path.join(parent_path,'out_plot/view_1.csv'),sep='\t')
view_product2 = pd.read_csv(os.path.join(parent_path,'out_plot/view_2.csv'),sep='\t')
search_product = pd.read_csv(os.path.join(parent_path, 'out_plot/search_event.csv'), sep='\t')


uvp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/user_view_product.csv')
usp = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/user_search_product.csv')

def plot_vp(vp, value):
	# vp['view_product - product_name'] = pd.to_datetime(vp['view_product - product_name']).dt.strftime('%Y-%m')
	
	fig = px.line(vp, x='view_product - product_name', y=vp[str(value)], template='ggplot2',\
		text=vp[str(value)])
	fig.update_traces(
	    texttemplate='%{text:.2s}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{y}'
	)

	fig.update_xaxes(
	#     dtick="M1",
	    tickformat="%d%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='total_view'
	)

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=-0.4,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	title={
	    'text': value,
	    'y':1,
	    'x':0.9,
	    'xanchor': 'right',
	    'yanchor': 'top',
		'font': {
		    'family':"Courier",
		    'size':20,
		    'color':"black"}
	}
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict,title=title)

	return fig

def plot_sp(sp, value):
	fig = px.line(sp, x='search_products - keyword', y=sp[str(value)], template='ggplot2',\
		text=sp[str(value)])
	fig.update_traces(
	    texttemplate='%{text:.2s}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{y}'
	)

	fig.update_xaxes(
	#     dtick="M1",
	    tickformat="%d%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='total_search'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=-0.4,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	title={
	    'text': value,
	    'y':1,
	    'x':0.9,
	    'xanchor': 'right',
	    'yanchor': 'top',
		'font': {
		    'family':"Courier",
		    'size':20,
		    'color':"black"}
	}
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict, title=title)
	# Show plot 
	# fig.show()

	return fig

def plot_uvp():
	fig = px.line(uvp, x='view_product - uid', y=uvp.columns[1:7], template='ggplot2')
	fig.update_traces(
	#     texttemplate='%{text}', 
	#     textposition='top center', 
	#     textfont_size=11,
	    hovertemplate='%{x}<br>%{y}')

	fig.update_xaxes(
	#     dtick="M1",
	#     tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='total_event'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=-0.4,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	# Show plot 
	#fig.show()

	return fig, round(uvp.mean(axis=1).mean(),2)

def plot_usp():
	fig = px.line(usp, x='search_products - uid', y=usp.columns[1:7], template='ggplot2')
	fig.update_traces(
	#     texttemplate='%{text}', 
	#     textposition='top center', 
	#     textfont_size=11,
	    hovertemplate='%{x}<br>%{y}')

	fig.update_xaxes(
	#     dtick="M1",
	#     tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='total_event'
	)
	legend_dict = \
	    legend=dict(
	            x=0,
	            y=-0.4,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	# Show plot 
	#fig.show()
	return fig, round(usp.mean(axis=1).mean(), 2)


def plot_view_product1():
	df_init = pd.DataFrame()
	df_init['name'] = list(view_product1)
	df_init['id'] = list(view_product1)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=view_product1.to_dict('records'),
		tooltip_data=[
		    {
		        column: {'value': str(value), 'type': 'markdown'}
		        for column, value in row.items()
		    } for row in view_product1.to_dict('records')
		],

		# Overflow into ellipsis
		style_cell={
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		    'maxWidth': 0,
		},
		tooltip_delay=0,
		tooltip_duration=None,
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '120px', 'minWidth': '120px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	)

def plot_view_product2():
	df_init = pd.DataFrame()
	df_init['name'] = list(view_product2)
	df_init['id'] = list(view_product2)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')

	return dash_table.DataTable(


		columns=columns,
		data=view_product2.to_dict('records'),
		tooltip_data=[
		    {
		        column: {'value': str(value), 'type': 'markdown'}
		        for column, value in row.items()
		    } for row in view_product2.to_dict('records')
		],

		# Overflow into ellipsis
		style_cell={
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		    'maxWidth': 0,
		},
		tooltip_delay=0,
		tooltip_duration=None,
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '120px', 'minWidth': '120px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	)

def plot_search_product():
	df_init = pd.DataFrame()
	df_init['name'] = list(search_product)
	df_init['id'] = list(search_product)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=search_product.to_dict('records'),
		tooltip_data=[
		    {
		        column: {'value': str(value), 'type': 'markdown'}
		        for column, value in row.items()
		    } for row in search_product.to_dict('records')
		],

		# Overflow into ellipsis
		style_cell={
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		    'maxWidth': 0,
		},
		tooltip_delay=0,
		tooltip_duration=None,
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '120px', 'minWidth': '120px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	)


def plot_general_push():

	return general_push

def g_general_push():

	fig = px.line(g_push, x='Campaign Sent Time', y='value', template='ggplot2', \
	              text='value_format', color='variable')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')
	for ix, trace in enumerate(fig.data):
	    if ix == 3:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#'
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def g_general_email():
	fig = px.line(g_email, x='Date', y='value', template='ggplot2', \
	              text='value_format', color='variable')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')
	for ix, trace in enumerate(fig.data):
	    if ix == 3:
	        trace.update(textposition='bottom center')
	fig.update_xaxes(
	    dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#'
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig


def click_general_push():
	top_click = general_push.sort_values(by=['Clicks'], ascending=False).head(7)\
	            [['Campaign Name', 'Clicks', 'Primary Conversion Goal']].reset_index(drop=True)
	top_click['Campaign Name'] = pd.Series(split_label(top_click['Campaign Name'].str[10:]))

	fig = px.bar(top_click, x="Campaign Name", y="Clicks", color = 'Primary Conversion Goal')

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(font={'size': 16}, width=1000,template='ggplot2',
	                plot_bgcolor = '#FFFFFF', legend = legend_dict,
	                xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                       'showgrid': True, 'automargin': True, 'title':''},
	                yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                       'showgrid': True,  'automargin': True, 'title':'Clicks'},
	                bargap=0.3, title="", title_x=0.5)

	return fig

def conversion_general_push():
	top_click = general_push.sort_values(by=['Conversions'], ascending=False).head(7)\
	            [['Campaign Name', 'Conversions', 'Primary Conversion Goal']].reset_index(drop=True)
	top_click['Campaign Name'] = pd.Series(split_label(top_click['Campaign Name'].str[10:]))

	fig = px.bar(top_click, x="Campaign Name", y="Conversions", color='Primary Conversion Goal')

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )

	fig.update_layout(font={'size': 16}, width=1000,template='ggplot2',
	            plot_bgcolor = '#FFFFFF', legend = legend_dict,
	            xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                   'showgrid': True, 'automargin': True, 'title':''},
	            yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                   'showgrid': True,  'automargin': True, 'title':'Conversions'},
	            bargap=0.3, title="", title_x=0.5)

	return fig



def plot_general_inapp():

	return general_inapp

def g_general_inapp():
	general_inapp['Created At'] = pd.to_datetime(general_inapp['Created At'])
	g_inapp = general_inapp.groupby([pd.Grouper(key='Created At',freq='M')])\
	                    .agg({'impressions':'sum', 'clicks':'sum', 'conversions (unique)':'sum'})\
	                    .reset_index()
	g_inapp['Created At'] = g_inapp['Created At'].dt.strftime('%Y-%m')
	g_inapp = pd.melt(g_inapp, ['Created At'])
	g_inapp['value_format'] = g_inapp['value'].astype('float')\
								.apply(transform_to_format)

	fig = px.line(g_inapp, x='Created At', y='value', template='ggplot2', \
	              text='value_format', color='variable')
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

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#'
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig


def click_general_inapp():
	top_click = general_inapp.sort_values(by=['clicks'], ascending=False).head(7)\
	            [['Campaign Name', 'clicks', 'Conversion Goal']].reset_index(drop=True)
	top_click['Campaign Name'] = pd.Series(split_label(top_click['Campaign Name']\
	                                .str[7:]))

	fig = px.bar(top_click, x="Campaign Name", y="clicks", color = 'Conversion Goal')

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )

	fig.update_layout(font={'size': 16}, width=1000,template='ggplot2',
	                plot_bgcolor = '#FFFFFF', legend=legend_dict,
	                xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                       'showgrid': True, 'automargin': True, 'title':''},
	                yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                       'showgrid': True,  'automargin': True, 'title':'Clicks'},
	                bargap=0.3, title="", title_x=0.5)

	return fig

def conversion_general_inapp():

	top_click = general_inapp.sort_values(by=['conversions (unique)'], ascending=False).head(7)\
	            [['Campaign Name', 'conversions (unique)', 'Conversion Goal']].reset_index(drop=True)
	top_click['Campaign Name'] = pd.Series(split_label(top_click['Campaign Name']\
	                                .str[7:]))

	fig = px.bar(top_click, x="Campaign Name", y="conversions (unique)", color = 'Conversion Goal')

	legend_dict = \
	    legend=dict(
	            x=0,
	            y=1,
	            traceorder="normal",
	            title='',
	            title_font_family="Times New Roman",
	            font=dict(
	                family="Courier",
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )

	fig.update_layout(font={'size': 16}, width=1000,template='ggplot2',
	                plot_bgcolor = '#FFFFFF', legend=legend_dict,
	                xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                       'showgrid': True, 'automargin': True, 'title':''},
	                yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                       'showgrid': True,  'automargin': True, 'title':'Clicks'},
	                bargap=0.3, title="", title_x=0.5)

	return fig


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
        ], template='ggplot2', legend=legend)
    
    return fig


def plot_sales_train():
	return multi_plot(res_unstack)

def plot_sales_test():
	return multi_plot(pred_unstack)

def plot_sales_all(sales_plot, value):

	if value == 'Monthly':
		sales_plot = sales_plot.groupby([pd.Grouper(key='index',freq='M'), 'type'])\
							.agg({'tbtop_amount_final':'sum'})\
							.reset_index()
		sales_plot['index'] = sales_plot['index'].dt.strftime('%Y-%m')
		
	fig = px.line(sales_plot, x='index', y='tbtop_amount_final', template='ggplot2', \
	              color='type')
	fig.update_traces(
	#     texttemplate='%{text}', 
	#     textposition='top center', 
	#     textfont_size=11,
	    hovertemplate='%{x}<br>%{y}')

	fig.update_xaxes(
	#     dtick="M1",
	#     tickformat="%b%y",
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig


def plot_table_sales(sales_plot_table, value):

	# if value == 'Monthly':
	# 	sales_plot_table['index'] = pd.to_datetime(sales_plot_table['index'])
	# 	sales_plot_table = sales_plot_table.groupby([pd.Grouper(key='index',freq='M')])\
	# 						.agg({'actual':'sum', 'prediction':'sum'})\
	# 						.reset_index()
		
	# 	## formatting view
	# 	sales_plot_table['index'] = sales_plot_table['index'].dt.strftime('%d%b%y')

	# 	sales_plot_table['prediction'] = sales_plot_table['prediction'].astype('float').apply(transform_to_rupiah_format)
	# 	sales_plot_table['actual'] = sales_plot_table['actual'].astype('float').apply(transform_to_rupiah_format)
	# 	sales_plot_table = sales_plot_table.rename(columns={'index':'date', 'type':''})
	# 	##
	# else:
	# 	## formatting view
	# 	sales_plot_table['index'] = sales_plot_table['index'].dt.strftime('%d%b%y')

	# 	sales_plot_table['prediction'] = sales_plot_table['prediction'].astype('float').apply(transform_to_rupiah_format)
	# 	sales_plot_table['actual'] = sales_plot_table['actual'].astype('float').apply(transform_to_rupiah_format)
	# 	sales_plot_table = sales_plot_table.rename(columns={'index':'date', 'type':''})
	# 	##


	df_init = pd.DataFrame()
	df_init['name'] = list(sales_plot_table)
	df_init['id'] = list(sales_plot_table)
	df_init['type'] = 'text'
	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(


		columns=columns,
		data=sales_plot_table.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'width': '120px', 'minWidth': '120px', 'maxWidth': '150px',
		    'overflow': 'hidden',
		    'textOverflow': 'ellipsis',
		}
	)

def plot_store_type_sales():
	
	fig = px.line(store_type_sales, x='tbto_create_date', y='sales_amount', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig


def plot_application_type_sales():
	fig = px.line(application_type_sales, x='tbto_create_date', y='sales_amount', template='ggplot2', \
	              text='sales_amount_rp', color='store_type')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{y}')
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_order_status():
	fig = px.line(order_status, x='tbto_create_date', y='final_stat_count', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig


def plot_sapa_notsapa():
	
	sapa_notsapa['sapa_enable'] = sapa_notsapa['sapa_enable'].replace({'not_sapa':'non_sapa'})
	fig = px.line(sapa_notsapa, x='tbto_create_date', y='net_amount', template='ggplot2', \
	              text='tbto_amount_final_rp', color='sapa_enable')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_new_regular(new_regular, start_date, end_date):


	new_regular['tbto_create_date'] = pd.to_datetime(new_regular['tbto_create_date'])
	new_regular = new_regular[(new_regular['tbto_create_date'] >= start_date) &
								(new_regular['tbto_create_date'] <= end_date) ]
	new_regular['member_stat'] = new_regular['member_stat'].replace({'regular':'existing'})
	fig = px.line(new_regular, x='tbto_create_date', y='tbto_amount_final', template='ggplot2', \
	              text='net_amount', color='member_stat')
	fig.update_traces(texttemplate='%{text}', 
		textposition='top center', 
		textfont_size=11,
		hovertemplate='%{x}<br>%{y}')
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	
	return fig

def plot_plus_minus():

	fig = px.line(plus_minus, x='date', y='count_member', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_status():

	fig = px.line(oos_status, x='month', y='value', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_count():


	fig = px.line(oos_count, x='month', y='value', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)
	return fig

def plot_oos_consecutive_order():
	fig = px.line(oos_consecutive_order, x='month', y='value', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

def plot_oos_time_spend():
	
	fig = px.line(oos_time_spend, x='month', y='value', template='ggplot2', \
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
	                size=12,
	                color="black"
	            ),
	            bgcolor="LightGrey",
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
	    template="ggplot2",
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


