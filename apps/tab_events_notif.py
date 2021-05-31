import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_general_push, conversion_general_push, click_general_push)
from plots.campaign_report import g_general_push, w_general_push
general_push = plot_general_push()

from data_loader import get_cpn

from datetime import datetime
now_str = datetime.now().date().strftime('%Y-%m')

f_push = get_cpn()
campaign_push = f_push[0]
option_push = f_push[1]

def fill_card_content(header, content):
    card_content = [
        dbc.CardHeader(html.Center(header)),
        dbc.CardBody(
            [
                #html.H5("Card title", className="card-title"),
                html.B(
                    "{} ({}%)".format(content[header],content['%{}'.format(header)]),
                    className="card-title",
                ),
                dbc.ListGroup(
                    [
                        dbc.ListGroupItem("Android: {}".format(content['{}_{}'.format('Android',header)])),
                        dbc.ListGroupItem("IOS: {}".format(content['{}_{}'.format('IOS',header)])),

                    ],
                    flush=True,
                ),
            ],
        ),
    ]
    return card_content

def fill_card(header, content, row):
    card_content = [
        dbc.CardHeader(html.H5(header)),
        dbc.CardBody(
            [
              html.H5("Target {} users, goal conversion ({})".format(row['Targets'], \
                row['Primary Conversion Goal']), className="card-title"),
              html.Br(),
              content
            ]
        ),
    ]
    return card_content

li_row = []

row_top = [
        dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                  dbc.CardHeader(html.H5("General Push Notification Campaign Growth")),
                  dbc.CardBody(
                      [
                          # html.H5("Card title", className="card-title"),
                          html.P(
                                dcc.Graph(
                                  figure=g_general_push(campaign_push),
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                          ),
                      ]),
                ]), md=12),
        ]),
        dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                [
                  
                    dbc.CardHeader(
                      [
                        dbc.Row([
                          dbc.Col(html.Div("Campaign Performance"), md=4),
                          dbc.Col(
                            dcc.Dropdown(
                                id='cpn_dropdown',
                                options=option_push,
                                value=now_str
                            ), md=4),
                        ],justify="between",)
                      ]
                    ),
                  dbc.CardBody(
                      [
                          # html.H5("Card title", className="card-title"),
                          html.P(
                                dcc.Graph(
                                  #figure=w_general_push(campaign_push),
                                  id = 'cpn_fig', 
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                          ),
                      ]),
                ]), md=12),
        ]),
    ]
# li_row.append(row_top)
li_row = li_row + row_top


for idx, row in general_push.iterrows():
    campaign_name = row['Campaign Name'].strip()
    
    row_x = dbc.Row(
        [

            dbc.Col(dbc.Card(fill_card_content('Impressions', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('Clicks', row)\
              , color="dark", outline=True)),
            dbc.Col(dbc.Card(fill_card_content('Conversions', row)\
              , color="dark", outline=True)),

        ],
        className="mb-4",
    )
    row_y = dbc.Row(
        [
            dbc.Col(dbc.Card(fill_card(campaign_name, row_x, row), color="dark", outline=True)),
        ],
        className="mb-12",
    )
    # li_row.append(row_y)



# li_row = li_row[::-1]

cards = html.Div(li_row)
events_tab = dac.TabItem(id='content_tab_events', 
                              
    children=cards

)