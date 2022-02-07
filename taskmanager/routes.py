from flask import render_template, request, redirect, url_for
from taskmanager import app, db # noqa
from taskmanager.modules import Category, Task



@app.route("/")
def home():
    return render_template("tasks.html") # noqa

# route to open the categories page
@app.route("/categories")
def categories():
    # query for getting all the categories on the database and store
    # in a list called categories
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

# route function to render the all the categires
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # here is the post method
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        # now add and commit the changes on the database
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories'))

    return render_template("add_category.html")