from flask import abort
import sys
import datetime
import random


def check_allowed_keys(allowed_keys, passed_in_json):
    for key, value in passed_in_json.items():
        if key not in allowed_keys:
            abort(400, 'Unknown key sent')

def check_datetime_format(post_json):
    if type(post_json.get('date_of_birth')) == str:
        try:
            post_json['date_of_birth'] = datetime.datetime.strptime(post_json.get('date_of_birth'), "%Y-%m-%d")
        except Exception:
            abort(400, "Date of birth needs to be in isoformat (1996-02-17)")

def check_gender_format(post_json):
    print(post_json.get('gender'), flush=True)
    if post_json.get('gender') is not 'F' and  post_json.get('gender') is not 'M':
        abort(400, "Incorrect gender format. M or F values are accepted.")

def get_licence_number(post_json):
    #Get first 5 digits
    last_name = ''.join((post_json.get('last_name'), '99999'))
    licence_number = last_name[0:5]

    #Get the 6th digit
    year_of_birth = str(post_json['date_of_birth'].year)[2]
    licence_number = ''.join((licence_number, year_of_birth))

    #Get the 7th and 8th digits
    month_of_birth = 100+post_json['date_of_birth'].month
    if post_json['gender'] is 'F':
        month_of_birth += 50
    licence_number = ''.join((licence_number, str(month_of_birth)[1:3]))

    #Get the 9th and 10th digits
    day_of_birth = 100+post_json['date_of_birth'].day
    licence_number = ''.join((licence_number, str(day_of_birth)))

    #Get the 11th digit
    year_of_birth = str(post_json['date_of_birth'].year)[3]
    licence_number = ''.join((licence_number, year_of_birth))

    #Get the 12th and the 13th digit
    first_inital = str(post_json['first_name'])[0]
    middle_name = '9'
    if 'middle_name' in post_json:
        middle_name = str(post_json['middle_name'])[0]
    licence_number = ''.join((licence_number, first_inital, middle_name))

    #Get the 14th digit
    licence_number = ''.join((licence_number, str(random.randint(0, 9))))

    #Get the 15th and 16th digit
    licence_number = ''.join((licence_number, chr(random.randint(65, 90)), chr(random.randint(65, 90)))).upper()

    return licence_number
