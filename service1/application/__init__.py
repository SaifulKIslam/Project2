from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
#app.config['SECRET_KEY'] = "root"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#from application import routes