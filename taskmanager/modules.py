# here is where our modules for the database will be placed
from taskmanager import db

# Note that because this project is using the Flask-SQLALchemy library
# we don't need to import the "Column" for the data base
# the notation "db.Column" and "db.Integer" since that "db" alredy has it

# for the propourse od this project will be created two tables
# using the class base model
class Category(db.Model):
    """ Schema for the Category model """
    # unique id
    id = db.Column(db.Integer, primary_key=True)
    # the line bellow to create the category 
    # will be a string with max 25 caracters, unique, so
    # every time is created a new one and 
    # nullable fasle beause is mandatory
    category_name = db.Column(db.String(25), unique=True, nullable=False)

    # here is how we link the other class database to this one
    # backref means the ref of itself, the cascade to delete all
    # and lazy means that when we query the db for category we link
    # the task also
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        # to represent itself in a form of a string
        return self.category_name




class Task(db.Model):
    """ Schema for the Category model """
    # unique id
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # in the task_description we use ".Text" to refer a longer texts
    task_descripiton = db.Column(db.Text, nullable=False)
    is_urget = db.Column(db.Boolean, default=False, nullable=False)
    # in this case we take only the day but if hours are needed have
    # to use a different data-type
    due_date = db.Column(db.Date, nullable=False)
    # this act as a foreign key related with the Category class
    # ondelete=CASCADE means that once that the category is deleted all the tasks
    # related to that category will also be deleted
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        # to represent itself in a form of a string
        return f'#{self.id} - Task: {self.task_descripiton} | Urgent: {self.is_urgent}'