import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
from example_plots import (plot_store_type_sales, plot_application_type_sales, plot_order_status)
import base64

from IPython.core.display import HTML
HTML("""
<style>
g.pointtext {display: none;}
</style>
""")

image_filename = '/home/server/gli-data-science/akhiyar/out_plot/path_end_uninstall.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')

user_path_tab = dac.TabItem(id='content_user_path', 
                              
    children=html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("User path (ends with uninstall apk)")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              # html.P(
                                    # dcc.Graph(
                                    #   figure=plot_store_type_sales(),
                                    #   config=dict(displayModeBar=False),
                       
                                    #   ),className="card-text",
                                    
                              # ),
                              html.P(
                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image),\
                                      style={'width':'95%'})
                              ),
                          ]),
                  ]) ,md=12),
              ]),
            # dbc.Row([
            #   dbc.Col(
            #     dbc.Card(
            #       [
            #           dbc.CardHeader(html.H5("Alfagift vs WebOrder(Whatsapp) Sales")),
            #           dbc.CardBody(
            #               [
            #                   # html.H5("Card title", className="card-title"),
            #                   html.P(
            #                         dcc.Graph(
            #                           figure=plot_application_type_sales(),
            #                           config=dict(displayModeBar=False),
                       
            #                           ),className="card-text",
            #                   ),
            #               ]),
            #       ]) ,md=12),
            #   ]),
            # dbc.Row([
            #   dbc.Col(
            #     dbc.Card(
            #       [
            #           dbc.CardHeader(html.H5("Alfagift Order Status")),
            #           dbc.CardBody(
            #               [
            #                   # html.H5("Card title", className="card-title"),
            #                   html.P(
            #                         dcc.Graph(
            #                           figure=plot_order_status(),
            #                           config=dict(displayModeBar=False),
                       
            #                           ),className="card-text",
            #                   ),
            #               ]),
            #       ]) ,md=12),
            #   ]),

       ])
)