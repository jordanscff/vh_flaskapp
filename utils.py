from flask import abort
import sys
import datetime

def check_allowed_keys(allowed_keys, passed_in_json):
    for key, value in passed_in_json.items():
        if key not in allowed_keys:
            abort(400, 'Unknown key sent')

def check_datetime_format(post_json):
    if type(post_json.get('date_of_birth')) == str:
        try:
            post_json['date_of_birth'] = datetime.datetime.strptime(post_json.get('date_of_birth'), "%Y-%m-%dT%H:%M:%S")
            post_json['date_of_birth'] = post_json['date_of_birth'].isoformat()
        except Exception:
            abort(400, "Date of birth needs to be in isoformat (1996-02-17T00:00:00)")

def get_licence_number(post_json):
    #Get first 5 digits
    last_name = ''.join((post_json.get('last_name'), '99999'))
    licence_number = last_name[0:5]
