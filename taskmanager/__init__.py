# the __init__ file allow us to use custom libraries and 
# will start the application as a package
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# to import the env.py we need to do a if statement otherwise if for some reason
# the app does not find it will not try to load and crash the program
if os.path.exists("env.py"):
    import env  # noqa

# creating a instanse of the flask taking the name module as parameter
# then we attach the secret key and db url to this app instanse that was created
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# then we create a db that is an instance of the SQLALchemy with the  flask instance "app"
db = SQLAlchemy(app)

# here we gonna import "routes" from the application folder
from taskmanager import routes  # noqa
