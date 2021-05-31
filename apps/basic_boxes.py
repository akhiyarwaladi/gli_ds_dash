import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_new_regular, 
plot_sapa_notsapa, plot_plus_minus)
from datetime import datetime as dt

from dateutil.relativedelta import relativedelta
end_picker = dt.today().date().replace(day=1)
start_picker = end_picker - relativedelta(months=7)


basic_boxes_tab = dac.TabItem(id='content_basic_boxes', 
                              
    children=html.Div([
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(
                                dbc.Row([
                                    dbc.Col(html.H5("Existing vs New Member Sales"), width=4),
                                    dbc.Col(
                                            dcc.DatePickerRange(
                                                id='exist_new_picker',
                                                min_date_allowed=dt(2020, 1, 1),
                                                max_date_allowed=dt(2021, 12, 1),
                                                start_date_placeholder_text="Start Date",
                                                end_date_placeholder_text="End Date",
                                                display_format='DD-MM-Y',
                                                start_date=start_picker,
                                                end_date=end_picker
                                            )
                                    , width=4),   
                                ], justify="between",),
                            ),

                            dbc.CardBody([
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      id='exist_new_fig',
                                      config=dict(displayModeBar=False),

                                      ),className="card-text",
                              ),
                            ]),


                        ], color="light", style={'font': {'size': 35, 'family': 'sans-serif'}})),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(
                                dbc.Row([
                                    dbc.Col(html.H5("Increase and Decrease Sales Member"), width=4),
                                    dbc.Col(
                                            dcc.DatePickerRange(
                                                id='increase_decrease_date',
                                                min_date_allowed=dt(2020, 1, 1),
                                                max_date_allowed=dt(2021, 12, 1),
                                                start_date_placeholder_text="Start Date",
                                                end_date_placeholder_text="End Date",
                                                display_format='DD-MM-Y',
                                                start_date=start_picker,
                                                end_date=end_picker
                                            )
                                    , width=4),   
                                ], justify="between",),
                            ),
                            dbc.CardBody([
                                # html.H5("Card title", className="card-title"),
                                html.P(
                                    dcc.Graph(
                                      id='box-graph',
                                      config=dict(displayModeBar=False),

                                      ),className="card-text",
                                ),
                            ]),
                        ], color="light")),

                    ],className="mb-12")
                ], className='column'
    )
)
