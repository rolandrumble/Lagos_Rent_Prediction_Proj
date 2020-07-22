import json
import pickle
import numpy as np
from scipy.special import boxcox, inv_boxcox

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, num_bedrooms, num_toilet, num_bathrooms):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = num_bedrooms
    x[1] = num_toilet
    x[2] = num_bathrooms
    if loc_index >= 0:
        x[loc_index] = 1

    return __model.predict([x])[0]


def get_location_names():
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./artifacts/Lagos_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts... done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(inv_boxcox(get_estimated_price('lekki', 3, 3, 3), 0))
    print(inv_boxcox(get_estimated_price('aguda surulere', 3, 3, 3), 0))
