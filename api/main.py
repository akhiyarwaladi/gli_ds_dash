from flask import Flask, jsonify, request

app = Flask(__name__)


def predict_result(img):
    return 1 if model.predict(img)[0][0] > 0.5 else 0


@app.route('/predict', methods=['POST'])
def infer_image():
    # Catch the image file from a POST request

    discount_amount = request.args.get('discount_amount', None)


    # Return on a JSON format


    res = {
    	'sales':1000
    	'sales_increase_by':['duration']

    }
    return jsonify(res)
    

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)