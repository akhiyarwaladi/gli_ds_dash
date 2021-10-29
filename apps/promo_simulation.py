import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from config_var import promo_selector



## for daterange picker
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

## define date picker start date and end date
start_picker = dt(2021,1,1)
end_picker = dt.today().date() - relativedelta(days=2)

end_picker_promo = dt(2022,1,1)


promo_simulation_tab = dac.TabItem(id='content_promo_simulation', 
                              
    children=[
        

        html.Div([
           
            dbc.Row([
               dbc.Col(
                
                  dbc.Card(
                    [
                        dbc.CardHeader(
                          [

                            html.H5("Card title", className="card-title"),
                          ]
                        ),
                        dbc.CardBody(
                            [
                                # html.H5("Card title", className="card-title"),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Promo start date", html_for="promo-start-grid", width=5),
                                                dcc.DatePickerSingle(
                                                    id='promo_start_date',
                                                    min_date_allowed=dt(1995, 8, 5),
                                                    max_date_allowed=dt(2022, 9, 19),
                                                    initial_visible_month=dt(2021, 8, 24),
                                                    display_format='DD-MM-Y',
                                                    date=dt(2021, 8, 24)
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Promo end date", html_for="promo-end-grid", width=5),
                                                dcc.DatePickerSingle(
                                                    id='promo_end_date',
                                                    min_date_allowed=dt(1995, 8, 5),
                                                    max_date_allowed=dt(2022, 9, 19),
                                                    initial_visible_month=dt(2021, 8, 31),
                                                    display_format='DD-MM-Y',
                                                    date=dt(2021, 8, 31)
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(

                                        dbc.Select(
                                            id="dropdown-promo-type",
                                            options=[
                                                {"label": "201 (potongan langsung)", "value": "201", "disabled": False},
                                                {"label": "103 (gratis item)", "value": "103", "disabled": False},

                                            ],
                                            value="201"
                                        ),
                                        
                                        width=4,
                                    ),

                                    dbc.Col(

                                        width=4,
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
                                                    placeholder="Enter count product in this promo",
                                                    value=40
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Whitelist product price", html_for="example-password-grid"),
                                                dbc.Input(
                                                    type="number",
                                                    id="price_whitelist",
                                                    placeholder="Enter sum of product price in this promo",
                                                    value=1200000
                                                ),
                                                html.P(id="price_whitelist_output"),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Total discount amount / product", html_for="example-email-grid"),
                                                dbc.Input(
                                                    type="number",
                                                    id="sum_discount_amount",
                                                    placeholder="Enter sum discount given",
                                                    value=97000,
                                                    plaintext=True
                                                ),
                                                html.P(id="sum_discount_amount_output"),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Promo name", html_for="example-email-grid"),
                                                # dbc.Select(
                                                #     id="promo_name",
                                                #     options=[
                                                #         {"label": "JSM (jumat-sabtu-minggu)", "value": "JSM (jumat-sabtu-minggu)", "disabled": False},
                                                #         {"label": "Gantung (gajian untung)", "value": "gantung", "disabled": False},
                                                #         {"label": "INSTORE", "value": "INSTORE", "disabled": False},
                                                #     ],
                                                #     value="JSM (jumat-sabtu-minggu)"
                                                # ),                                        
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H5('Next sales prediction: '),
                                            html.H3(html.Div(id='prediction_promo_sales'))
                                        ]
                                        , width=12
                                    ),
                                ], style={"margin-bottom": "10px"}),

                                dbc.Row([
                                    dbc.Button(
                                        "Show result", id="button-result", className="me-2", size="lg", n_clicks=0
                                    ),


                                ])

                               



                            ]),

                    ]), md=12),

            ]),




        ])
    ]
)