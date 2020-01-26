from __future__ import print_function

import jwt
import smooch

from pprint import pprint
from flask import Flask
from flask import request
from smooch.rest import ApiException


# Config
KEY_ID = 'act_5e2d2961a471f2000fc19c89'
SECRET = 'cWlyh0diBDlrwne-h5FVMUg-LDqKe1lsR2sFKo1WbzIdipoTb5N_YWxQGU9LDc6kqlfTcVBY9DuUvk1bZ1l6Cg'

token_bytes = jwt.encode(
    {'scope': 'app'}, SECRET, algorithm='HS256', headers={'kid': KEY_ID})
token = token_bytes.decode('utf-8')

smooch.configuration.api_key['Authorization'] = token
smooch.configuration.api_key_prefix['Authorization'] = 'Bearer'
api_instance = smooch.ConversationApi()


# Server http://flask.pocoo.org/docs/0.12/quickstart/
app = Flask(__name__)


# Expose /messages endpoint to capture webhooks
# https://docs.smooch.io/rest/#webhooks-payload
@app.route('/messages', methods=['POST', 'GET'])
def messages():
    req = request.get_json()
    print('webhook PAYLOAD:')
    pprint(req)

    app_id = req.get('app', {}).get('_id')
    app_user_id = req.get('appUser', {}).get('_id')
    # Call REST API to send message https://docs.smooch.io/rest/#post-message
    if req.get('trigger') == 'message:appUser':
        try:
            message_post_body = smooch.MessagePost(
                'appMaker', 'text', text='Live long and prosper')
            api_response = api_instance.post_message(
                app_id, app_user_id, message_post_body)
            print('API RESPONSE:')
            pprint(api_response)
        except ApiException as e:
            print('API ERROR: %s\n' % e)
    return ('', 204)
