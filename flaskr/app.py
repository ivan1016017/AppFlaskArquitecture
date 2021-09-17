from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()

# to use context to avoid reuse of the app code in differnet instances through the app
app_context.push()

db.init_app(app)

# to create all the tables 
db.create_all() 


# test the app

with app.app_context():
    c1 = Cancion(titulo = "PrimeraPrueba", minutos = 2, segundos = 25, interprete = "ivan")
    c2  = Cancion(titulo = "SegundaPrueba", minutos = 3, segundos = 12, interprete = "catalina")
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()

    # to take a query through all the songs
    print(Cancion.query.all())