import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_df_m_2802, plot_df_m_3101)


fig_, unique_item_ag, change_to_online = plot_df_m_2802()
fig_3101, unique_item_ag_3101, change_to_online_3101 = plot_df_m_3101()

value_behave_tab = dac.TabItem(id='content_value_behave', 
                              
    children=[
        html.H4('Online-offline switching behavior'),
        html.Div([
            dac.ValueBox(
            	value = unique_item_ag,
              subtitle ='User always buy different item on online (alfagift) transaction',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = change_to_online,
              subtitle = 'User change their item buy from offline to online (alfagift)',
              color = "info",
              icon = "database"
            ),
        ], className='row'),
        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Detail jan21-feb21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_,className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Detail dec20-jan21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_3101,className="card-text",
                              ),
                          ]),
                  ])),


            ],className="md-12")
        ], className='column')
    ]
)