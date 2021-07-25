import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac
import dash_bootstrap_components as dbc
import base64
from loader.user_path_load import get_app_update, get_device_uninstall, get_notification_received, get_df_3gram
from plots.user_path_plot import (plot_app_update, plot_device_uninstall, 
  plot_notification_received, plot_review_gram, plot_uninstall_review)
from IPython.core.display import HTML
HTML("""
<style>
g.pointtext {display: none;}
</style>
""")

image_filename = '/home/server/gli-data-science/akhiyar/out_plot/path_end_uninstall.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('ascii')


df_app_update = get_app_update()
df_device_uninstall = get_device_uninstall()
df_notification_received = get_notification_received()
df_3gram = get_df_3gram()

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
                              html.P(
                                    dcc.Graph(
                                      figure=plot_uninstall_review(),
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
                      dbc.CardHeader(html.H5("")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_device_uninstall(df_device_uninstall),
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
                      dbc.CardHeader(html.H5("")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_notification_received(df_notification_received),
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
                      dbc.CardHeader(html.H5("")),
                      dbc.CardBody(
                          [
                              # html.H5("Card title", className="card-title"),
                              html.P(
                                    dcc.Graph(
                                      figure=plot_review_gram(df_3gram),
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
       ])
)