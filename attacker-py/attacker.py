from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/redirect')
def get_route():
    url = request.args.get('url', None)
    if url is None:
        url = request.headers.get('url')
    if url is None:
        return 'Invalid url', 400
    
    return redirect(url)

@app.route('/redirect-custom')
def get_route():
    return redirect('http://127.0.0.1:8080/flag/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    