from flask import Flask, jsonify, request

app = Flask(__name__)


def predict_result(img):
    return 1 if model.predict(img)[0][0] > 0.5 else 0


@app.route('/predict', methods=['POST'])
def infer_image():
    # Catch the image file from a POST request

    

    promo_start_date = request.args.get('promo_start_date', None)
    promo_end_date = request.args.get('promo_end_date', None)
    input_min_amount = request.args.get('input_min_amount', None)
    input_min_qty = request.args.get('input_min_qty', None)
    input_extra_star = request.args.get('input_extra_star', None)
    input_extra_point = request.args.get('input_extra_point', None)
    input_discount_amount = request.args.get('input_discount_amount', None)
    input_num_target = request.args.get('input_num_target', None)
    pred_promo_type = request.args.get('pred_promo_type', None)
    pred_plu = request.args.get('pred_plu', None)
    pred_app = request.args.get('pred_app', None)
    # Return on a JSON format

    print(promo_start_date)
    print(promo_end_date)
    print(input_min_amount)

    res = {
    	'sales':1000,
    	'sales_increase_by':['duration']

    }
    return jsonify(res)
    

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8049)