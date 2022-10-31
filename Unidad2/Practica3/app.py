from flask import Flask,render_template,request,redirect,url_for,jsonify
from database import db
from flask_migrate import Migrate
from models import Cancion,Album,Cantante
from forms import CancionForm,AlbumForm
import logging 


#Aplicacion
app=Flask(__name__)

#Configuracion de la base de datos
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB ='db_cancion'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI']= FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

#configurar migracion
migrate=Migrate()
migrate.init_app(app,db)

#form
app.config["SECRET_KEY"]="una llave muy secreta"
# app.secret_key="llave_secreta"

@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error), 404

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    return render_template('index.html')

logging.basicConfig(filename='error.log',level=logging.DEBUG)

#Entidad canción-----------------------------------------------------------------
@app.route('/cancion')
def mostrarCancion():
    canciones=Cancion.query.all()
    return render_template('cancion.html',canciones=canciones)

@app.route('/verCancion/<int:id>')
def verDetalleCancion(id):
    cancion=Cancion.query.get_or_404(id)
    return render_template('detalleCancion.html',cancion=cancion)

@app.route('/agregarCancion', methods=["GET","POST"])
def agregarCancion():
    cancion = Cancion()
    cancionForm=CancionForm(obj=cancion)
    if request.method=="POST":
        if cancionForm.validate_on_submit():
            cancionForm.populate_obj(cancion)
            #insertar a la base de datos
            db.session.add(cancion)
            db.session.commit()
            return redirect(url_for('mostrarCancion'))
    return render_template('agregarCancion.html',forma=cancionForm)


@app.route('/editarCancion/<int:idCancion>',methods=['GET','POST'])
def editarCancion(idCancion):
    cancion=Cancion.query.get_or_404(idCancion)
    cancionForm=CancionForm(obj=cancion)
    if request.method == "POST":
        if cancionForm.validate_on_submit():
            cancionForm.populate_obj(cancion)
            db.session.commit()
            return redirect(url_for('mostrarCanciones'))
    return render_template('editarCancion.html', forma=cancionForm)

@app.route('/eliminarCancion/<int:idCancion>')
def eliminarCancion(idCancion):
    cancion = Cancion.query.get_or_404(idCancion)
    db.session.delete(cancion)
    db.session.commit()
    return redirect(url_for('mostrarCancion'))

#Entidad Album -----------------------------------------------------------------------
@app.route('/Album')
def mostrarAlbum():
    albumes= Album.query.all()
    return render_template('album.html', albumes=albumes)

@app.route('/verAlbum/<int:id>')
def verDetalleAlbum(id):
    album=Album.query.get_or_404(id)
    return render_template('detalleAlbum.html',album=album)

@app.route('/agregarAlbum', methods=["GET","POST"])
def agregarAlbum():
    album= Album()
    albumForm=AlbumForm(obj=album)
    if request.method=="POST":
        if albumForm.validate_on_submit():
            albumForm.populate_obj(album)
            #insertar a la base de datos
            db.session.add(album)
            db.session.commit()
            return redirect(url_for('mostrarAlbum'))
    return render_template('agregarAlbum.html',forma=albumForm)


@app.route('/editarAlbum/<int:idAlbum>',methods=['GET','POST'])
def editarAlbum(idAlbum):
    album=Album.query.get_or_404(idAlbum)
    albumForm=CancionForm(obj=album)
    if request.method == "POST":
        if albumForm.validate_on_submit():
            albumForm.populate_obj(album)
            db.session.commit()
            return redirect(url_for('mostrarAlbum'))
    return render_template('editarAlbum.html', forma=albumForm)

@app.route('/eliminarAlbum/<int:idAlbum>')
def eliminarAlbum(idAlbum):
    album = Album.query.get_or_404(idAlbum)
    db.session.delete(album)
    db.session.commit()
    return redirect(url_for('mostrarAlbum'))

#Entidad con peticiones http---------------------------------------------------------------
@app.route('/cantantes')
def mostrarCantantes():
    cantantes=Cantante.query.all()
    resultado={"nombreCantante":cantantes.nombreCantante,"nombreArtistico":cantantes.nombreArtistico,"aDebut":cantantes.aDebut}
    return jsonify(resultado)

@app.route('/cantante/<int:id>')
def mostrarCantante(id):
    cantante=Cantante.query.get(id)
    resultado={"idCantante":id,"nombreCantante":cantante.nombreCantante,"nombreArtistico":cantante.nombreArtistico,"aDebut":cantante.aDebut}
    return  jsonify(resultado)

@app.route('/agregarCantante', methods=["POST"])
def agregarCantante():
    info= request.get_json()
    nombreCantante=info["nombreCantante"]
    nombreArtistico= info["nombreArtistico"]
    aDebut = info["aDebut"]
    cantante=Cantante(nombreCantante,nombreArtistico,aDebut)
    db.session.add(cantante)
    db.session.commit()
    return f'{nombreCantante} {nombreArtistico} {aDebut}'

@app.route('/editarCantante/<int:idCantante>',methods=['PUT'])
def editarCantante(idCantante):
    cantante= Cantante.query.get(idCantante)
    info= request.get_json()
    cantante.nombreCantante=info["nombreCantante"]
    cantante.nombreArtistico= info["nombreArtistico"]
    cantante.aDebut = info["aDebut"]
    db.session.add(cantante)
    db.session.commit()
    return f'Se editó la informacion del cantante'
    

@app.route('/eliminarCantante/<int:idCantante>', methods=["DELETE"])
def eliminarCantante(idCantante):
    cantante = Cantante.query.get(idCantante)
    db.session.delete(cantante)
    db.session.commit()
    return 'Se ha eliminado correctamente'
    