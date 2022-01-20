import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def plot_member_count(am, value):
	#value = 'Monthly'

	if value == 'Monthly':
	    am = am.groupby([pd.Grouper(key='index',freq='M')]).agg({'count':'last','count_format':'last'}).reset_index()
	    am['index'] = am['index'].dt.strftime('%Y-%m')

	fig = px.line(am, x='index', y='count', template='presentation', \
	              text='count_format')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')

	fig.update_xaxes(
	#     dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	if value == 'Daily':
		fig.update_xaxes(
		#     dtick="M1",
		    tickformat="%d%b%y",
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
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig



def plot_sapa_count(am, value):
	#value = 'Monthly'

	if value == 'Monthly':
	    am = am.groupby([pd.Grouper(key='index',freq='M')]).agg({'count':'first','count_format':'first'}).reset_index()
	    am['index'] = am['index'].dt.strftime('%Y-%m')
	    am = am[-10:-1]
	    
	am = am[0:9]
	fig = px.line(am, x='index', y='count', template='presentation', \
	              text='count_format')
	fig.update_traces(texttemplate='%{text}', 
	    textposition='top center', 
	    textfont_size=11,
	    hovertemplate='%{x}<br>%{text}')

	fig.update_xaxes(
	#     dtick="M1",
	    tickformat="%b%y",
	    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
	)
	if value == 'Daily':
		fig.update_xaxes(
		#     dtick="M1",
		    tickformat="%d%b%y",
		    showgrid=True, gridwidth=1, gridcolor='LightPink', title=''
		)
		
	fig.update_yaxes(

	    showgrid=True, gridwidth=1, gridcolor='LightPink', title='#sapa store'
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
	                  {'l':70, 'r':30, 't':30, 'b':70},legend=legend_dict)

	return fig

