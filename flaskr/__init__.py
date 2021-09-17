from flask import Flask 

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db' 
    app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
    return app