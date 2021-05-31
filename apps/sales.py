import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_sales_train, plot_sales_test)
fig_sales_train, fig_sales_test = plot_sales_train(), plot_sales_test()


from loader.agsales_load import get_agsales
sales_plot = get_agsales()



sales_tab = dac.TabItem(id='content_sales', 
                              
    children=[
        html.H4('Alfagift Sales'),

        html.Div([
           
            dbc.Row([
               dbc.Col(
                
                  dbc.Card(
                    [
                        dbc.CardHeader(
                          [
                            dbc.Row([
                              dbc.Col(html.Div("Overall sales, actual and prediction"), md=8),
                              dbc.Col(
                                dcc.Dropdown(
                                    id='demo-dropdown',
                                    options=[
                                        {'label': 'Monthly', 'value': 'Monthly'},
                                        {'label': 'Daily', 'value': 'Daily'}
                                    ],
                                    value='Daily'
                                ), md=4),
                            ])
                          ]
                        ),
                        dbc.CardBody(
                            [
                                # html.H5("Card title", className="card-title"),
                                html.P(
                                      dcc.Graph(
                                        # figure=fig_sales_all,
                                        # config=dict(displayModeBar=False),
                                        id='sales_fig',
                                        config=dict(displayModeBar=False),

                                        ),className="card-text",
                                ),
                            ]),
                    ], style={'height':'120vh'}), md=12),
              # dbc.Col(
              #   dbc.Card(
              #     [
              #         # dbc.CardHeader("Detail jan21-feb21"),
              #         dbc.CardBody(
              #             [
              #                 # html.H5("Card title", className="card-title"),
              #                 html.Div(
                                      
              #                     id='sales_table',

              #                 ),
              #             ]),
              #     ], style={'height':'120vh'}), md=4),

            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Sales training data 01jan20 - 17mar21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=fig_sales_train,
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]), md=12),
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Sales prediction 18mar21 - 28mar21"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=fig_sales_test,
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]), md=12),
            ]),
        ])
    ]
)