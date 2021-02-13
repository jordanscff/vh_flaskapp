from flask import Flask, request, abort

app = Flask(__name__)

#Required for routing
import routes.licence

#Configs for SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.dev_master'

if __name__ == '__main__':
    app.run()
