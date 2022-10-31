from app import db
class Cantante(db.Model):
    idCantante=db.Column(db.Integer,primary_key=True)
    nombreCantante=db.Column(db.String(250))
    nombreArtistico=db.Column(db.String(250))
    aDebut=db.Column(db.Integer)

    def __str__(self) -> str:
        return (f'idCantante:{self.idCantante},'
                f'nombreCantante:{self.nombreCantante},'
                f'nombreArtistico:{self.nombreArtistico},'
                f'aDebut:{self.aDebut}'
        )

    # def __init__(self,nombreCantante,nombreArtistico,aDebut):
    #     self.nombreCantante=nombreCantante
    #     self.nombreArtistico=nombreArtistico
    #     self.aDebut=aDebut

class Album(db.Model):
    idAlbum=db.Column(db.Integer,primary_key=True)
    nombreAlbum=db.Column(db.String(250))
    fechaLanzamiento=db.Column(db.String(250))
    numCanciones=db.Column(db.Integer)


class Cancion(db.Model):
    idCancion=db.Column(db.Integer,primary_key=True)
    nombreCancion = db.Column(db.String(250))
    fechaEstreno = db.Column(db.String(250))
    discografica =  db.Column(db.String(250))
    duracion =  db.Column(db.String(250))

    def __str__(self) -> str:
        return (f'idCancion:{self.idCancion},'
                f'nombreCancion:{self.nombreCancion},'
                f'fechaEstreno:{self.fechaEstreno},'
                f'discografica:{self.discografica},'
                f'duracion:{self.duracion}'
        )