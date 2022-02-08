from flask import render_template, request, redirect, url_for
from taskmanager import app, db # noqa
from taskmanager.modules import Category, Task



@app.route("/")
def home():
    """Display all the task from the database"""
    tasks = list(Task.query.order_by(Task.task_name).all())
    return render_template("tasks.html", tasks=tasks) # noqa


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
    """ Function to add categories"""
    # here is the post method
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        # now add and commit the changes on the database
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('categories'))

    return render_template("add_category.html")


# route for edditing categories
# to pass the category_id from the edit_category we use this(<int:category_id>)
@app.route("/edit_category/<int:category_id>", methods = ["GET", "POST"])
def edit_category(category_id):
    """we also need to pass "category_id" into the function here as well"""
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    """Function to delete a category"""
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

@app.route("/add_task", methods=["GET","POST"])
def add_task():
    """ Adding new tasks to the db """
    # get the list of all the categories that exist on the database
    # since that the user need to select one of those
    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_descripiton=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)

# route for editing tasks
@app.route("/edit_task/<int:task_id>", methods = ["GET", "POST"])
def edit_task(task_id):
    """we also need to pass "category_id" into the function here as well"""
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_descripiton = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent")else False)
        task.due_date = request.form.get("due_date")
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, categories=categories)

@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    """Function to delete a task"""
    task = Task.query.get_or_404(task_id)

    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))