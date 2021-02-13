from app import app
from flask import Flask, request, abort, make_response, jsonify
import sys
from utils import check_allowed_keys, get_licence_number, check_datetime_format
import datetime

@app.route('/licence', methods=['POST'])
def post_licence():
    post_json = request.get_json()
    allowed_keys = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender']
    check_allowed_keys(allowed_keys, post_json)
    check_datetime_format(post_json)
    licence_number = get_licence_number(post_json)
    return jsonify(licence_number)

@app.route('/licence')
def get_licence():
    return make_response(jsonify("OK"), 200)
