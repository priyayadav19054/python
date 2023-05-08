from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow CORS for all routes

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}
    return jsonify(data)


@app.route('/api/submit', methods=['POST'])
def submit_data():

    # print("got data")
    data = request.get_json()
    # process the data here
    processed_data = {'name': 'John', 'age': 30, 'city': 'New York'}
    # return the processed data as JSON
    return jsonify({'processed_data': processed_data})


# @app.route('/api/submit', methods=['POST'])
# def submit_data():
#     print("Got Data1")
#     data = request.get_json()
#     print("input data: ")
#     print(data)
#     # do something with the data (e.g. save to a database)
#     return jsonify({'message': 'Data received successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
