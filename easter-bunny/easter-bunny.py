from flask import Flask, request
from flask_cors import CORS

file_string = open('main.js', 'r').read()

app = Flask(__name__)
CORS(app)

@app.route('/static/main.js')
def get_route():
    response = app.make_response(file_string)
    response.mimetype = 'text/javascript'
    return response
