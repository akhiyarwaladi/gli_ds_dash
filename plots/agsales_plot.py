import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime, timedelta

pd.set_option('display.float_format', lambda x: '%.3f' % x)
import matplotlib.pyplot as plt

from helper import transform_to_rupiah_format, transform_to_rupiah
import numpy as np
import os
import time


def plot_sales_all(sales_plot, value, date_start, date_end):
	# give anotation text every x gap
	gap_anot = 30

	sales_plot = sales_plot[(sales_plot['index'] >= date_start) &
	                            (sales_plot['index'] <= date_end) ]

	# change grouping if selected monthly
	if value == 'Monthly':
	    sales_plot = sales_plot.groupby([pd.Grouper(key='index',freq='M')])\
	                .agg({'TRO_NET':'sum','TRO_NET_PRED':'sum'}).reset_index()
	    sales_plot['index'] = sales_plot['index'].dt.strftime('%Y-%m')
	    gap_anot = 1



	fig = go.Figure()
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET'],
	    name='Actual',
	    text=sales_plot['TRO_NET'].astype(float).apply(transform_to_rupiah),
	    mode="lines+markers",

	))
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET_PRED'],
	    name='Prediction',
	    text=sales_plot['TRO_NET_PRED'].astype(float).apply(transform_to_rupiah),
	    mode="lines+markers",
	))

	for i, r in sales_plot.iterrows():
	    if i%gap_anot == 0:
	        # if not np.isnan(r['TRO_NET']):
	        #     fig.add_annotation(x=r['index'], y=r['TRO_NET'],
	        #             text=transform_to_rupiah(r['TRO_NET']),
	        #             showarrow=True,
	        #             ax=10,
	        #             ay=25,
	        #             arrowhead=1)
	        if not np.isnan(r['TRO_NET_PRED']):
	            fig.add_annotation(x=r['index'], y=r['TRO_NET_PRED'],
	                    text=transform_to_rupiah(float(int(r['TRO_NET_PRED']))),
	                   	font=dict(
			                family="Roboto",
			                size=13,
			                color="black"
			            ),
	                    showarrow=True,
	                    ax=-10,
	                    ay=-45,
	                    arrowhead=1)

	fig.update_traces(

	    hovertemplate='%{x}<br>%{text}')

	fig.update_xaxes(
	    tickformat="%d%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)

	legend_dict = \
	    legend=dict(
	    		orientation="h",
				yanchor="bottom",
				y=0.95,
				xanchor="left",
				x=0,
	            traceorder="normal",
	            title='',
	            title_font_family="Courier",
	            font=dict(
	                family="Courier",
	                size=16,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout( 
		  xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
                       'showgrid': True, 'automargin': True, 'title':''},
                yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                       'showgrid': True,  'automargin': True, 'title':'sales (Rp)'},
					  uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict,\
	                  template='presentation', hoverlabel=dict(font=dict(family='sans-serif', size=17)))
	return fig


def plot_sales_promo(sales_plot):

	fig = go.Figure()
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET'],
	    name='Actual',
	    text=sales_plot['TRO_NET'].astype(float).apply(transform_to_rupiah),
	    mode="lines+markers+text",
	    textposition="top center"
	))
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET_PRED'],
	    name='Prediction',
	    text=sales_plot['TRO_NET_PRED'].astype(float).apply(transform_to_rupiah),
	    mode="lines+markers+text",
	    textposition="top center"
	))


	fig.update_traces(

	    hovertemplate='%{x}<br>%{text}')

	fig.update_xaxes(
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)

	legend_dict = \
	    legend=dict(
	            orientation="h",
	            yanchor="bottom",
	            y=0.95,
	            xanchor="left",
	            x=0,
	            traceorder="normal",
	            title='',
	            title_font_family="Courier",
	            font=dict(
	                family="Courier",
	                size=16,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout( 
	      xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                   'showgrid': True, 'automargin': True, 'title':''},
	            yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                   'showgrid': True,  'automargin': True, 'title':'sales (Rp)'},
	                  uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':0, 'b':70},legend=legend_dict,\
	                  template='presentation', hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig


def plot_sales_jsm(sales_plot, start_date, end_date, promo_name, value):


	sales_plot = sales_plot[(sales_plot['index'] >= start_date) &
				(sales_plot['index'] <= end_date)]


	if value == 'Monthly':
	    sales_plot = sales_plot.groupby([pd.Grouper(key='index',freq='M')])\
	                .agg({'TRO_NET':'sum','TRO_NET_PRED':'sum','yhat_upper':'sum', 'yhat_lower':'sum'}).reset_index()


	fig = go.Figure()
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET'],
	    name='Actual',
	    text=sales_plot['index'].dt.strftime("%A") + '<br>' + sales_plot['TRO_NET'].astype(int,  errors = 'ignore').astype(float, errors = 'ignore').apply(transform_to_rupiah),
	    mode="lines+markers",
	    textposition="top center"
	))
	fig.add_trace(
	    go.Scatter(
	        x=sales_plot['index'],
	        y=sales_plot['TRO_NET_PRED'],
	        name='Prediction',
	        text=sales_plot['index'].dt.strftime("%A") + '<br>' + sales_plot['TRO_NET_PRED'].astype(int, errors = 'ignore').astype(float,  errors = 'ignore').apply(transform_to_rupiah),
	        mode="lines+markers",
	        textposition="top center"
	    ),



	)
	fig.add_trace(
	    go.Scatter(
	        name='Upper Bound',
	        x=sales_plot['index'],
	        y=sales_plot['yhat_upper'],
	        mode='lines',
	        marker=dict(color="#444"),
	        line=dict(width=0),
	        text = sales_plot['yhat_upper'].astype(int).astype(float).apply(transform_to_rupiah),
	        showlegend=False
	    ),
	)
	fig.add_trace(
	    go.Scatter(
	        name='Lower Bound',
	        x=sales_plot['index'],
	        y=sales_plot['yhat_lower'],
	        marker=dict(color="#444"),
	        line=dict(width=0),
	        mode='lines',
	        fillcolor='rgba(255, 190, 118, 0.4)',
	        fill='tonexty',
	        text = sales_plot['yhat_lower'].astype(int).astype(float).apply(transform_to_rupiah),
	        showlegend=False
	    )

	)


	fig.update_traces(

	    hovertemplate='%{x}<br>%{text}')

	fig.update_xaxes(
	    tickformat="%d%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='sales_amount'
	)

	legend_dict = \
	    legend=dict(
	            orientation="h",
	            yanchor="bottom",
	            y=0.95,
	            xanchor="left",
	            x=0,
	            traceorder="normal",
	            title='',
	            title_font_family="Courier",
	            font=dict(
	                family="Courier",
	                size=16,
	                color="black"
	            ),
	            bgcolor="#dfe4ea",
	            bordercolor="Black",
	            borderwidth=1
	        )
	fig.update_layout( title=promo_name,
	      xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                   'showgrid': True, 'automargin': True, 'title':''},
	            yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                   'showgrid': True,  'automargin': True, 'title':'sales (Rp)'},
	                  uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':70, 'b':70},legend=legend_dict,\
	                  template='presentation', hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig