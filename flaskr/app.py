from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api
from .vistas import VistasCanciones, VistaCancion, VistaLogIn, VistaSignIn, VistaAlbumsUsuario, VistaCancionesAlbum, VistaAlbum

app = create_app('default')
app_context = app.app_context()

# to use context to avoid reuse of the app code in differnet instances through the app
app_context.push()

db.init_app(app)

# to create all the tables 
db.create_all() 


api = Api(app)

api.add_resource(VistasCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')