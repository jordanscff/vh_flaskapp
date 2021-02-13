from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.dev_master'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    middle_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.Enum('M', 'F'), nullable=False)

@app.route('/licence', methods=['POST'])
def post_licence():
    print(request.get_json(), flush=True)
    return "hello"

@app.route('/licence')
def get_licence():
    print(request.get_json(), flush=True)
    return "hello"

if __name__ == '__main__':
    app.run()
