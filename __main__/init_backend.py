from parse import *
from flask import jsonify
import json


def runBackendProcess():
    result = processData()
    #print(json.dumps(result))
    #print(type(json.dumps(result)))
    print(json.dumps(result))
    return json.dumps(result)

#runBackendProcess()
