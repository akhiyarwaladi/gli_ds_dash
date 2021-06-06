import numpy as np 
import pandas as pd
import os
import textwrap

import plotly.express as px

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
