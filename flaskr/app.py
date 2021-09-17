from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

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
    u = Usuario(nombre = 'Ivan', contrasena = "1234")
    a = Album(titulo = "albumPrueba", anio = 2020, descripcion = "Este es el nuevo album", medio = Medio.CD)
    a.canciones.append(c1)
    a.canciones.append(c2)
    u.albumes.append(a)
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
    print(u)

    # to take a query through all the songs
