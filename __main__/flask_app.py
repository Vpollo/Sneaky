'''
Main Flask Server Starter Codes
'''
from init_backend import runBackendProcess
import parse
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
        data = parse.processData() #runBackendProcess()# make_test_JSON()
        #Ensures that data is of JSON Type
        data1 = runBackendProcess()
        data2 = make_test_JSON()
        return data1
    else:
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

def make_test_JSON():
    a = {
            'title': "Math Club Night",
            'location': "CUC McConomy",
            'time': "FEB 18th; 8 PM"
        }
    b = {
            'title': "Robot Club",
            'location': "DH 2315",
            'time': "MAR 2nd; 3 AM"
        }
    c = {
            'title': "University Health Center",
            'location': "POS 103",
            'time': "JULY 7th; 2 AM"
        }
    d = {
            'title': "Engineering Career Fair",
            'location': "The Cut",
            'time': "APR 20th; 6 PM"
    }
    return_data = {
            'a': a,
            'b': b,
            'c': c,
            'd': d
        }
    return jsonify(return_data)

if __name__ == '__main__':
    # The host has to be public 0.0.0.0 for broadcasting
    app.run(host='0.0.0.0')
