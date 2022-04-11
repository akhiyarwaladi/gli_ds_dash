import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from config_var import promo_selector

## for load csv file
from loader.agsales_load import get_agsales, get_agsales_promo
sales_plot_general = get_agsales()
# target_member_value = sales_plot_general['fbprophet'][2].iloc[-1,:]['member']
# target_sapa_store_value = sales_plot_general['fbprophet'][2].iloc[-1,:]['sapa']

target_member_value = 70000
target_sapa_store_value = 3000


sales_plot_promo = get_agsales_promo()
# sales_plot_jsm = get_agsales_jsm()

## for daterange picker
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

## define date picker start date and end date
start_picker = dt(2021,1,1)
end_picker = dt.today().date() - relativedelta(days=2)

end_picker_promo = dt(2022,12,31)


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
                                dbc.Col(html.Div(html.H4(['Alfagift ', html.B('Sales')])), md=3),
                                dbc.Col(
                                      dcc.DatePickerRange(
                                          id='all_sales_daterange',
                                          min_date_allowed=dt(2020, 1, 1),
                                          max_date_allowed=dt(2022, 12, 1),
                                          start_date_placeholder_text="Start Date",
                                          end_date_placeholder_text="End Date",
                                          display_format='DD-MM-Y',
                                          start_date=start_picker,
                                          end_date=end_picker_promo
                                      )
                                , md=4),
                                dbc.Col(
                                dcc.Dropdown(
                                    id='group_dropdown',
                                    options=[
                                        {'label': 'Monthly', 'value': 'Monthly'},
                                        {'label': 'Daily', 'value': 'Daily'}
                                    ],
                                    value='Monthly'
                                )
                                , md=2),
                                dbc.Col(                                            
                                    dbc.Select(
                                        id="model_algo_dropdown",
                                        options=[
                                            {"label": "Facebook Prophet", "value": "fbprophet", "disabled": False},
                                            {"label": "N-BEATS", "value": "nbeats", "disabled": False},

                                        ],
                                        value="fbprophet"
                                    )                                   

                                , md=3),
                            ]),
                            dbc.Row([
                                dbc.Col('', md=3),
                                dbc.Col('', md=4),
                                dbc.Col('', md=2),
                                dbc.Col(
                                    dcc.Loading(
                                        id="loading-model",
                                        type="default",
                                        children=html.P(id="loading_model")
                                            
                                        
                                    )

                                , md=3),
                            ]),

                          ]
                        ),
                        dbc.CardBody(
                            [
                                # html.H5("Card title", className="card-title"),
                                dcc.Loading(
                                    id="loading-sales-fig",
                                    type="default",
                                    children=html.P(
                                        dcc.Graph(
                                         
                                            id='sales_fig',
                                            config=dict(displayModeBar=False),

                                        ),
                                        className="card-text",
                                    ),
                                ),
                                dcc.Store(id='sales_fig_store'),
                               

                            ]),
                        dbc.CardFooter([
                          dbc.Card(
                            dbc.CardBody([
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
                                                start_date=start_picker + relativedelta(months=12),
                                                end_date=end_picker 
                                            )
                                    , width=5),
                                    dbc.Col(
                                        dcc.Loading(
                                            id="loading-actual-sales",
                                            type="default",
                                            children=html.H3(html.Div(id='actual_sales_child'))
                                        )
                                        , width=4
                                    ),
   
                                ], justify="start",),
                                html.Br(),
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
                                                start_date=start_picker + relativedelta(months=12),
                                                end_date=end_picker_promo
                                            )
                                    , width=5), 

                                    dbc.Col(
                                        dcc.Loading(
                                            id="loading-prediction-sales",
                                            type="default",
                                            children=html.H3(html.Div(id='prediction_sales_child'))
                                        )
                                        , width=4
                                    ),
                                    # dbc.Col(html.H3("hehehe"), width=4),
  
                                ], justify="start",),
                            ]
                            )
                          ),
                          dbc.Card(
                            dbc.CardBody(
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Target member shopper", html_for="example-email-grid"),
                                                dbc.Input(
                                                    type="number",
                                                    id="target_member",
                                                    placeholder="",
                                                    value=target_member_value,
                                                    plaintext=True,
                                                    debounce = True
                                                ),
                                                dcc.Loading(
                                                    id="loading-member",
                                                    type="default",
                                                    children=html.P(id="target_member_enter"),
                                                ),
                                                
                                            ]
                                        ),
                                        width=2,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Target sapa store", html_for="example-email-grid"),
                                                dbc.Input(
                                                    type="number",
                                                    id="target_sapa_store",
                                                    placeholder="",
                                                    value=target_sapa_store_value,
                                                    plaintext=True,
                                                    debounce = True
                                                ),
                                                dcc.Loading(
                                                    id="loading-sapa",
                                                    type="default",
                                                    children=html.P(id="target_sapa_store_enter"),
                                                ),
                                                
                                            ]
                                        ),
                                        width=2,                                    
                                    ),
                                    # dbc.Col(
                                    #     dcc.Loading(
                                    #         id="loading-1",
                                    #         type="default",
                                            
                                    #     ),
                                    #     width=2, 
                                    # ),

                                ], justify="start",),


                            )
                          ),

                        
                        ]),
                    ]), md=12),

            ]),
            # dbc.Row([
            #     dbc.Col(
            #     dbc.Card([
            #         dbc.CardHeader([
            #             dbc.Row([
            #                 dbc.Col(html.Div(html.H4(['Alfagift ', html.B('Sales Promo')]))
            #                     , md=4),
            #                 dbc.Col(
            #                   dcc.DatePickerRange(
            #                       id='sales_promo_picker',
            #                       min_date_allowed=dt(2020, 1, 1),
            #                       max_date_allowed=dt(2022, 12, 1),
            #                       start_date_placeholder_text="Start Date",
            #                       end_date_placeholder_text="End Date",
            #                       display_format='DD-MM-Y',
            #                       start_date=start_picker,
            #                       end_date=end_picker_promo
            #                   )
            #                 , md=4),
            #                 dbc.Col(
            #                     dcc.Dropdown(
            #                         id='sales_promo_dropdown',
            #                         options=[
            #                             {'label': 'Monthly', 'value': 'Monthly'},
            #                             {'label': 'Daily', 'value': 'Daily'}
            #                         ],
            #                         value='Monthly'
            #                     )
            #                 , md=4),

            #             ]),
            #             dbc.Row([
            #                 dbc.Col(''
            #                     , md=4),
            #                 dbc.Col(
            #                     dcc.Loading(
            #                         id="loading-promo-model",
            #                         type="default",
            #                         children=html.P(id="loading_promo_model")
                                        
                                    
            #                     )

            #                 , md=4),
            #                 dbc.Col(                                            
            #                     dbc.Select(
            #                         id="promo_name",
            #                         options=promo_selector,
            #                         value="INSTORE (harga coret)"
            #                     )                                   

            #                 , md=4),
                            
            #             ])


            #         ]),
            #         dbc.CardBody([
            #             dbc.Row([
            #                 dbc.Col([
            #                     dcc.Loading(
            #                         id="loading-sales-promo",
            #                         type="default",
            #                         children=html.P(
            #                             dcc.Graph(
            #                                 # figure=fig_sales_all,
            #                                 # config=dict(displayModeBar=False),
            #                                 id='sales_promo_fig',
            #                                 config=dict(displayModeBar=False),

            #                             )
            #                         )
            #                     ),
            #                     dcc.Store(id='sales_promo_fig_store'),
            #                 ]
            #                 , width=12
            #                 )

            #             ],style={"margin-bottom": "0px", "margin-top": "10px"}),
            #         ]),
            #         dbc.CardFooter([
            #               dbc.Card(
            #                 dbc.CardBody(
            #                     dbc.Row([
            #                         dbc.Col(
            #                             dbc.FormGroup(
            #                                 [
            #                                     dbc.Label("Target member", html_for="example-email-grid"),
            #                                     dbc.Input(
            #                                         type="number",
            #                                         id="target_member_promo",
            #                                         placeholder="",
            #                                         value=target_member_value,
            #                                         plaintext=True,
            #                                         debounce = True
            #                                     ),
            #                                     dcc.Loading(
            #                                         id="loading-member-promo",
            #                                         type="default",
            #                                         children=html.P(id="target_member_promo_enter"),
            #                                     ),
                                                
            #                                 ]
            #                             ),
            #                             width=2,
            #                         ),
            #                         dbc.Col(
            #                             dbc.FormGroup(
            #                                 [
            #                                     dbc.Label("Target sapa store", html_for="example-email-grid"),
            #                                     dbc.Input(
            #                                         type="number",
            #                                         id="target_sapa_store_promo",
            #                                         placeholder="",
            #                                         value=target_sapa_store_value,
            #                                         plaintext=True,
            #                                         debounce = True
            #                                     ),
            #                                     dcc.Loading(
            #                                         id="loading-sapa-promo",
            #                                         type="default",
            #                                         children=html.P(id="target_sapa_store_promo_enter"),
            #                                     ),
                                                
            #                                 ]
            #                             ),
            #                             width=2,                                    
            #                         ),
            #                         # dbc.Col(
            #                         #     dcc.Loading(
            #                         #         id="loading-1",
            #                         #         type="default",
                                            
            #                         #     ),
            #                         #     width=2, 
            #                         # ),

            #                     ], justify="start",),


            #                 )
            #               ),

            #             # dbc.Row([
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Promo start date", html_for="promo-start-grid", width=5),
            #             #                 dcc.DatePickerSingle(
            #             #                     id='promo_start_date',
            #             #                     min_date_allowed=dt(1995, 8, 5),
            #             #                     max_date_allowed=dt(2022, 9, 19),
            #             #                     initial_visible_month=dt(2021, 8, 24),
            #             #                     display_format='DD-MM-Y',
            #             #                     date=dt(2021, 8, 24)
            #             #                 ),
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Promo end date", html_for="promo-end-grid", width=5),
            #             #                 dcc.DatePickerSingle(
            #             #                     id='promo_end_date',
            #             #                     min_date_allowed=dt(1995, 8, 5),
            #             #                     max_date_allowed=dt(2022, 9, 19),
            #             #                     initial_visible_month=dt(2021, 8, 31),
            #             #                     display_format='DD-MM-Y',
            #             #                     date=dt(2021, 8, 31)
            #             #                 ),
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
            #             # ], style={"margin-bottom": "15px"}),
            #             # dbc.Row([
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Whitelist product count", html_for="example-email-grid"),
            #             #                 dbc.Input(
            #             #                     type="number",
            #             #                     id="count_whitelist",
            #             #                     placeholder="Enter count product in this promo",
            #             #                     value=40
            #             #                 ),
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Whitelist product price", html_for="example-password-grid"),
            #             #                 dbc.Input(
            #             #                     type="number",
            #             #                     id="price_whitelist",
            #             #                     placeholder="Enter sum of product price in this promo",
            #             #                     value=1200000
            #             #                 ),
            #             #                 html.P(id="price_whitelist_output"),
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
            #             # ], style={"margin-bottom": "15px"}),
            #             # dbc.Row([
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Total discount amount / product", html_for="example-email-grid"),
            #             #                 dbc.Input(
            #             #                     type="number",
            #             #                     id="sum_discount_amount",
            #             #                     placeholder="Enter sum discount given",
            #             #                     value=97000,
            #             #                     plaintext=True
            #             #                 ),
            #             #                 html.P(id="sum_discount_amount_output"),
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
            #             #     dbc.Col(
            #             #         dbc.FormGroup(
            #             #             [
            #             #                 dbc.Label("Promo name", html_for="example-email-grid"),
            #             #                 # dbc.Select(
            #             #                 #     id="promo_name",
            #             #                 #     options=[
            #             #                 #         {"label": "JSM (jumat-sabtu-minggu)", "value": "JSM (jumat-sabtu-minggu)", "disabled": False},
            #             #                 #         {"label": "Gantung (gajian untung)", "value": "gantung", "disabled": False},
            #             #                 #         {"label": "INSTORE", "value": "INSTORE", "disabled": False},
            #             #                 #     ],
            #             #                 #     value="JSM (jumat-sabtu-minggu)"
            #             #                 # ),                                        
            #             #             ]
            #             #         ),
            #             #         width=4,
            #             #     ),
                            
            #             # ], style={"margin-bottom": "15px"}),
            #             # dbc.Row([
            #             #     dbc.Col(
            #             #         [
            #             #             html.H5('Next sales prediction: '),
            #             #             html.H3(html.Div(id='prediction_promo_sales'))
            #             #         ]
            #             #         , width=12
            #             #     ),
            #             # ], style={"margin-bottom": "10px"}),
            #         ]),
                
            #     ]), md=12),
            # ]),





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