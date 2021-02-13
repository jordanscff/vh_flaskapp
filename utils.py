from flask import abort

def check_allowed_keys(allowed_keys, passed_in_json):
    for key, value in passed_in_json.items():
        if key not in allowed_keys:
            abort(400, 'Unknown key sent')
