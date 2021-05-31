import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc


from example_plots import plot_oos_status, plot_oos_count, plot_oos_consecutive_order, plot_oos_time_spend

oos_boxes_tab = dac.TabItem(id='content_oos_boxes', 
                              
    children=html.Div([
            dbc.Row([
              # dbc.Col(
              #   dbc.Card(
              #     [
              #         dbc.CardHeader("OOS position in order status"),
              #         dbc.CardBody(
              #             [
              #                 # html.H5("Card title", className="card-title"),
              #                 html.P(
              #                       dcc.Graph(
              #                         figure=plot_oos_status(),
              #                         config=dict(displayModeBar=False),
                       
              #                         ),className="card-text",
              #                 ),
              #             ]),
              #     ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("Order item attempt and Order item oos")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_oos_count(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("Consecutive order that user do in same item")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_oos_consecutive_order(),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("User time spend on OOS event")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      id='oos-graph',
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ])),

            ],className="mb-12")
        ], className='column'
    )
)
