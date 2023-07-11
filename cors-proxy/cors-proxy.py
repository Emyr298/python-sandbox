import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def pass_request(url):
    res = requests.get(url)
    return res.content

@app.route('/')
def get_route():
    url = request.args.get('url')
    if url is None:
        return 'Bad Request', 400
    content_type = request.args.get('content-type', 'text/plain')
    response = app.make_response(pass_request(url))
    response.mimetype = content_type
    return response