from datetime import date 

opcion = int(input("1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY \n\nSeleccionar una opción para imprimir la fecha:")) 
fecha= date.today() 
if opcion==1:
    print("La fecha es: " + format(fecha)) 
else: 
    print("La fecha es: " + date.strftime(fecha, '%m-%d-%Y')) 