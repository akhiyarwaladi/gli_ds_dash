import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
import base64
from loader.user_path_load import get_app_update
from plots.user_path_plot import plot_app_update
from IPython.core.display import HTML
HTML("""
<style>
g.pointtext {display: none;}
</style>
""")

image_filename = '/home/server/gli-data-science/akhiyar/out_plot/path_end_uninstall.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')


df_app_update = get_app_update()

user_path_tab = dac.TabItem(id='content_user_path', 
                              
    children=html.Div([
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("User path (ends with uninstall apk)")),
                      dbc.CardBody(
                          [

                              html.P(
                                    html.Img(src='data:image/png;base64,{}'.format(encoded_image),\
                                      style={'width':'95%'})
                              ),
                              
                          ]),
                  ]) ,md=12),
              ]),
            dbc.Row([
              dbc.Col(
                dbc.Card(
                  [
                      dbc.CardHeader(html.H5("")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_app_update(df_app_update),
                                      config=dict(displayModeBar=False),
                       
                                      ),className="card-text",
                              ),
                          ]),
                  ]) ,md=12),
              ]),
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