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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8049, debug=True)