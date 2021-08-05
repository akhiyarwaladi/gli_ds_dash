import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

## for load csv file
from loader.agsales_load import get_agsales
sales_plot = get_agsales()

## for daterange picker
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

## define date picker start date and end date
start_picker = dt(2021,1,1)
end_picker = dt.today().date() - relativedelta(days=2)


sales_tab = dac.TabItem(id='content_sales', 
                              
    children=[
        

        html.Div([
           
            dbc.Row([
               dbc.Col(
                
                  dbc.Card(
                    [
                        dbc.CardHeader(
                          [
                            dbc.Row([
                              dbc.Col(html.Div(html.H4(['Alfagift ', html.B('Sales')])), md=4),
                              dbc.Col(
                                      dcc.DatePickerRange(
                                          id='all_sales_daterange',
                                          min_date_allowed=dt(2020, 1, 1),
                                          max_date_allowed=dt(2022, 12, 1),
                                          start_date_placeholder_text="Start Date",
                                          end_date_placeholder_text="End Date",
                                          display_format='DD-MM-Y',
                                          start_date=start_picker,
                                          end_date=dt(2021,12,31)
                                      )
                              , md=4),
                              dbc.Col(
                                dcc.Dropdown(
                                    id='demo-dropdown',
                                    options=[
                                        {'label': 'Monthly', 'value': 'Monthly'},
                                        {'label': 'Daily', 'value': 'Daily'}
                                    ],
                                    value='Daily'
                                )
                              , md=4),
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
                        dbc.CardFooter([
                          dbc.Card(
                            dbc.CardBody(
                                dbc.Row([
                                    dbc.Col(html.H5([html.B('actual'), ' sales', html.Br(), 'cumulative']), width=3),
                                    dbc.Col(
                                            dcc.DatePickerRange(
                                                id='actual_sales_daterange',
                                                min_date_allowed=dt(2020, 1, 1),
                                                max_date_allowed=dt(2022, 12, 1),
                                                start_date_placeholder_text="Start Date",
                                                end_date_placeholder_text="End Date",
                                                display_format='DD-MM-Y',
                                                start_date=start_picker,
                                                end_date=end_picker
                                            )
                                    , width=5),
                                    dbc.Col(html.H3(html.Div(id='actual_sales_child')), width=4),
   
                                ], justify="start",),

                            )
                          ),
                          dbc.Card(
                            dbc.CardBody(
                                dbc.Row([
                                    dbc.Col(html.H5([html.B('prediction'), ' sales', html.Br(), 'cumulative']), width=3),
                                    dbc.Col(
                                            dcc.DatePickerRange(
                                                id='prediction_sales_daterange',
                                                min_date_allowed=dt(2020, 1, 1),
                                                max_date_allowed=dt(2022, 12, 1),
                                                start_date_placeholder_text="Start Date",
                                                end_date_placeholder_text="End Date",
                                                display_format='DD-MM-Y',
                                                start_date=start_picker,
                                                end_date=end_picker
                                            )
                                    , width=5), 
                                    dbc.Col(html.H3(html.Div(id='prediction_sales_child')), width=4),
                                    # dbc.Col(html.H3("hehehe"), width=4),
  
                                ], justify="start",),
                            )
                          ),

                        
                        ]),
                    ], style={'height':'124vh'}), md=12),

            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Alfagift promotion sales"),
                      dbc.CardBody(
                          [
                            dbc.Row([
                                dbc.Col(
                                    dbc.FormGroup(
                                        [
                                            dbc.Label("Promo start date", html_for="promo-start-grid"),
                                            dcc.DatePickerSingle(
                                                id='promo_start_date',
                                                min_date_allowed=dt(1995, 8, 5),
                                                max_date_allowed=dt(2017, 9, 19),
                                                initial_visible_month=dt(2017, 8, 5),
                                                date=dt(2017, 8, 25)
                                            ),
                                        ]
                                    ),
                                    width=6,
                                ),
                                dbc.Col(
                                    dbc.FormGroup(
                                        [
                                            dbc.Label("Promo end date", html_for="promo-end-grid"),
                                            dcc.DatePickerSingle(
                                                id='promo_end_date',
                                                min_date_allowed=dt(1995, 8, 5),
                                                max_date_allowed=dt(2017, 9, 19),
                                                initial_visible_month=dt(2017, 8, 5),
                                                date=dt(2017, 8, 25)
                                            ),
                                        ]
                                    ),
                                    width=6,
                                ),
                            ]),
                            dbc.Row([
                                dbc.Col(
                                    dbc.FormGroup(
                                        [
                                            dbc.Label("Whitelist product count", html_for="example-email-grid"),
                                            dbc.Input(
                                                type="number",
                                                id="count_whitelist",
                                                placeholder="Enter email",
                                            ),
                                        ]
                                    ),
                                    width=6,
                                ),
                                dbc.Col(
                                    dbc.FormGroup(
                                        [
                                            dbc.Label("Whitelist product price", html_for="example-password-grid"),
                                            dbc.Input(
                                                type="number",
                                                id="price_whitelist",
                                                placeholder="Enter sum of product price",
                                            ),
                                        ]
                                    ),
                                    width=6,
                                ),
                            ])
                            dbc.Row([
                                dbc.Col(
                                    dbc.FormGroup(
                                        [
                                            dbc.Label("Total discount amount", html_for="example-email-grid"),
                                            dbc.Input(
                                                type="number",
                                                id="sum_discount_amount",
                                                placeholder="Enter sum discount or budget afford",
                                            ),
                                        ]
                                    ),
                                    width=6,
                                ),
                                
                            ])
                          ]),
                  ]), md=12),
            ]),
            # dbc.Row([
            #   dbc.Col(
            #     dbc.Card(
            #       [
            #           dbc.CardHeader("Sales prediction 18mar21 - 28mar21"),
            #           dbc.CardBody(
            #               [
            #                   # html.H5("Card title", className="card-title"),
            #                   html.P(
            #                         dcc.Graph(
            #                           figure=fig_sales_test,
            #                           config=dict(displayModeBar=False),
                       
            #                           ),className="card-text",
            #                   ),
            #               ]),
            #       ]), md=12),
            # ]),
        ])
    ]
)