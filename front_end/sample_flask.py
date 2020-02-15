'''
Main Flask Server Starter Codes
'''
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Render Main Page
@app.route('/')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

# Port to receive and process the requests
@app.route("/posts", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = make_test_JSON()
        return data
    else:
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

def make_test_JSON():
    a = {
            'title': "Tartan eat shit",
            'location': "CAUC McConomy",
            'time': "tomorrow at 6"
        }
    b = {
            'title': "Tartan eat suckers",
            'location': "CAUC sucks",
            'time': "tomorrow at 666"
        }
    c = {
            'title': "Lucas is shit",
            'location': "Jesus Fuck",
            'time': "never"
        }
    d = {
            'a': a,
            'b': b,
            'c': c
        }
    e = jsonify(d)
    return e

if __name__ == '__main__':
    # The host has to be public 0.0.0.0 for broadcasting
    app.run(host='0.0.0.0')
