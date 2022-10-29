from logger_base import log
class Persona():
    def __init__(self,idpersona,nombre,edad,email) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._edad = edad
        self._email = email
        pass
    
    def __str__(self) -> str:
        return f"idPersona: {self._idpersona}\nNombre: {self._nombre}\nEmail: {self._email}\nEdad: {self._edad}"


class Ciudad():
    def __init__(self,idciudad,nombre,habitantes,capital) -> None:
        self._idciudad=idciudad
        self._nombre = nombre
        self._habitantes = habitantes
        self._capital = capital
        pass
    
    def __str__(self) -> str:
        return f"idCiudad: {self._idciudad}\nNombre: {self._nombre}\nhabitantes: {self._habitantes}\nCapital: {self._capital}"
    

class Domicilio():
    def __init__(self,iddomicilio,calle,numero,colonia) -> None:
        self._iddomicilio= iddomicilio
        self._calle = calle
        self._numero = numero
        self._colonia = colonia
        pass
    
    def __str__(self) -> str:
        return f"idDomicilio: {self._iddomicilio}\nNombreCalle: {self._calle}\nNumero: {self._numero}\nColonia: {self._colonia}"
