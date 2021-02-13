from app import app
from flask import Flask, request, abort
import sys
from utils import check_allowed_keys

@app.route('/licence', methods=['POST'])
def post_licence():
    post_json = request.get_json()
    allowed_keys = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender']
    check_allowed_keys(allowed_keys, post_json)
    return "hello"

@app.route('/licence')
def get_licence():
    print(request.get_json(), flush=True)
    return "hello"
