from Persona import Domicilio
from Conexion import Conexion
from logger_base import log
from cursorDelPool import CursorDelPool  

class DomicilioDao:
    _SELECCIONAR=   "SELECT * FROM domicilio"
    _INSERTAR =     "INSERT INTO domicilio(iddomicilio,calle,numero,colonia) Values(%s,%s,%s,%s)"
    _ACTUALIZAR=    "UPDATE domicilio SET calle=%s, numero=%s, colonia=%s WHERE iddomicilio=%s"
    _ELIMINAR =     "DELETE FROM domicilio WHERE iddomicilio=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                domicilios=[]
                for r in registros:
                    domicilio=(Domicilio(r[0],r[1],r[2],r[3]))
                    domicilios.append(domicilio)
                return domicilios
    @classmethod
    def INSERT(cls,domicilio):
        with CursorDelPool() as cursor:
            valores = (domicilio._iddomicilio,domicilio._calle,domicilio._numero,domicilio._colonia)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,domicilio):
        with CursorDelPool() as cursor:
            valores = (domicilio._calle,domicilio._numero,domicilio._colonia,domicilio._iddomicilio)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,domicilio):
        with CursorDelPool() as cursor:
            valores = (domicilio._iddomicilio)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
if __name__=="__main__":
    #Mostrar
     domicilios = DomicilioDao.seleccionar()
     for d in domicilios:
       log.debug(f"Domicilios mostrados {d}")
    #INSERT
    #Domicilio1 = Domicilio(iddomicilio="3",calle="Sierra Mexicali",numero=350,colonia="Infonavit")
    #domicilioInsertadas = DomicilioDao.INSERT(Domicilio1)
    #log.debug(f"Ciudades insertadas {domicilioInsertadas}")
    #UPDATE
    #Domicilio1 = Domicilio(iddomicilio="3",calle="Sierra Gonzales",numero=1400,colonia="Buenavusta")
    #domicilioActualizados = DomicilioDao.UPDATE(Domicilio1)
    #log.debug(f"Ciudades actualizadas {domicilioActualizados}")
    #DELETE
    #domicilioEliminadas = DomicilioDao.DELETE(Domicilio1)
    #log.debug(f"Personas Eliminadas {domicilioEliminadas}")