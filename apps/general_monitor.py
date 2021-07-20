import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_store_type_sales, plot_application_type_sales, plot_order_status)
from IPython.core.display import HTML

## for daterange picker
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

## define date picker start date and end date
start_picker = dt(2021,1,1)
end_picker = dt.today().date() - relativedelta(days=2)



from loader.general_load import get_member_count, get_sapa_count
member_count  = get_member_count()
sapa_count = get_sapa_count()

HTML("""
<style>
g.pointtext {display: none;}
</style>
""")


general_monitor_tab = dac.TabItem(id='content_general_monitor', 
                              
    children=html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5(['SAPA', html.B(html.I('  vs  ')), 'non-SAPA Store Sales'])
                        ,style={'font-size':'36px','font-family':'Verdana'}),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_store_type_sales(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5(['Alfagift', html.B(html.I('  vs  ')), 'WebOrder(Whatsapp) Sales'])
                        ,style={'font-size':'36px','font-family':'Verdana'}),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_application_type_sales(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("Alfagift Order Status")
                        ,style={'font-size':'36px','font-family':'Verdana'}),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_order_status(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(
                        [
                          dbc.Row([
                            dbc.Col(html.Div(html.H4(['Alfagift ', html.B('Member')])), md=4),
                            dbc.Col(
                                    # dcc.DatePickerRange(
                                    #     id='member_count_daterange',
                                    #     min_date_allowed=dt(2020, 1, 1),
                                    #     max_date_allowed=dt(2022, 12, 1),
                                    #     start_date_placeholder_text="Start Date",
                                    #     end_date_placeholder_text="End Date",
                                    #     display_format='DD-MM-Y',
                                    #     start_date=start_picker,
                                    #     end_date=dt(2021,12,31)
                                    # )
                                    ""
                            , md=4),
                            dbc.Col(
                              dcc.Dropdown(
                                  id='member_count_dropdown',
                                  options=[
                                      {'label': 'Monthly', 'value': 'Monthly'},
                                      {'label': 'Daily', 'value': 'Daily'}
                                  ],
                                  value='Monthly'
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
                                      id='member_count_fig'
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),

            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(
                        [
                          dbc.Row([
                            dbc.Col(html.Div(html.H4(['Alfagift ', html.B('SAPA Store')])), md=4),
                            dbc.Col(
                                    # dcc.DatePickerRange(
                                    #     id='member_count_daterange',
                                    #     min_date_allowed=dt(2020, 1, 1),
                                    #     max_date_allowed=dt(2022, 12, 1),
                                    #     start_date_placeholder_text="Start Date",
                                    #     end_date_placeholder_text="End Date",
                                    #     display_format='DD-MM-Y',
                                    #     start_date=start_picker,
                                    #     end_date=dt(2021,12,31)
                                    # )
                                    ""
                            , md=4),
                            dbc.Col(
                              dcc.Dropdown(
                                  id='sapa_count_dropdown',
                                  options=[
                                      {'label': 'Monthly', 'value': 'Monthly'},
                                      {'label': 'Daily', 'value': 'Daily'}
                                  ],
                                  value='Monthly'
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
                                      id='sapa_count_fig'
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),



       ])
)