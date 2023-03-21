from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy() #Define the database Object to use to create or add something to database
DB_NAME = "database.db"


#How to initalize Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ioniq'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #SQLALCHEMY Database is stored at this database
    db.init_app(app) #take the database we defined to tell this is app we are going to use

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note 

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #Telling flask how we load a user. 
    
    return app

