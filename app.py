import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from flask_restful import Resource, Api
from flask import Flask, jsonify, request


import json
import dash
import time
from dash.dependencies import Input, Output, State


import dash_html_components as html
import dash_core_components as dcc
import dash_admin_components as dac

from dash.exceptions import PreventUpdate

# from apps.cards import cards_tab
from apps.social_cards import social_cards_tab
from apps.tab_cards import tab_cards_tab
from apps.tab_cards import text_1, text_2, text_3
from apps.member_growth import basic_boxes_tab
from apps.general_monitor import general_monitor_tab, member_count, sapa_count
from apps.price_compare import tab_price_compare
from apps.value_boxes import value_boxes_tab
from apps.value_behave import value_behave_tab
from apps.sales import (sales_tab, sales_plot_general, sales_plot_promo)
from apps.oos_boxes import oos_boxes_tab
from apps.tab_events_notif import events_tab, campaign_push
from apps.tab_events_inapp import events_inapp, campaign_inapp
from apps.tab_events_email import events_email, campaign_email
from apps.event_product import view_product_tab, product_group, vp, sp, general_event
from apps.user_path_box import user_path_tab, low_review_table

from apps.promo_simulation import (
    promo_simulation_tab, 
    promo_feature, 
    promo_feature_offline,
    promo_feature_map,
    plu_list_dropdown,
    plu_list_offline_dropdown)



from example_plots import (plot_plus_minus, plot_oos_time_spend, plot_new_regular,
                            plot_new_regular_trx)
from plots.campaign_report import w_general_push, w_general_email, w_general_inapp
from plots.product_plot import plot_product

from plots.agsales_plot import plot_sales_all, plot_sales_promo
from plots.agsales_preprocess import (adjust_feature_target,
                                    adjust_promo_feature_target)

from plots.event_product_plot import plot_vp, plot_sp, plot_general_event
from plots.general_plot import plot_member_count, plot_sapa_count
from plots.user_path_plot import plot_low_review


from data_loader import get_vp, get_sp, get_cpn, get_cpe, get_cpi

import pandas as pd
import numpy as np
import requests
import glob



from datetime import date, timedelta, datetime
from dateutil import parser
from helper import transform_to_rupiah_format,transform_format,transform_to_rupiah,rupiah_format



from sqlalchemy import event,create_engine,types


driver = 'cx_oracle'
server = '10.234.152.61' 
database = 'alfabi' 
username = 'report' 
password = 'justd0it'
engine_stmt = "oracle://%s:%s@%s/%s" % ( username, password, server, database )





## importing data in here to enable callback

parent_path = '/home/server/gli-data-science/akhiyar'
new_regular = pd.read_csv(os.path.join(parent_path, \
                'out_plot/new_regular_alfagift_oshop_test.csv'), sep='\t')

from joblib import dump, load
clf = load('/home/server/gli-data-science/akhiyar/sales_prediction/model_stag/LinearRegression_PayDayGantung.joblib') 
normalize = load('/home/server/gli-data-science/akhiyar/sales_prediction/model_stag/normalize_gantung.joblib') 

df_libur = pd.read_csv('/home/server/gli-data-science/akhiyar/out_plot/sales/harilibur.csv')
df_libur['holiday_date'] = pd.to_datetime(df_libur['holiday_date'])

# =============================================================================
# Dash App and Flask Server
# =============================================================================

import dash_bootstrap_components as dbc

FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"



server_flask = Flask('my_app')
app = dash.Dash(__name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME],
    server=server_flask)
app.title = "Data Science Dashboard"
app.config.suppress_callback_exceptions = True
server = app.server 
api = Api(server_flask)

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar

right_ui = dac.NavbarDropdown(
    # badge_label = "!",
    # badge_color= "danger",
    # src = "https://quantee.ai",
    # header_text="2 Items",
    # children= [
    # 	dac.NavbarDropdownItem(
    # 		children = "message 1",
    # 		date = "today"
    # 	),
    # 	dac.NavbarDropdownItem(
    # 		children = "message 2",
    # 		date = "yesterday"
    # 	),
    # ]
)
                              
navbar = dac.Navbar(color="white", 
                    text="select menu on left", 
                    children=right_ui)

# Sidebar
subitems1 = [dac.SidebarMenuSubItem(id='tab_gallery_1', 
                            label='Gallery 1', 
                            icon='arrow-circle-right', 
                            badge_label='Soon',
                            badge_color='success', style={'font-size':'19px'}), 
			dac.SidebarMenuSubItem(id='tab_gallery_2', 
                            label='Gallery 2', 
                            icon='arrow-circle-right', 
                            badge_label='Soon', 
                            badge_color='success', style={'font-size':'19px'})
            ]

# Sidebar
sub_event = [
            dac.SidebarMenuSubItem(id='tab_events', 
                            label='Push Notification', 
                            icon='bell', style={'font-size':'19px'}), 
            dac.SidebarMenuSubItem(id='tab_events_inapp', 
                            label='Mobile in-app (pop-up)', 
                            icon='mobile-alt', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_events_email', 
                            label='Email Campaign', 
                            icon='envelope', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_view_product', 
                            label='General Event', 
                            icon='shopping-bag', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_user_path', 
                            label='Member Review', 
                            icon='wrench', style={'font-size':'19px'})
            ]


sub_monitor = [
            dac.SidebarMenuSubItem(id='tab_general_monitor', label='General Monitor'
                , icon='desktop', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_basic_boxes', label='Member Growth'
                , icon='users', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_price_compare', label='Price Competitor'
                , icon='balance-scale-right', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_oos_boxes', label='Out of stock'
                , icon='layer-group', style={'font-size':'19px'})
]

sub_research = [
            dac.SidebarMenuSubItem(id='tab_value_boxes', label='Voucher Usage'
                , icon='sticky-note', style={'font-size':'19px'}, disabled=True),
            dac.SidebarMenuSubItem(id='tab_value_behave', label='Online-offline trx'
                , icon='shopping-cart', style={'font-size':'19px'}, disabled=True),
            dac.SidebarMenuSubItem(id='tab_sales', label='Sales Prediction'
                , icon='chart-area', style={'font-size':'19px'}),
            dac.SidebarMenuSubItem(id='tab_promo_simulation', label='Promo Simulation'
                , icon='percentage', style={'font-size':'19px'})
]

# icon refer to 
## https://fontawesome.com/v5.15/icons?d=gallery&p=2&q=cart

sidebar = dac.Sidebar(
	dac.SidebarMenu(
		[
			#dac.SidebarHeader(children="Cards"),
			#dac.SidebarMenuItem(id='tab_cards', label='Basic cards', icon='box'),
            #dac.SidebarMenuItem(id='tab_social_cards', label='Social cards', icon='id-card'),
            #dac.SidebarMenuItem(id='tab_tab_cards', label='Tab cards', icon='image'),
			dac.SidebarHeader(children="alfagift insight", 
                style={'font-size':'15px','font-family':'monospace'}),
            dac.SidebarMenuItem(label='Monitoring', icon='chart-line', children=sub_monitor),
            dac.SidebarMenuItem(label='Research', icon='vial', children=sub_research),
            dac.SidebarHeader(children="user behavior", 
                style={'font-size':'15px','font-family':'monospace'}),
            dac.SidebarMenuItem(label='Moengage', icon='handshake', children=sub_event),
            dac.SidebarHeader(children="empty space", 
                style={'font-size':'15px','font-family':'monospace'}),
            dac.SidebarMenuItem(label='...', icon='cubes', children=subitems1),
		]
	),
    style={'font-size':'21px'},
    title='Data Science Dashboard',
	skin="light",
    color="secondary",
	brand_color="secondary",
    url="",
    src="",
    elevation=30,
    opacity=0.7
)

# Body
body = dac.Body(
    dac.TabItems([

        general_monitor_tab,
        basic_boxes_tab,
        tab_price_compare,
        oos_boxes_tab,
        value_boxes_tab,
        value_behave_tab,
        sales_tab,
        promo_simulation_tab,
        events_tab,
        events_inapp,
        events_email,
        view_product_tab,
        user_path_tab,
        dac.TabItem(html.P('Gallery 1 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_1'),
        dac.TabItem(html.P('Gallery 2 (You can add Dash Bootstrap Components!)'), 
                    id='content_gallery_2'),
    ])
)

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Slide to change graph in Basic Boxes"),
        dcc.Slider(
            id='controlbar-slider',
            min=10,
            max=50,
            step=1,
            value=20
        )
    ],
    title = "My right sidebar",
    skin = "light"
)

# Footer
footer = dac.Footer(
	html.A("@Global Loyalty Indonesia",
		href = "", 
		target = "_blank", 
	),
	right_text = "2021"
)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([dcc.Location(id='url', refresh=False), navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Callbacks
# =============================================================================
def activate(input_id, 
             n_general_monitor, n_basic_boxes, n_price_compare, n_oos_boxes, n_value_boxes, n_value_behave,
             n_sales, n_promo_simulation, n_events, n_events_inapp, n_events_email, n_view_product, n_user_path, n_gallery_1, 
             n_gallery_2):
    
    # Depending on tab which triggered a callback, show/hide contents of app
    if input_id == 'tab_general_monitor' and n_general_monitor:
        return True, False, False, False, False, False, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_basic_boxes' and n_basic_boxes:
        return False, True, False, False, False, False, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_price_compare' and n_price_compare:
        return False, False, True, False, False, False, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_oos_boxes' and n_oos_boxes:
        return False, False, False, True, False, False, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_value_boxes' and n_value_boxes:
        return False, False, False, False, True, False, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_value_behave' and n_value_behave:
        return False, False, False, False, False, True, False, False, False, False, False, False, False, False, False
    elif input_id == 'tab_sales' and n_sales:
        return False, False, False, False, False, False, True, False, False, False, False, False, False, False, False
    elif input_id == 'tab_promo_simulation' and n_promo_simulation:
        return False, False, False, False, False, False, False, True, False, False, False, False, False, False, False
    elif input_id == 'tab_events' and n_events:
        return False, False, False, False, False, False, False, False, True, False, False, False, False, False, False
    elif input_id == 'tab_events_inapp' and n_events_inapp:
        return False, False, False, False, False, False, False, False, False, True, False, False, False, False, False
    elif input_id == 'tab_events_email' and n_events_email:
        return False, False, False, False, False, False, False, False, False, False, True, False, False, False, False
    elif input_id == 'tab_view_product' and n_view_product:
        return False, False, False, False, False, False, False, False, False, False, False, True, False, False, False
    elif input_id == 'tab_user_path' and n_user_path:
        return False, False, False, False, False, False, False, False, False, False, False, False, True, False, False
    elif input_id == 'tab_gallery_1' and n_gallery_1:
        return False, False, False, False, False, False, False, False, False, False, False, False, False, True, False
    elif input_id == 'tab_gallery_2' and n_gallery_2:
        return False, False, False, False, False, False, False,False, False, False, False, False, False, False, True
    # initialization
    else:
        return True, False, False, False, False, False, False, False, False, False, False, False, False, False, False
    
@app.callback(
        [
            Output('content_general_monitor', 'active'),
            Output('content_basic_boxes', 'active'),
            Output('content_price_compare', 'active'),
            Output('content_oos_boxes', 'active'),
            Output('content_value_boxes', 'active'),
            Output('content_value_behave', 'active'),
            Output('content_sales', 'active'),
            Output('content_promo_simulation', 'active'),
            Output('content_tab_events', 'active'),
            Output('content_inapp_events', 'active'),
            Output('content_email_events', 'active'),
            Output('content_view_product', 'active'),
            Output('content_user_path', 'active'),
            Output('content_gallery_1', 'active'),
            Output('content_gallery_2', 'active')
            
        ],
        [
            Input('tab_general_monitor', 'n_clicks'),
            Input('tab_basic_boxes', 'n_clicks'),
            Input('tab_price_compare', 'n_clicks'),
            Input('tab_oos_boxes', 'n_clicks'),
            Input('tab_value_boxes', 'n_clicks'),
            Input('tab_value_behave', 'n_clicks'),
            Input('tab_sales', 'n_clicks'),
            Input('tab_promo_simulation', 'n_clicks'),
            Input('tab_events', 'n_clicks'),
            Input('tab_events_inapp', 'n_clicks'),
            Input('tab_events_email', 'n_clicks'),
            Input('tab_view_product', 'n_clicks'),
            Input('tab_user_path', 'n_clicks'),
            Input('tab_gallery_1', 'n_clicks'),
            Input('tab_gallery_2', 'n_clicks'),
            Input('url', 'pathname')
            
        ]
)

def display_tab(n_general_monitor, 
    n_basic_boxes, 
    n_price_compare, 
    n_oos_boxes, 
    n_value_boxes, 
    n_value_behave, 
    n_sales, 
    n_promo_simulation, 
    n_events, 
    n_events_inapp, 
    n_events_email, 
    n_view_product, 
    n_user_path, 
    n_gallery_1, 
    n_gallery_2, 
    pathname):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered


    # Get id of input which triggered callback
    if ctx.triggered[0]['prop_id'].split('.')[0] == 'url':
        
        if pathname == '/':
            input_id = 'tab_general_monitor'
            n_general_monitor = True
        elif pathname == "/sales_monitor":
            input_id = 'tab_sales'
            n_sales = True
        elif pathname == "/member_review":
            input_id = 'tab_user_path'
            n_user_path = True
        elif pathname == "/promo_simulation":
            input_id = 'tab_promo_simulation'
            n_promo_simulation = True
        else:
            input_id = 'tab_general_monitor'
            n_general_monitor = True

    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0] 


    return activate(input_id, 
                    n_general_monitor, n_basic_boxes, n_price_compare, n_oos_boxes, n_value_boxes, n_value_behave, 
                    n_sales, n_promo_simulation, n_events, n_events_inapp, n_events_email, n_view_product, n_user_path, n_gallery_1, 
                    n_gallery_2)

@app.callback(
        [
            Output('tab_general_monitor', 'active'),
            Output('tab_basic_boxes', 'active'),
            Output('tab_price_compare', 'active'),
            Output('tab_oos_boxes', 'active'),
            Output('tab_value_boxes', 'active'),
            Output('tab_value_behave', 'active'),
            Output('tab_sales', 'active'),
            Output('tab_promo_simulation', 'active'),
            Output('tab_events','active'),
            Output('tab_events_inapp', 'active'),
            Output('tab_events_email', 'active'),
            Output('tab_view_product', 'active'),
            Output('tab_user_path', 'active'),
            Output('tab_gallery_1', 'active'),
            Output('tab_gallery_2', 'active')
            
        ],
        [
            Input('tab_general_monitor', 'n_clicks'),
            Input('tab_basic_boxes', 'n_clicks'),
            Input('tab_price_compare', 'n_clicks'),
            Input('tab_oos_boxes', 'n_clicks'),
            Input('tab_value_boxes', 'n_clicks'),
            Input('tab_value_behave', 'n_clicks'),
            Input('tab_sales', 'n_clicks'),
            Input('tab_promo_simulation', 'n_clicks'),
            Input('tab_events', 'n_clicks'),
            Input('tab_events_inapp', 'n_clicks'),
            Input('tab_events_email', 'n_clicks'),
            Input('tab_view_product', 'n_clicks'),
            Input('tab_user_path', 'n_clicks'),
            Input('tab_gallery_1', 'n_clicks'),
            Input('tab_gallery_2', 'n_clicks'),
            Input('url', 'pathname')
        ]
)

def activate_tab(n_general_monitor, 
    n_basic_boxes, 
    n_price_compare, 
    n_oos_boxes, 
    n_value_boxes, 
    n_value_behave, 
    n_sales, 
    n_promo_simulation, 
    n_events, 
    n_events_inapp, 
    n_events_email, 
    n_view_product, 
    n_user_path, 
    n_gallery_1, 
    n_gallery_2, 
    pathname):
    
    ctx = dash.callback_context # Callback context to recognize which input has been triggered

    # Get id of input which triggered callback
    if ctx.triggered[0]['prop_id'].split('.')[0] == 'url':
        
        if pathname == '/':
            input_id = 'tab_general_monitor'
            n_general_monitor = True
        elif pathname == "/sales_monitor":
            input_id = 'tab_sales'
            n_sales = True
        elif pathname == "/member_review":
            input_id = 'tab_user_path'
            n_user_path = True
        elif pathname == "/promo_simulation":
            input_id = 'tab_promo_simulation'
            n_promo_simulation = True
        else:
            input_id = 'tab_general_monitor'
            n_general_monitor = True

    else:
        input_id = ctx.triggered[0]['prop_id'].split('.')[0] 


    return activate(input_id, 
                    n_general_monitor, n_basic_boxes, n_price_compare, n_oos_boxes, n_value_boxes, n_value_behave, 
                    n_sales, n_promo_simulation, n_events, n_events_inapp, n_events_email, n_view_product, n_user_path, n_gallery_1, 
                    n_gallery_2)



# Update figure on slider change
@app.callback(
    Output('box-graph', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_box_graph(value):
    return plot_plus_minus()
    

# Update figure on slider change
@app.callback(
    Output('oos-graph', 'figure'),
    [Input('controlbar-slider', 'value')])
def update_oos_graph(value):
    return plot_oos_time_spend()
    

@app.callback(
    Output('exist_new_fig', 'figure'),
    [
        Input('exist_new_picker', 'start_date'),
        Input('exist_new_picker', 'end_date'),
    ]
)
def make_plot_callback(date_start, date_end):
    
    fig = plot_new_regular(new_regular, date_start, date_end)
    return fig


@app.callback(
    Output('exist_new_trx_fig', 'figure'),
    [
        Input('exist_new_trx_picker', 'start_date'),
        Input('exist_new_trx_picker', 'end_date'),
    ]
)
def make_plot_callback(date_start, date_end):
    
    fig = plot_new_regular_trx(new_regular, date_start, date_end)
    return fig


@app.callback(
    Output('general_event_fig', 'figure'),
    [
        Input('general_event_picker', 'start_date'),
        Input('general_event_picker', 'end_date'),


    ]

)
def make_plot_callback(date_start, date_end):
    fig = plot_general_event(general_event, date_start, date_end)
    return fig


@app.callback(
    Output('vp_fig', 'figure'),
    [
        Input('vp_dropdown', 'value')
    ]
)
def update_plot_vp(value):
    fig = plot_vp(vp, value)

    return fig


@app.callback(
    Output('sp_fig', 'figure'),
    [
        Input('sp_dropdown', 'value')
    ]
)
def update_plot_sp(value):
    fig = plot_sp(sp, value)

    return fig

@app.callback(
    Output('cpn_fig', 'figure'),
    [
        Input('cpn_dropdown', 'value')
    ]
)
def update_plot_cpn(value):
    fig = w_general_push(campaign_push, value)

    return fig

@app.callback(
    Output('cpe_fig', 'figure'),
    [
        Input('cpe_dropdown', 'value')
    ]
)
def update_plot_cpe(value):
    fig = w_general_email(campaign_email, value)

    return fig
    
@app.callback(
    Output('cpi_fig', 'figure'),
    [
        Input('cpi_dropdown', 'value')
    ]
)
def update_plot_cpi(value):
    fig = w_general_inapp(campaign_inapp, value)

    return fig

@app.callback(
    Output('product_fig', 'figure'),
    [
        Input('product_date_dropdown', 'value')
    ]
)
def update_plot_product(value):
    value_2 = 'TRO_NET'
    fig = plot_product(product_group, value, value_2)

    return fig

@app.callback(
    Output('low_review_table', 'children'),
    [
        Input('low_review_dropdown', 'value')
    ]
)
def update_plot_low_review(value):

    fig = plot_low_review(low_review_table, value)

    return fig

@app.callback(
    Output('datatable-interactivity-container', "children"),
    Input('datatable-interactivity', "derived_virtual_data"),
    Input('datatable-interactivity', "derived_virtual_selected_rows"))
def update_graphs(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    return '({})'.format(len(rows))

@app.callback(
    Output('datatable_uninstall_review_container', "children"),
    Input('datatable_uninstall_review', "derived_virtual_data"),
    Input('datatable_uninstall_review', "derived_virtual_selected_rows"))
def update_uninstall_review(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    return '({})'.format(len(rows))


@app.callback(
    Output('datatable_low_review_container', "children"),
    Input('datatable_low_review', "derived_virtual_data"),
    Input('datatable_low_review', "derived_virtual_selected_rows"))
def update_low_review(rows, derived_virtual_selected_rows):
    if derived_virtual_selected_rows is None:
        derived_virtual_selected_rows = []
    return '({})'.format(len(rows))



class HelloWorld(Resource):

    def get(self):
        # app_select = 'alfagift'

        # if app_select == 'alfagift':
        #     li_opt = plu_list_dropdown
        # elif app_select == 'offline':
        #     li_opt = plu_list_offline_dropdown
        # elif app_select == 'targeted_voucher':
        #     li_opt = [{'value': 'alfagift', 'label': 'Alfagift'}]
     
        li_opt = update_date_dropdown_plu_func('alfagift')
        return {'hello': li_opt}

    def post(self):
        promo_start_date = request.args.get('promo_start_date', None)
        promo_end_date = request.args.get('promo_end_date', None)
        input_min_amount = request.args.get('input_min_amount', None)
        input_min_qty = request.args.get('input_min_qty', None)
        input_extra_star = request.args.get('input_extra_star', None)
        input_extra_point = request.args.get('input_extra_point', None)
        input_discount_amount = request.args.get('input_discount_amount', None)
        input_num_target = request.args.get('input_num_target', default=None, type=int)
        input_num_branch = request.args.get('input_num_branch', default=None, type=int)

        pred_promo_type = request.args.get('pred_promo_type', default=None, type=str)
        pred_plu = request.args.get('pred_plu', None)
        pred_app = request.args.get('pred_app', type=str)


        parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
        modul_path = '{}/model/plu_linear_test/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)



        ##### FORM
        pred_df = pd.DataFrame()


        date_object = parser.parse(promo_start_date)
        promo_start_date_str = date_object.strftime('%Y-%m-%d')

        date_object = parser.parse(promo_end_date)
        promo_end_date_str = date_object.strftime('%Y-%m-%d')

        pred_df['tbmproi_start_date'] = [promo_start_date_str]
        pred_df['tbmproi_end_date'] = [promo_end_date_str]

        pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
        pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
        pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
        pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
                                    .astype('timedelta64[D]') + 1).astype(int)


        pred_df['tbmproi_min_purchase_amount'] = [input_min_amount]
        pred_df['tbmproi_min_purchase_qty'] = [input_min_qty]
        pred_df['tbmproi_star'] = [input_extra_star]
        pred_df['tbmproi_extra_point'] = [input_extra_point]
        pred_df['tbmproi_disc_amount'] = [input_discount_amount]
        pred_df['count_branch'] = [input_num_branch]
        pred_df['Non Member'] = 1
        pred_df['SSP Member'] = 1
        pred_df['Regular'] = 1
        pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9

        ### #END FORM
        # if not os.path.exists(modul_path):
        #     engine = create_engine(engine_stmt)
        #     q = '''
        #     SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
        #     FROM(
        #         SELECT 
        #             ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
        #         FROM GLI_REPORT_FAKTUR_SALES_ONLINE
        #         WHERE PLU = {}
        #     )


        #     '''.format(pred_plu)
        #     con = engine.connect()
        #     try:
        #         res_avg = pd.read_sql_query(q,con)
        #     except Exception as e:
        #         if is_debug:
        #             print(e)
        #         pass
        #     con.close()
        #     engine.dispose()
        #     return (
        #         rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
        #         {'display': 'block'}, 
        #         {'display': 'block'},
        #         'duration',
        #         ''
        #     )
        # ####    
        clf = load(modul_path)
        adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

        df_res = pd.concat([pd.DataFrame(promo_feature[pred_promo_type], columns=['variabel']), 
                   pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)
        li_adder_plus = [promo_feature_map[i] for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
        li_adder_min = [promo_feature_map[i] for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

        ####

        pred_val = clf.predict(pred_df[promo_feature[pred_promo_type]])[0]


        time.sleep(1)
        print(pred_val)

        res = {
            'sales':rupiah_format(pred_val, with_prefix=True),
            'sales_increase_by':li_adder_plus

        }
        return jsonify(res)

api.add_resource(HelloWorld, '/hello')



@app.callback(
    [
        Output('sales_promo_fig_store', 'data'),
        Output('target_member_promo_enter', 'children'),
        Output('target_sapa_store_promo_enter', 'children'),
        Output('loading_promo_model', 'children'),
    ],
    [
        Input('promo_name', 'value'),
        Input('target_member_promo', 'value'),
        Input('target_sapa_store_promo', 'value'),
    ]
)
def update_plot_sales(promo_name, target_member, target_sapa_store):
    



    df_forecast = adjust_promo_feature_target(int(target_member), 'trx_member'
        , sales_plot_promo[promo_name][1])
    df_forecast = adjust_promo_feature_target(int(target_sapa_store), 'sapa'
        , df_forecast)

    m = sales_plot_promo[promo_name][2]
    df = sales_plot_promo[promo_name][0]

    #### start predicting
    forecast_train = m.predict(df)
    forecast_future = m.predict(df_forecast)


    train = pd.merge(forecast_train[['ds','yhat','yhat_upper', 'yhat_lower']]
                    , df[['ds','y']],on='ds')
    train = pd.concat([train
                       , forecast_future[['ds','yhat','yhat_upper', 'yhat_lower']]])


    sales_plot = train.rename(columns={'ds':'index','yhat':'TRO_NET_PRED','y':'TRO_NET'})
    sales_plot.iloc[:,1:] = np.where(sales_plot.iloc[:,1:] < 0, 0, sales_plot.iloc[:,1:])
    #### end of prediction



    target_member_enter = "entered: {}".format(rupiah_format(target_member))
    target_sapa_store_enter = "entered: {}".format(rupiah_format(target_sapa_store))


    sales_plot_store = sales_plot.to_json(date_format='iso', orient='split')

    return (sales_plot_store, target_member_enter, 
        target_sapa_store_enter, '')


@app.callback(
    
    Output('sales_promo_fig', 'figure'),
    
    [
        Input('sales_promo_picker', 'start_date'),
        Input('sales_promo_picker', 'end_date'),
        Input('promo_name', 'value'),
        Input('sales_promo_dropdown', 'value'),
        Input('sales_promo_fig_store', 'data'),
    ]
)
def update_fig(date_start, date_end, promo_name, group_dropdown, sales_plot_store):
    sales_plot = pd.read_json(sales_plot_store, orient='split')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    group = group_dropdown

    ## return figure
    fig = plot_sales_promo(sales_plot, date_start, date_end, promo_name, group)
    return fig



@app.callback(
    [
        Output('sales_fig_store', 'data'),
        Output('target_member_enter', 'children'),
        Output('target_sapa_store_enter', 'children'),
        Output('loading_model', 'children'),
    ],
    [
        Input('model_algo_dropdown', 'value'),
        Input('target_member', 'value'),
        Input('target_sapa_store', 'value'),
    ]
)
def update_plot_sales(model_algo, target_member, target_sapa_store):
    
    if model_algo == 'nbeats':
        sales_plot = sales_plot_general[model_algo]

    if model_algo == 'fbprophet':

        df_tto_test = adjust_feature_target(int(target_member), 'trx_member', sales_plot_general['fbprophet'][2])
        df_tto_test = adjust_feature_target(int(target_sapa_store), 'sapa', df_tto_test)

        m = sales_plot_general['fbprophet'][4]
        df = sales_plot_general['fbprophet'][3]
        df_test = df_tto_test.rename(columns={'TRO_DATE_ORDER':'ds','TRO_NET':'y'})
        df_test['ds'] = pd.to_datetime(df_test['ds'])

        forecast_train = m.predict(df.drop(columns="y"))
        train = pd.merge(forecast_train[['ds','yhat','yhat_upper', 'yhat_lower']], df[['ds','y']],on='ds')

        forecast_future = m.predict(df_test)
        train = pd.concat([train, forecast_future[['ds','yhat','yhat_upper', 'yhat_lower']]]).drop_duplicates(subset=['ds'], keep='first')
        

        sales_plot = train.rename(columns={'ds':'index','yhat':'TRO_NET_PRED','y':'TRO_NET'})
        sales_plot.iloc[:,1:] = np.where(sales_plot.iloc[:,1:] < 0, 0, sales_plot.iloc[:,1:])


    target_member_enter = "entered: {}".format(rupiah_format(target_member))
    target_sapa_store_enter = "entered: {}".format(rupiah_format(target_sapa_store))


    sales_plot_store = sales_plot.to_json(date_format='iso', orient='split')

    return (sales_plot_store, target_member_enter, 
        target_sapa_store_enter, '')

@app.callback(
    
    Output('sales_fig', 'figure'),
    
    [
        Input('all_sales_daterange', 'start_date'),
        Input('all_sales_daterange', 'end_date'),
        Input('group_dropdown', 'value'),
        Input('sales_fig_store', 'data'),
    ]
)
def update_fig(date_start, date_end, group_dropdown, sales_plot_store):
    sales_plot = pd.read_json(sales_plot_store, orient='split')
    sales_plot['index'] = pd.to_datetime(sales_plot['index'])
    group = group_dropdown
    fig = plot_sales_all(sales_plot, group, date_start, date_end)
    return fig


@app.callback(
    [
        Output('actual_sales_child', "children"),
        Output('prediction_sales_child', "children"),
    ],
    [
        Input('actual_sales_daterange', 'start_date'),
        Input('actual_sales_daterange', 'end_date'),
        Input('prediction_sales_daterange', 'start_date'),
        Input('prediction_sales_daterange', 'end_date'),
        Input('sales_fig_store', 'data')
    ]
)
def update_actual(date_start, date_end, p_date_start, p_date_end, sales_plot_store):

    date_start = date_start.split('T')[0]
    date_end = date_end.split('T')[0]
    p_date_start = p_date_start.split('T')[0]
    p_date_end = p_date_end.split('T')[0]

    sales_plot = pd.read_json(sales_plot_store, orient='split')
    sales_plot['index'] = pd.to_datetime(sales_plot['index']).dt.strftime('%Y-%m-%d')
    
    print(sales_plot.dtypes)
    print(date_start, date_end)
    print(type(date_start), type(date_end))
    print(p_date_start, p_date_end)
    print(type(p_date_start), type(p_date_end))

    sales_plot_sel = sales_plot[(sales_plot['index'] >= date_start) &
                                (sales_plot['index'] <= date_end) ]

    print(sales_plot_sel.head())
    print(sales_plot_sel.tail())

    p_sales_plot_sel = sales_plot[(sales_plot['index'] >= p_date_start) &
                                (sales_plot['index'] <= p_date_end) ]

    print(p_sales_plot_sel.head())                        
    print(p_sales_plot_sel.tail())

    return ('[ {} ]'.format(transform_to_rupiah(sales_plot_sel['TRO_NET'].sum())),
        '[ {} ]'.format(transform_to_rupiah(p_sales_plot_sel['TRO_NET_PRED'].sum())))


@app.callback(
    Output('member_count_fig', 'figure'),
    [
        Input('member_count_dropdown', 'value'),
    ]
)
def update_plot_member_count(value):
    fig = plot_member_count(member_count, value)

    return fig

@app.callback(
    Output('sapa_count_fig', 'figure'),
    [
        Input('sapa_count_dropdown', 'value'),
    ]
)
def update_plot_sapa_count(value):
    fig = plot_sapa_count(sapa_count, value)

    return fig



@app.callback(
    [
        Output(component_id='input_num_target', component_property='value'),
        Output(component_id='input_min_amount', component_property='disabled'),
        Output(component_id='input_min_qty', component_property='disabled'),
        Output(component_id='input_extra_star', component_property='disabled'),
        Output(component_id='input_extra_point', component_property='disabled'),
        Output(component_id='input_discount_amount', component_property='disabled'),
        Output(component_id='input_num_target', component_property='disabled'),
        Output(component_id='input_min_amount_label', component_property='color'),
        Output(component_id='input_min_qty_label', component_property='color'),
        Output(component_id='input_extra_star_label', component_property='color'),
        Output(component_id='input_extra_point_label', component_property='color'),
        Output(component_id='input_discount_amount_label', component_property='color'),
        Output(component_id='input_num_target_label', component_property='color')
    ],

    [
        Input(component_id='dropdown_promo_type', component_property='value'),
        Input(component_id='dropdown_plu', component_property='value'),
        Input(component_id='dropdown_app', component_property='value')

    ]
)
def show_hide_element(dropdown_promo_type_val, dropdown_plu, dropdown_app):

    def get_num_target(dropdown_plu, dropdown_promo_type_val):
        engine = create_engine(engine_stmt)
        q = '''
            SELECT AVG(NUM_MEMBER) AS AVG_NUM_MEMBER
            FROM GLI_REPORT_FAKTUR_SALES_ONLINE tspa 
            WHERE tspa.PLU = {}
            AND tspa.TYPE = {}

        '''.format(dropdown_plu, dropdown_promo_type_val)
        con = engine.connect()
        try:
            res_avg = pd.read_sql_query(q,con)
        except Exception as e:
            if is_debug:
                print(e)
            pass
        con.close()
        engine.dispose()


        if res_avg['avg_num_member'][0] is not None:
            return int(res_avg['avg_num_member'][0])
        else:
            return 100


    if dropdown_promo_type_val == '201':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, True, False, True, True, False, False, '#C8C9CB', 'black', '#C8C9CB', '#C8C9CB', 'black', 'black'
    elif dropdown_promo_type_val == '103':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, True, False, True, True, True, False, '#C8C9CB', 'black', '#C8C9CB', '#C8C9CB', '#C8C9CB', 'black'
    elif dropdown_promo_type_val == '801':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, False, True, False, True, True, False, 'black', '#C8C9CB', 'black', '#C8C9CB', '#C8C9CB', 'black'
    elif dropdown_promo_type_val == '803':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, True, False, False, True, True, False, '#C8C9CB', 'black', 'black', '#C8C9CB', '#C8C9CB', 'black'
    elif dropdown_promo_type_val == '807':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, False, False, True, False, True, False, 'black', 'black', '#C8C9CB', 'black', '#C8C9CB', 'black'
    elif dropdown_promo_type_val == 'general_voucher':

        val_target = get_num_target(dropdown_plu, dropdown_promo_type_val)

        return val_target, False, True, True, True, False, False, 'black', '#C8C9CB', '#C8C9CB', '#C8C9CB', 'black', 'black'
    else:
        return 100, True, True, True, True, True, True, '#C8C9CB', '#C8C9CB', '#C8C9CB', '#C8C9CB', '#C8C9CB', '#C8C9CB'



@app.callback(
    Output('dropdown_promo_type', 'options'),
    [
        Input('dropdown_app', 'value'),
        Input('dropdown_plu', 'value')
    ]
)
def update_date_dropdown(app_select, plu_select):
    app_select = str(app_select)
    plu_select = str(plu_select)

    if app_select == 'alfagift':
        model_type_map = {"201":"201 potongan langsung",
                  "103":"103 gratis product",
                  "801":"801 beli minimum rupiah dapat star",
                  "803":"803 beli minimum kuantitas dapat star",
                  "807":"807 minimum (kuantitas/rupiah) dapat point"}

        li_opt = []
        li_model = glob.glob('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_linear_test/{}_*'.format(plu_select))
        li_model_type = [model.split('/')[-1].split('.')[0].split('_')[-1] for model in li_model]
        for model_type in model_type_map:
            
        
            if str(model_type) in li_model_type:
                li_opt.append({"label": "{}  -  [ PREDICTED BY MODEL ]".format(model_type_map[model_type]), "value": model_type, "disabled": False})
            else:
                li_opt.append({"label": "{}".format(model_type_map[model_type]), "value": model_type, "disabled": False})
        return li_opt



    elif app_select == 'offline':
        model_type_map = {"201":"201 potongan langsung",
                  "103":"103 gratis product",
                  "801":"801 beli minimum rupiah dapat star",
                  "803":"803 beli minimum kuantitas dapat star",
                  "807":"807 minimum (kuantitas/rupiah) dapat point"}

        li_opt = []
        li_model = glob.glob('/home/server/gli-data-science/akhiyar/sales_prediction/model/plu_linear_offline/{}_*'.format(plu_select))

        for model in li_model:
            print(model)
            model_type = model.split('/')[-1].split('.')[0].split('_')[-1]
            li_opt.append({"label": model_type_map[model_type], "value": model_type, "disabled": False})
        return li_opt

    elif app_select == 'targeted_voucher':
        return [{"label":"General", "value":"general_voucher", "disabled": False}]



def update_date_dropdown_plu_func(app_select):
    app_select = str(app_select)

    if app_select == 'alfagift':
        li_opt = plu_list_dropdown
    elif app_select == 'offline':
        li_opt = plu_list_offline_dropdown
    elif app_select == 'targeted_voucher':
        li_opt = [{'value': 'alfagift', 'label': 'Alfagift'}]

    return li_opt


@app.callback(
    Output('dropdown_plu', 'options'),
    [
        Input('dropdown_app', 'value')
    ]
)
def update_date_dropdown_plu(app_select):


    li_opt = update_date_dropdown_plu_func(app_select)
    return li_opt




@app.callback(
    
    [
        Output(component_id='outval_promo_simulation', component_property='children'),
        Output(component_id='increase_sales_adder', component_property='style'),
        Output(component_id='decrease_sales_adder', component_property='style'),
        Output(component_id='increase_sales_adder_str', component_property='children'),
        Output(component_id='decrease_sales_adder_str', component_property='children')
    ],

    [
        Input(component_id='button_promo_simulation', component_property='n_clicks')
    ],

    [
        State('promo_start_date','date'),
        State('promo_end_date','date'),
        State('input_min_amount', 'value'),
        State('input_min_qty', 'value'),
        State('input_extra_star', 'value'),
        State('input_extra_point', 'value'),
        State('input_discount_amount', 'value'),
        State('input_num_target', 'value'),
        State('input_num_branch', 'value'),
        State('dropdown_promo_type', 'value'),
        State('dropdown_plu', 'value'),
        State('dropdown_app', 'value')
    ]
    
)
def calculate_promo_simulation(
    n_clicks, 
    promo_start_date, 
    promo_end_date, 
    input_min_amount, 
    input_min_qty, 
    input_extra_star, 
    input_extra_point, 
    input_discount_amount, 
    input_num_target,
    input_num_branch,
    pred_promo_type, 
    pred_plu,
    pred_app
    ):
    
    if pred_app == 'alfagift':

        try:
            parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
            modul_path = '{}/model/plu_linear_test/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)

            
            engine = create_engine(engine_stmt)
            q = '''
                SELECT AVG(NUM_MEMBER) AS AVG_NUM_MEMBER
                FROM GLI_REPORT_FAKTUR_SALES_ONLINE tspa 
                WHERE tspa.PLU = {}
                AND tspa.TYPE = {}

            '''.format(pred_plu, pred_promo_type)
            con = engine.connect()
            try:
                res_avg = pd.read_sql_query(q,con)
            except Exception as e:
                if is_debug:
                    print(e)
                pass
            con.close()
            engine.dispose()


            if res_avg['avg_num_member'][0] is not None:
                return int(res_avg['avg_num_member'][0])
            else:
                return 100

            ##### FORM
            pred_df = pd.DataFrame()

            
            date_object = parser.parse(promo_start_date)
            promo_start_date_str = date_object.strftime('%Y-%m-%d')

            date_object = parser.parse(promo_end_date)
            promo_end_date_str = date_object.strftime('%Y-%m-%d')

            pred_df['tbmproi_start_date'] = [promo_start_date_str]
            pred_df['tbmproi_end_date'] = [promo_end_date_str]

            pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
            pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
            pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
            pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
                                        .astype('timedelta64[D]') + 1).astype(int)


            pred_df['tbmproi_min_purchase_amount'] = [input_min_amount]
            pred_df['tbmproi_min_purchase_qty'] = [input_min_qty]
            pred_df['tbmproi_star'] = [input_extra_star]
            pred_df['tbmproi_extra_point'] = [input_extra_point]
            pred_df['tbmproi_disc_amount'] = [input_discount_amount]
            pred_df['count_branch'] = [input_num_branch]
            pred_df['Non Member'] = 1
            pred_df['SSP Member'] = 1
            pred_df['Regular'] = 1
            pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9

            ### #END FORM
            if not os.path.exists(modul_path):
                engine = create_engine(engine_stmt)
                q = '''
                SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
                FROM(
                    SELECT 
                        ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
                    FROM GLI_REPORT_FAKTUR_SALES_ONLINE
                    WHERE PLU = {}
                )


                '''.format(pred_plu)
                con = engine.connect()
                try:
                    res_avg = pd.read_sql_query(q,con)
                except Exception as e:
                    if is_debug:
                        print(e)
                    pass
                con.close()
                engine.dispose()
                return (
                    rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
                    {'display': 'block'}, 
                    {'display': 'block'},
                    'duration',
                    ''
                )
            ####    
            clf = load(modul_path)
            adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

            df_res = pd.concat([pd.DataFrame(promo_feature[pred_promo_type], columns=['variabel']), 
                       pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)
            li_adder_plus = [promo_feature_map[i] for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
            li_adder_min = [promo_feature_map[i] for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

            ####

            pred_val = clf.predict(pred_df[promo_feature[pred_promo_type]])[0]
            pred_val = (input_num_target / num_target_avg) * pred_val
            if pred_val < 0:
                pred_val = 0

            time.sleep(1)
            return (
                rupiah_format(pred_val, with_prefix=True), 
                {'display': 'block'}, 
                {'display': 'block'},
                ', '.join(li_adder_plus),
                ', '.join(li_adder_min)
            )
            
        except Exception as e:
 

            engine = create_engine(engine_stmt)
            q = '''
            SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
            FROM(
                SELECT 
                    ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
                FROM GLI_REPORT_FAKTUR_SALES_ONLINE
                WHERE PLU = {}
            )


            '''.format(pred_plu)
            con = engine.connect()
            try:
                res_avg = pd.read_sql_query(q,con)
            except Exception as e:
                if is_debug:
                    print(e)
                pass
            con.close()
            engine.dispose()
            return (
                rupiah_format(res_avg['avg_daily'][0] * pred_df['duration'][0], with_prefix=True),
                {'display': 'block'}, 
                {'display': 'block'},
                'duration',
                ''
            )

    elif pred_app == 'targeted_voucher':
        try:
            pred_promo_type = 'voucher'
            pred_plu = 'all'

            parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
            modul_path = '{}/model/plu_linear_test/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)




            ##### FORM
            pred_df = pd.DataFrame()


            date_object = parser.parse(promo_start_date)
            promo_start_date_str = date_object.strftime('%Y-%m-%d')

            date_object = parser.parse(promo_end_date)
            promo_end_date_str = date_object.strftime('%Y-%m-%d')

            pred_df['tbmproi_start_date'] = [promo_start_date_str]
            pred_df['tbmproi_end_date'] = [promo_end_date_str]

            pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
            pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
            pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
            pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
                                        .astype('timedelta64[D]') + 1).astype(int)


            pred_df['tbmproi_min_purchase_amount'] = [input_min_amount]
            pred_df['tbmproi_min_purchase_qty'] = [input_min_qty]
            pred_df['tbmproi_star'] = [input_extra_star]
            pred_df['tbmproi_extra_point'] = [input_extra_point]
            pred_df['tbmproi_disc_amount'] = [input_discount_amount]
            pred_df['tbmproi_max_issued_promo'] = [input_num_target]
            pred_df['count_branch'] = 32
            pred_df['Non Member'] = 1
            pred_df['SSP Member'] = 1
            pred_df['Regular'] = 1
            pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9

            ### #END FORM
            if not os.path.exists(modul_path):
                engine = create_engine(engine_stmt)
                q = '''
                SELECT AVG(ACTUAL_DAILY) AS AVG_DAILY
                FROM(
                    SELECT 
                        ACTUAL / ((END_DATE - START_DATE) + 1) AS ACTUAL_DAILY
                    FROM GLI_REPORT_FAKTUR_SALES_ONLINE
                    WHERE PLU = {}
                )


                '''.format(pred_plu)
                con = engine.connect()
                try:
                    res_avg = pd.read_sql_query(q,con)
                except Exception as e:
                    if is_debug:
                        print(e)
                    pass
                con.close()
                engine.dispose()

            ####    
            clf = load(modul_path)
            adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

            df_res = pd.concat([pd.DataFrame(promo_feature[pred_promo_type], columns=['variabel']), 
                       pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)
            li_adder_plus = [promo_feature_map[i] for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
            li_adder_min = [promo_feature_map[i] for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

            ####

            pred_val = clf.predict(pred_df[promo_feature[pred_promo_type]])[0]

            if pred_val < 0:
                pred_val = 0

            time.sleep(1)
            return (
                rupiah_format(pred_val, with_prefix=True), 
                {'display': 'block'}, 
                {'display': 'block'},
                ', '.join(li_adder_plus),
                ', '.join(li_adder_min)
            )


        except Exception as e:
            return (
                str(e),
                {'display': 'block'}, 
                {'display': 'block'},
                '',
                ''
            )     


    elif pred_app == 'offline':
        try:
            parent_path = '/home/server/gli-data-science/akhiyar/sales_prediction'
            modul_path = '{}/model/plu_linear_offline/{}_{}.joblib'.format(parent_path, pred_plu, pred_promo_type)

            clf = load(modul_path)


            adder_blacklist = ['Non Member','SSP Member', 'Regular', 'timestamp']

            df_res = pd.concat([pd.DataFrame(promo_feature_offline[pred_promo_type], columns=['variabel']), 
                       pd.DataFrame(pd.Series(clf.coef_), columns=['bobot'])], 1)

            li_adder_plus = [i for i in list(df_res[df_res['bobot']>0]['variabel']) if i not in adder_blacklist]
            li_adder_min = [i for i in list(df_res[df_res['bobot']<0]['variabel']) if i not in adder_blacklist]

            pred_df = pd.DataFrame()


            date_object = parser.parse(promo_start_date)
            promo_start_date_str = date_object.strftime('%Y-%m-%d')

            date_object = parser.parse(promo_end_date)
            promo_end_date_str = date_object.strftime('%Y-%m-%d')

            pred_df['tbmproi_start_date'] = [promo_start_date_str]
            pred_df['tbmproi_end_date'] = [promo_end_date_str]

            pred_df['tbmproi_start_date'] = pd.to_datetime(pred_df['tbmproi_start_date'])
            pred_df['tbmproi_end_date'] = pd.to_datetime(pred_df['tbmproi_end_date'])
            pred_df['start_week'] = pred_df['tbmproi_start_date'] .apply(lambda d: (d.day-1) // 7 + 1)
            pred_df['duration'] = ((pred_df['tbmproi_end_date'] - pred_df['tbmproi_start_date'])
                                        .astype('timedelta64[D]') + 1).astype(int)

            pred_df['BRANCH'] = [input_num_branch]

            pred_df['MIN_QTY'] = [input_min_qty]
            if pred_promo_type == '807':
                pred_df['POT'] = [input_extra_point]
            elif pred_promo_type == '201':
                pred_df['POT'] = [input_discount_amount]
            pred_df['timestamp'] = pred_df['tbmproi_start_date'].values.astype(np.int64) // 10 ** 9



            pred_val = clf.predict(pred_df[promo_feature_offline[pred_promo_type]])[0]
            if pred_val < 0:
                pred_val = 0

            time.sleep(1)
            return (
                rupiah_format(pred_val, with_prefix=True), 
                {'display': 'block'}, 
                {'display': 'block'},
                ', '.join(li_adder_plus),
                ', '.join(li_adder_min)
            )
            
        except Exception as e:
            return (
                str(e),
                {'display': 'block'}, 
                {'display': 'block'},
                '',
                ''
            )     


# =============================================================================
# Run app    
# =============================================================================
if __name__ == '__main__':
    app.run_server(host= '0.0.0.0', debug=True)
