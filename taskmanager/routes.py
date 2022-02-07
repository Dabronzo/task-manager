from flask import render_template
from taskmanager import app, db # noqa
from taskmanager.modules import Category, Task



@app.route("/")
def home():
    return render_template("tasks.html") # noqa

