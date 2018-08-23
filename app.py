#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
	res = makeWebhookResult()
	return res
def makeWebhookResult():
    speech ="hot"
    print("Response:")
    print(speech)
    print(json.dumps(slack_message))
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {"slack": slack_message, "facebook": facebook_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='127.0.0.1')
