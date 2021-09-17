from flask import Flask 

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_database.db' 
    app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

    # TO ASSES THE SECURITY OF THE KEY
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'

    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app