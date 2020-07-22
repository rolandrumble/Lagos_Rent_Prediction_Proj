from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names/')
def get_location_names():
    response = jsonify({'locations': util.get_location_names()
                        })
    response.headers.add('Access-control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    num_bedrooms = int(request.form.get['number_of_bedrooms'])
    location = request.form.get['location']
    num_bathrooms = int(request.form.get['number_of_bathrooms'])
    num_toilet = int(request.form.get['number_ of_toilet'])
    response = jsonify({'estimated_price': util.get_estimated_price(num_bedrooms, location, num_bathrooms, num_toilet)})
    response.headers.add('Access-control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction>>>>")
    util.load_saved_artifacts()
    app.run()
