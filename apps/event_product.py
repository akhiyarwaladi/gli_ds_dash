import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc


from datetime import datetime
now_str = datetime.now().date().strftime('%Y-%m')

from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
end_picker = dt.today().date().replace(day=1)
start_picker = end_picker - relativedelta(months=7)


from data_loader import get_vp, get_sp

## view product
f_vp = get_vp()
vp = f_vp[0]
mean_vp = f_vp[1] 
options_vp = f_vp[2]

## search product
f_sp = get_sp()
sp =f_sp[0]
mean_sp = f_sp[1]
options_sp = f_sp[2]

from loader.product_load import get_product, get_general_event
f_product_group = get_product()
product_group = f_product_group[0]
product_date_dropdown_li = f_product_group[1]

general_event = get_general_event()


view_product_tab = dac.TabItem(id='content_view_product', 
                              
    children=[
        # html.H5('View Product Event'),

        html.Div([

            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(
                      [
                        dbc.Row([
                          dbc.Col(html.H5("General Event"), width=4
                              ,style={'font-size':'36px','font-family':'Verdana'}),
                          dbc.Col(
                                  dcc.DatePickerRange(
                                      id='general_event_picker',
                                      min_date_allowed=dt(2020, 1, 1),
                                      max_date_allowed=dt(2021, 12, 1),
                                      start_date_placeholder_text="Start Date",
                                      end_date_placeholder_text="End Date",
                                      display_format='DD-MM-Y',
                                      start_date=start_picker,
                                      end_date=end_picker
                                  )
                          , width=6),                        ])
                      ]
                    ),
                    dbc.CardBody(
                        [
                            # html.H5("View product (total event)", className="card-title"),
                            html.P(
                                dcc.Graph(
                                  # figure=plot_vp()[0],
                                  id='general_event_fig',
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                            ),
                        ]),
                    #dbc.CardFooter("Mean view product event {}".format(mean_vp)),
              ]), md=12),
            ]),

            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                    dbc.CardHeader(
                      [
                        dbc.Row([
                          dbc.Col(html.H5("View Product"), md=4),
                          dbc.Col(
                            dcc.Dropdown(
                                id='vp_dropdown',
                                options=options_vp,
                                value='All'
                            ), md=8),
                        ])
                      ]
                    ),
                    dbc.CardBody(
                        [
                            # html.H5("View product (total event)", className="card-title"),
                            html.P(
                                dcc.Graph(
                                  # figure=plot_vp()[0],
                                  id='vp_fig',
                                  config=dict(displayModeBar=False),
                   
                                  ),className="card-text",
                            ),
                        ]),
                    dbc.CardFooter("Mean view product event {}".format(mean_vp)),
              ]), md=12),
            ]),

            # dbc.Row([
            #   dbc.Col(
            #     dbc.Card(
            #       [
            #         dbc.CardHeader(
            #           [
            #             dbc.Row([
            #               dbc.Col(html.H5("Search Product"), md=4),
            #               dbc.Col(
            #                 dcc.Dropdown(
            #                     id='sp_dropdown',
            #                     options=options_sp,
            #                     value='All'
            #                 ), md=8),
            #             ])
            #           ]
            #         ),
            #         dbc.CardBody(
            #             [
            #                 # html.H5("Search product (total event)", className="card-title"),
            #                 html.P(
            #                     dcc.Graph(
            #                       # figure=plot_sp()[0],
            #                       id='sp_fig',
            #                       config=dict(displayModeBar=False),
                   
            #                       ),className="card-text",
            #                 ),
            #             ]),
            #         dbc.CardFooter("Mean search product event {}".format(mean_sp)),

            #   ]), md=12),
            # ]),
            # dbc.Row([
            #   dbc.Col(
            #     dbc.Card(
            #       [
            #         dbc.CardHeader(
            #           [
            #             dbc.Row([
            #               dbc.Col(html.H5("Top Product"), md=4),
            #               dbc.Col(
            #                 dcc.Dropdown(
            #                     id='product_date_dropdown',
            #                     options=product_date_dropdown_li,
            #                     value=now_str
            #                 ), md=8),
            #             ])
            #           ]
            #         ),
            #         dbc.CardBody(
            #             [
            #                 html.P(
            #                     dcc.Graph(

            #                       id='product_fig',
            #                       config=dict(displayModeBar=False),
                   
            #                       ),className="card-text",
            #                 ),
            #             ]),                    

            #   ]), md=12),
            # ]),

    ])
])