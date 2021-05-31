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


def plot_sales_all(sales_plot, value):
	gap_anot = 15
	
	if value == 'Monthly':
	    sales_plot = sales_plot.groupby([pd.Grouper(key='index',freq='M')])\
	                .agg({'TRO_NET':'sum','TRO_NET_PRED':'sum'}).reset_index()
	    sales_plot['index'] = sales_plot['index'].dt.strftime('%Y-%m')
	    gap_anot = 1



	

	# fig = px.line(sales_plot, x='index', y='TRO_NET', template='presentation', \
	#               color='type')

	fig = go.Figure()
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET'],
	    name='Actual',

	))
	fig.add_trace(go.Scatter(
	    x=sales_plot['index'],
	    y=sales_plot['TRO_NET_PRED'],
	    name='Prediction',
	))

	for i, r in sales_plot.iterrows():
	    if i%gap_anot == 0:
	        if not np.isnan(r['TRO_NET']):
	            fig.add_annotation(x=r['index'], y=r['TRO_NET'],
	                    text=transform_to_rupiah(r['TRO_NET']),
	                    showarrow=True,
	                    ax=10,
	                    ay=25,
	                    arrowhead=1)
	        if not np.isnan(r['TRO_NET_PRED']):
	            fig.add_annotation(x=r['index'], y=r['TRO_NET_PRED'],
	                    text=transform_to_rupiah(r['TRO_NET_PRED']),
	                    showarrow=True,
	                    ax=10,
	                    ay=25,
	                    arrowhead=1)

	fig.update_traces(
	    hovertemplate='%{x}<br>%{y}')

	fig.update_xaxes(
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
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict,template='ggplot2')
	return fig