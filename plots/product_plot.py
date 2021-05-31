import plotly.express as px
import plotly.graph_objs as go


def plot_product(plu_group, value_1, value_2):
    value_1 = '2021-05'
    value_2 = 'TRO_NET'
    if value_2 == 'TRO_NET':
        plu_group = plu_group[plu_group['TRO_DATE_ORDER'] == value_1].sort_values(value_2).tail(10)
    elif value_2 == 'TRO_QTY':
        plu_group = plu_group[plu_group['TRO_DATE_ORDER'] == value_1].sort_values(value_2).tail(10)

    height_weight = len(plu_group)
        
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=plu_group[value_2],
        y=plu_group['product_name'],
        name=value_2,
        text=plu_group[value_2],
        textposition='auto',
        texttemplate='%{text:.2s}',
        orientation='h'
    ))



    fig.update_traces(
        hovertemplate='%{x}')

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
                    plot_bgcolor = '#FFFFFF',height=height_weight*55,
                    xaxis={'showline': True, 'visible': True, 'showticklabels': True, \
                           'showgrid': True, 'gridcolor':'LightPink', 'automargin': True, 'title':'{}'.format(value_2)},
                    yaxis={'showline': False, 'visible': True, 'showticklabels': True,\
                           'showgrid': True, 'gridcolor':'LightPink',  'automargin': True, 'title':'product_name'},
                    bargap=0.2, title="Product {} sort by {}".format(value_1, value_2), title_x=0.5,\
                    legend=legend_dict, margin={'l':70, 'r':70, 't':70, 'b':70})
