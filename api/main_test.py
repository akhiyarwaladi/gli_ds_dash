from flask import Flask, jsonify, request
from sqlalchemy import event,create_engine,types

import pandas as pd
import numpy as np
import os
import json
import ast
import time

from joblib import dump, load
from helper import transform_to_rupiah_format,transform_format,transform_to_rupiah,rupiah_format

from dateutil import parser

driver = 'cx_oracle'
server = '10.234.152.61' 
database = 'alfabi' 
username = 'report' 
password = 'justd0it'
engine_stmt = "oracle://%s:%s@%s/%s" % ( username, password, server, database )


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'




@app.route('/coba_input', methods=['POST'])
def infer_image():
    # Catch the image file from a POST request



    andi = request.args.get('andi', None)
    promo_end_date = request.args.get('promo_end_date', None)
    input_min_amount = request.args.get('input_min_amount', None)
    input_min_qty = request.args.get('input_min_qty', None)
    input_extra_star = request.args.get('input_extra_star', None)
    input_extra_point = request.args.get('input_extra_point', None)
    input_discount_amount = request.args.get('input_discount_amount', None)
    input_num_target = request.args.get('input_num_target', default=None, type=int)
    pred_promo_type = request.args.get('pred_promo_type', default=None, type=str)
    pred_plu = request.args.get('pred_plu', None)
    pred_app = request.args.get('pred_app', None)




    res = {
        'input_andi':andi

    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8049, debug=True)