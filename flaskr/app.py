from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema, CancionSchema, UsuarioSchema

app = create_app('default')
app_context = app.app_context()

# to use context to avoid reuse of the app code in differnet instances through the app
app_context.push()

db.init_app(app)

# to create all the tables 
db.create_all() 


# test the app

with app.app_context():
    album_schema = AlbumSchema() # it transform the information from pythn to json format
    cancion_schema = CancionSchema()
    A = Album(titulo = "prueba", anio = 2020, descripcion = "texto", medio = Medio.CD)
    C = Cancion( titulo = "cancionPrueba", minutos = 2, segundos = 1, interprete = "interpretePrueba")
    A.canciones.append(C)
    db.session.add(C)
    db.session.add(A)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()])
    print([cancion_schema.dumps(cancion) for cancion in Cancion.query.all()])



    # to take a query through all the songs
