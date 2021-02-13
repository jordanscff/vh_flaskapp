# vh_flaskapp

Set up a virtual env:
virtualenv env

Activate env:
source env/Scripts/activate
Windows (.\env\Scripts\activate)

Install flask:
pip install flask

Install flask-sqlalchemy:
pip install flask flask-sqlalchemy

Show flask the route to the main file:
export FLASK_APP=app

Run it in dev mode:
export FLASK_ENV=development

Run it:
flask run -h localhost -p 8080

