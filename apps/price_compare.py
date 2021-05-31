import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (plot_df_m_2802, plot_df_m_3101)
from plots.competitive_plot import plot_product_competitive
from datetime import datetime
now_str = datetime.now().date().strftime('%d%b')

fig_, unique_item_ag, change_to_online = plot_df_m_2802()
fig_3101, unique_item_ag_3101, change_to_online_3101 = plot_df_m_3101()

product_competitive = plot_product_competitive()
table_product_competitive = product_competitive[0]
lower_price = product_competitive[1]
higher_price = product_competitive[2]


card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

card1 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(lower_price, className="card-title"),
                    html.P("lower than competitor", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fas fa-angle-double-down", style=card_icon),
            # className="bg-primary",
            color="#3D9970",
            style={"maxWidth": 75, "height":110, 'width': 70},
        ),
    ],
    className="mt-4 shadow",
)

card2 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(higher_price, className="card-title"),
                    html.P("higher than competitor", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fas fa-angle-double-up", style=card_icon),
            # className="bg-info",
            color="#f55c47",
            style={"maxWidth": 75, "height":110, 'width': 70},
        ),
    ],className="mt-4 shadow",
)

card3 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("", className="card-title"),
                    html.P("minimum price", className="card-text",),
                ]
            )
        ),
        dbc.Card(
            html.Div(className="fas fa-dollar-sign", style=card_icon),
            # className="bg-info",
            color="#87a7b3",
            style={"maxWidth": 50, "height":50, 'width': 50},
        ),
    ],className="mt-3 shadow",
)



tab_price_compare = dac.TabItem(id='content_price_compare', 
                              
children=[
  html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(html.Center(html.H4("Product Competitive Price {}".format(now_str)))),
                    dbc.CardBody([
                      dbc.Row([
                        dbc.Col(
                          card1
                        , width = 3),
                        dbc.Col(
                          card2
                        , width = 3),
                      ], justify="center",),
                      dbc.Row([
                        dbc.Col(
                          card3
                        , width = 3),
                      ], justify="center",)
                    ])
                  ]
                ),
              )
            ]),
            dbc.Row([
              dbc.Col(
                dbc.Card([
                  dbc.CardHeader(["showing rows", html.H5(html.Div(id='datatable-interactivity-container'))]),
                  dbc.CardBody([
                      # html.H5("Card title", className="card-title"),
                      html.P(
                            table_product_competitive,className="card-text",
                      ),
                  ]),
                ])
              ),
            ]),
  ])

  
])


