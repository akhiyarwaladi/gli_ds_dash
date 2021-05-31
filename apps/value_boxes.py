import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc

from example_plots import (
plot_voucher_refund_c1, plot_voucher_refund_c2, plot_voucher_refund_c3,
plot_voucher_refund_status)



fig_status, status_count = plot_voucher_refund_status()
fig_c1, c1_count =plot_voucher_refund_c1()
fig_c2, c2_count =plot_voucher_refund_c2()
fig_c3, c3_count =plot_voucher_refund_c3()
value_boxes_tab = dac.TabItem(id='content_value_boxes', 
                              
    children=[
        html.H4('Status order'),
        html.Div([
            dac.ValueBox(
            	value = status_count['Sudah di terima oleh customer'],
              subtitle ='Sudah di terima oleh customer',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Autocancel By System'],
              subtitle = 'Autocancel By System',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Dibatalkan oleh customer care'],
              subtitle = 'Dibatalkan oleh customer care',
              color = "info",
              icon = "database"
            ),
            dac.ValueBox(
              value = status_count['Refund'],
              subtitle = 'Refund',
              color = "info",
              icon = "database"
            )
        ], className='row'),
        html.H4('Observation'),
        html.Div([
            dac.InfoBox(
              title = "Success delivered but didn't voucher",
              value = c1_count,
              icon = "bookmark"
            ),
            dac.InfoBox(
              title = "Success delivered but submit refund",
              color = "info",
              value = c2_count,
              icon = "bookmark"
            ),
            dac.InfoBox(
              title = "Get voucher but not success delivered",
              gradient_color = "danger",
              value = c3_count,
              icon = "bookmark"
            )
        ], className='row'),
        html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("Alfagift SKI order status spread"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=fig_status,
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("success order but not get voucher"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_c1,className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("already receive order but submit refund"),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_c2,className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader("get voucher but order not completed "),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    fig_c3,className="card-text",
                              ),
                          ]),
                  ])),

            ],className="mb-12")
        ], className='column')
    ]
)