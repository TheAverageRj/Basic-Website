from . import db
from flask_login import UserMixin #Help log users in
from sqlalchemy.sql import func

class Note(db.Model): #Database model is a blueprint for an object to be stored in a database(all notes look like this, all users look like this etc)
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #Gets current date and time and stores it
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Specifying foreign key means it must pass an id of an existing user (one to many relationship)


class User(db.Model, UserMixin): #define a layout for an object to store in database
    id = db.Column(db.Integer, primary_key=True) #Primary key to differentiate
    email = db.Column(db.String(150), unique=True) #No user can have the same email as another user
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #Tell Flask to add a note ID in this field for each account. Will be able to access all notes created by the user
