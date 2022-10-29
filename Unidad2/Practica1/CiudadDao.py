from Persona import Ciudad
from Conexion import Conexion
from logger_base import log
from cursorDelPool import CursorDelPool  

class CiudadDao:
    _SELECCIONAR=   "SELECT * FROM ciudad"
    _INSERTAR =     "INSERT INTO ciudad(idciudad,nombre,habitantes,capital) Values(%s,%s,%s,%s)"
    _ACTUALIZAR=    "UPDATE ciudad SET nombre=%s, habitantes=%s, capital=%s WHERE idciudad=%s"
    _ELIMINAR =     "DELETE FROM ciudad WHERE idciudad=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                ciudades=[]
                for r in registros:
                    ciudad=(Ciudad(r[0],r[1],r[2],r[3]))
                    ciudades.append(ciudad)
                return ciudades
    @classmethod
    def INSERT(cls,ciudad):
        with CursorDelPool() as cursor:
            valores = (ciudad._idciudad,ciudad._nombre,ciudad._habitantes,ciudad._capital)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def UPDATE(cls,ciudad):
        with CursorDelPool() as cursor:
            valores = (ciudad._nombre,ciudad._habitantes,ciudad._capital,ciudad._idciudad)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
        
    @classmethod
    def DELETE(cls,ciudad):
        with CursorDelPool() as cursor:
            valores = (ciudad._idciudad)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
if __name__=="__main__":
    #Mostrar
    ciudades = CiudadDao.seleccionar()
    for c in ciudades:
       log.debug(f"Ciudades insertadas {c}")
    #INSERT
    #Ciudad1 = Ciudad(idciudad="2",nombre="Guadalajara",habitantes=250004,capital="Jalisco")
    #ciudadInsertadas = CiudadDao.INSERT(Ciudad1)
    #log.debug(f"Ciudades insertadas {ciudadInsertadas}")
    #UPDATE
    #Ciudad1 = Ciudad(idciudad="2",nombre='Nayarit',habitantes=1500,capital='NY')
    #ciudadActualizada = CiudadDao.UPDATE(Ciudad1)
    #log.debug(f"Ciudades Actualizadas {ciudadActualizada}")
    #DELETE
    #ciudadEliminada = CiudadDao.DELETE(Ciudad1)
    #log.debug(f"Ciudades Eliminadas {ciudadEliminada}")