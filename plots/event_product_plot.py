import numpy as np 
import pandas as pd
import os
import textwrap

import plotly.express as px
import plotly.graph_objs as go
from helper import rupiah_format


def plot_vp(vp, value):
	# vp['view_product - product_name'] = pd.to_datetime(vp['view_product - product_name']).dt.strftime('%Y-%m')
	
	fig = px.line(vp, x='view_product - product_name', y=vp[str(value)], template='presentation',\
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
	fig = px.line(sp, x='search_products - keyword', y=sp[str(value)], template='presentation',\
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

def plot_general_event(sales_plot, start_date, end_date):

	sales_plot = sales_plot[(sales_plot['Event Time'] >= start_date) &
							(sales_plot['Event Time'] <= end_date)]


	fig = go.Figure()
	fig.add_trace(go.Scatter(
	    x=sales_plot['Event Time'],
	    y=sales_plot['App Update'],
	    name='App Update',
	    text=sales_plot['App Update'].apply(rupiah_format),
	    mode="lines+markers",
	    textposition="top center"
	))
	fig.add_trace(go.Scatter(
	    x=sales_plot['Event Time'],
	    y=sales_plot['INSTALL'],
	    name='INSTALL',
	    text=sales_plot['INSTALL'].apply(rupiah_format),
	    mode="lines+markers",
	    textposition="top center"
	))
	fig.add_trace(go.Scatter(
	    x=sales_plot['Event Time'],
	    y=sales_plot['Device Uninstall'],
	    name='Device Uninstall',
	    text=sales_plot['Device Uninstall'].apply(rupiah_format),
	    mode="lines+markers",
	    textposition="top center"
	))

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
	                   'showgrid': True,  'automargin': True, 'title':'#'},
	                  uniformtext_minsize=8, uniformtext_mode='hide', margin=\
	                  {'l':70, 'r':30, 't':70, 'b':70},legend=legend_dict,\
	                  template='presentation', hoverlabel=dict(font=dict(family='sans-serif', size=17)))

	return fig