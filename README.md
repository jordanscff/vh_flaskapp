# vh_flaskapp

Set up a virtual env:
virtualenv env

Activate env:
source env/Scripts/activate
Windows (.\env\Scripts\activate)

Show flask the route to the main file (Type into cmd line):
export FLASK_APP=app

Ensure it is in dev mode (Type into cmd line):
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

To run Pytest:
Activate env
Run 'Pytest -v'
There are a total of 6 tests.
