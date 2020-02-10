import os
import logging
from service.count import do_sizing
from flask_cors import CORS
from flask import Flask, request, send_file, jsonify
from flask_restful import reqparse
from werkzeug.utils import secure_filename
import numpy as np
from numpy import linalg as LA
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'
app.config['JSON_SORT_KEYS'] = False
CORS(app)

# model = None


@app.route('/api/v1/sizing', methods=['POST'])
def do_sizing_api():
    try:
        args = reqparse.RequestParser(). \
            add_argument('Vectors', type=int). \
            add_argument('Dimensions', type=int). \
            add_argument('Data', type=str). \
            add_argument('Index', type=str). \
            add_argument('Single', type=bool). \
            add_argument('Cluster', type=int). \
            parse_args()
        num_of_vectors = args['Vectors']
        dim = args['Dimensions']
        data_type = args['Data']
        index_type = args['Index']
        single_deploy = args['Single']
        num_of_cluster = args['Cluster']

        status = do_sizing(num_of_vectors, dim, data_type, index_type, single_deploy, num_of_cluster)
        return "{}".format(status)
    except Exception as e:
        return "Error with {}".format(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
