from flask import Flask, request
from flask_cors import CORS

file_string = open('viewletter.js', 'r').read()

app = Flask(__name__)
CORS(app)

@app.route('/static/viewletter.js')
def get_route():
    response = app.make_response(file_string)
    response.mimetype = 'text/javascript'
    return response
