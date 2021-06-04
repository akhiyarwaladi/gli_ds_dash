import pandas as pd
import plotly.express as px

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
