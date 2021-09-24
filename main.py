#!/usr/bin/env python

# Imports
from flask import Flask, request, render_template
import re
import json

app = Flask(__name__)

regex_validate_phone = "([0-9]{1,4})-([0-9]*$)"

@app.route('/')
def hello_world():
    return render_template('hello.html')

def validate_phone_format(phone):
    if not re.match(regex_validate_phone, phone):
        return False
    else:
        return True

def get_phone_info(phone):
    info_phone_extract = re.search(regex_validate_phone, phone, re.IGNORECASE)
    country_code = info_phone_extract.group(1)
    local_number = info_phone_extract.group(2)
    with open('./countries_phone.json') as json_file:
        data = json.load(json_file)
        for elem in data:
            if elem['country_code'] == '+' + country_code and len(local_number) == int(elem['local_length']) :
                return elem
    return '{ "error": "Invalid phone number"}', 404

@app.route('/validate/<phone>', methods=['GET'])
def validate(phone=None):
    if request.method == 'GET':
        if validate_phone_format(phone):
            return get_phone_info(phone)
        else:
            return '{ "error": "Invalid phone number"}', 404