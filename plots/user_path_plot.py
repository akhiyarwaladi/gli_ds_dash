import pandas as pd
import numpy as np
import plotly.express as px
import dash_table

from loader.user_path_load import get_uninstall_review
uninstall_review = get_uninstall_review()
uninstall_review_table = uninstall_review[0]


def plot_uninstall_review():
	df_init = pd.DataFrame()
	df_init['name'] = list(uninstall_review_table)
	df_init['id'] = list(uninstall_review_table)

	li_type = ['numeric', 'numeric', 'text']
	li_format = [np.nan, np.nan, np.nan]
	df_init['type'] = li_type
	df_init['format'] = li_format

	columns = df_init.to_dict(orient='records')
	return dash_table.DataTable(

		id='datatable_uninstall_review',
		columns=columns,
		data=uninstall_review_table.to_dict('records'),
		filter_action='native',
		page_size=20,
		fixed_rows={'headers': True},
		style_table={'overflowY': 'scroll', 'overflowX': 'scroll'},
		style_data={
		    'minWidth': '10px', 'maxWidth': '350px',

		},

	    style_cell_conditional=
	    [
	        {
	            'if': {'column_id': c},
	            'textAlign': 'right',
	            'width': '350px',
	            'height':'auto',
	            'fontSize':16, 
	            'font-family':'sans-serif',
	            'padding':'10px',
	            'whiteSpace':'normal'
	        } for c in ['review']

	    ] + 
	    [
	        {
	            'if': {'column_id': d},
	            'textAlign': 'left',
	            'width': '20px',
	            'fontSize':13, 
	            'font-family':'monospace',
	            'padding':'5px'
	        } for d in ['ponta_user']

	    ]+ 
	    [
	        {
	            'if': {'column_id': e},
	            'textAlign': 'left',
	            'width': '20px',
	            'fontSize':14, 
	            'font-family':'monospace',
	            'padding':'5px'
	        } for e in ['rating']

	    ]+
		[
	        {
				'if': {'column_id': 'rating'},
				'width': '20px'
            },
	        {
				'if': {'column_id': 'ponta_user'},
				'width': '20px'
            },
	        {
				'if': {'column_id': 'review'},
				'width': '350px'
            },
		],
	    style_data_conditional=[
	        {
	            'if': {'row_index': 'odd'},
	            'backgroundColor': 'rgb(248, 248, 248)'
	        },
	        
	    ],
	    style_header={
	        'backgroundColor': 'rgb(230, 230, 230)',
	        'fontWeight': 'bold', 'fontSize':19, 'font-family':'sans-serif',
	        'textOverflow': 'inherit'
	    },

		tooltip_data=[
		    {
		        column: {'value': str(value), 'type': 'markdown'}
		        for column, value in row.items()
		    } for row in uninstall_review_table.to_dict('records')
		],
		tooltip_duration=None
	)

def plot_app_update(app_update):
	fig = px.line(app_update, x='Event Time', y='App Update', template='ggplot2',\
	    text='App Update')
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
	    'text': 'APP update',
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

def plot_device_uninstall(device_uninstall):

	fig = px.line(device_uninstall, x='Event Time', y='Device Uninstall', template='ggplot2',\
	    text='Device Uninstall')
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
	    'text': 'Device Uninstall',
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






def plot_notification_received(notification_received):
	fig = px.line(notification_received, x='Event Time', y='Notification Received Android', template='ggplot2',\
	    text='Notification Received Android')
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
	    'text': 'Notification Received',
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



def plot_review_gram(df_gram):


	fig = px.bar(df_gram, y="index", x='value', \
	                orientation='h', title="Wide-Form Input")

	height_weight = 15

	legend_dict=\
	    legend=dict(
	        orientation="h",
	        traceorder="normal",
	        yanchor="bottom",
	        y=1,
	        xanchor="right",
	        x=1,
	        title=''
	    )

	fig.update_layout(font={'size': 11}, width=1000,template='seaborn',
	                plot_bgcolor = '#FFFFFF',height=height_weight*45,
	                xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
	                       'showgrid': True, 'automargin': True, 'title':'#'},
	                yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
	                       'showgrid': True,  'automargin': True, 'title':'pair word'},
	                bargap=0.2, title="Play store review (1-3) star", title_x=0.5,\
	                legend=legend_dict, margin={'l':70, 'r':70, 't':70, 'b':70}, barmode='stack')

	return fig