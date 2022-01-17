import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from config_var import promo_selector



## for daterange picker
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


from loader.promo_simulation_load import get_plu_list, get_promo_feature


f_plu_list = get_plu_list()
plu_list_dropdown = f_plu_list[0]
plu_list_offline_dropdown = f_plu_list[1]
promo_feature, promo_feature_offline, promo_feature_map = get_promo_feature()




promo_simulation_tab = dac.TabItem(id='content_promo_simulation', 
                              
    children=[
        

        html.Div([
           
            dbc.Row([
               dbc.Col(
                
                  dbc.Card(
                    [
                        dbc.CardHeader(
                          [

                            html.H5("Promo Simulation", className="card-title"),
                            
                          ]
                        ),
                        dbc.CardBody(
                            [
                                # html.H5("Card title", className="card-title"),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("start date", html_for="promo-start-grid", width=5),
                                                dcc.DatePickerSingle(
                                                    id='promo_start_date',
                                                    min_date_allowed=dt(1995, 8, 5),
                                                    max_date_allowed=dt(2022, 9, 19),
                                                    initial_visible_month=dt(2021, 12, 1),
                                                    display_format='DD-MM-Y',
                                                    date=dt(2021, 12, 1)
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("end date", html_for="promo-end-grid", width=5),
                                                dcc.DatePickerSingle(
                                                    id='promo_end_date',
                                                    min_date_allowed=dt(1995, 8, 5),
                                                    max_date_allowed=dt(2022, 9, 19),
                                                    initial_visible_month=dt(2021, 12, 31),
                                                    display_format='DD-MM-Y',
                                                    date=dt(2021, 12, 31)
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown_app',
                                            options=[
                                                {"label": "Alfagift", "value": "alfagift", "disabled": False},
                                                {"label": "Offline Store", "value": "offline", "disabled": False},

                                            ],
                                            value=1
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown_plu',
                                            options=plu_list_dropdown,
                                            value=1
                                        ),
                                        width=8,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([

                                    dbc.Col(

                                        dbc.Select(
                                            id="dropdown_promo_type",
                                            options=[
                                                {"label": "201 potongan langsung", "value": "201", "disabled": False},
                                                {"label": "103 gratis product", "value": "103", "disabled": False},
                                                {"label": "801 beli minimum rupiah dapat star", "value": "801", "disabled": False},
                                                {"label": "803 beli minimum kuantitas dapat star", "value": "803", "disabled": False},
                                                {"label": "807 minimum (kuantitas/rupiah) dapat point", "value": "807", "disabled": False},

                                            ],
                                            value="201"
                                        ),
                                        
                                        width=8,
                                    ),



                                ], style={"margin-bottom": "15px"}),
                                html.Hr(),
                                html.Br(),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [

                                                dbc.Label("Minimum beli rupiah (RP)", color='black-50'),
                                                dbc.Input(
                                                    type="number",
                                                    id="input_min_amount",
                                                    placeholder="Enter",
                                                    value=1,
                                                    disabled=True
                                                ),

                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Minimum beli kuantitas (qty)"),
                                                dbc.Input(
                                                    type="number",
                                                    id="input_min_qty",
                                                    placeholder="Enter",
                                                    value=1,
                                                    disabled=False
                                                ),
                                                
                                            ]
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Jumlah Star yang didapat"),
                                                dbc.Input(
                                                    type="number",
                                                    id="input_extra_star",
                                                    placeholder="Enter",
                                                    value=1,
                                                    disabled=True
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Jumlah Point yang didapat"),
                                                dbc.Input(
                                                    type="number",
                                                    id="input_extra_point",
                                                    placeholder="Enter",
                                                    value=1,
                                                    disabled=True
                                                ),
                                                
                                            ]
                                        ),
                                        width=4,
                                    ),
                                ], style={"margin-bottom": "15px"}),
                                dbc.Row([
                                    dbc.Col(
                                        dbc.FormGroup(
                                            [
                                                dbc.Label("Potongan harga (Rp)"),
                                                dbc.Input(
                                                    type="number",
                                                    id="input_discount_amount",
                                                    placeholder="Enter",
                                                    value=1,
                                                    disabled=False
                                                ),
                                            ]
                                        ),
                                        width=4,
                                    ),

                                ], style={"margin-bottom": "15px"}),
                                html.Hr(),
                                html.Br(),
                                dbc.Row([
                                    dbc.Button(
                                        "hitung", id="button_promo_simulation", className="me-2", size="lg", n_clicks=0
                                    ),


                                ], style={"margin-bottom": "15px"}),

                                dbc.Row([
                                    dbc.Col(
                                        [
                                            html.H5('perkiraan sales: '),
                                            dcc.Loading(
                                                id="loading_calculate_sales",
                                                type="default",
                                                children=[
                                                    html.H3(html.Div(id='outval_promo_simulation'))
                                                    
                                                ]
                                                
                                            ),
                                            
                                        ]
                                        , width=6
                                    ),
                                ], style={"margin-bottom": "15px"}),

                                dbc.Row(
                                [

                                    dbc.Col(
                                        dbc.Card([
                                            "Sales akan meningkat dengan menambah: ", 
                                            html.H5(html.Div(id='increase_sales_adder_str'))
                                        ]),

                                    width=6,)

                                ], id='increase_sales_adder', style={'display':'none'}),

                                dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card([
                                            "Sales akan menurun dengan menambah: ", 
                                            html.H5(html.Div(id='decrease_sales_adder_str'))
                                        ]),

                                    width=6,)

                                ], id='decrease_sales_adder', style={'display':'none'})


                            ]),

                    ]), md=12),

            ]),


        ])
    ]
)