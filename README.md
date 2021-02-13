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

Ensure it is in dev mode:
export FLASK_ENV=development

SETUP SQLite:
Go to command line in the project folder.
Activate env.
Type 'python'
Type 'from tables.user import db'
Type 'db.create_all()'
Your db will now be created. You can view by typing in sqlite3.exe db.dev_master.

Run it:
flask run -h localhost -p 8080
