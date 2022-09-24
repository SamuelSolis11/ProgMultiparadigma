from usuario import usuario
bandera=True 
administrador=usuario("Administrador","123","Administrador","Alumno","CURP","Nuevo Laredo") 
lista=[administrador] 

while bandera==True: 
    i=0 
    k=0 
    aux=0 
    print("  MENU  ") 
    print("1. Registro") 
    print("2. Inicio de sesión") 
    print("3. Salir") 
    opcion=int(input("Seleccione una opción del menu: ")) 
    if opcion==1: 
        usu=input("\nIngresar usuario: ") 
        contr=input("Ingresar contraseña: ") 
        rol ="cliente" 
        nom=input("Ingresar el nombre: ") 
        curp=input("Ingresar CURP: ") 
        
        while i < len(lista): 
            if lista[i].CURP == curp:
                print("No Registrado. El usuario ya existe ") 
                aux=1 
            
            i+=1 
        if aux==0: 
            ciu=input("Ingresar ciudad: ") 
            miUsuario=usuario(usu,contr,rol,nom,curp,ciu) 
            print("Registrado con exito") 
            lista.append(miUsuario) 
            
    elif opcion==2: 
        o=0 
        sesionUsu=input("\nIngresar usuario: ") 
        sesionContr=input("Ingresar contraseña: ") 
        while k < len(lista): 
            if lista[k].Usuario == sesionUsu and lista[k].Contraseña==sesionContr and lista[k].Rol=="cliente": 
                print("\nRol: ",lista[k].Rol,"\nNombre: ",lista[k].Nombre, "\nCURP: ", lista[k].CURP,"\nCiudad: ", lista[k].Ciudad)
                aux=1 
                break 
            if lista[k].Usuario == sesionUsu and lista[k].Contraseña==sesionContr and lista[k].Rol=="Administrador": 
                while o < len(lista): 
                    print("\nUsuario",lista[o].Usuario,"\nContraseña",lista[o].Contraseña,"\nRol: ",lista[o].Rol,"\nNombre: ",lista[o].Nombre, "\nCURP: ", lista[o].CURP,"\nCiudad: ", lista[o].Ciudad) 
                    o+=1 
                aux=1 
            k+=1 
        if aux==0: 
             print("  Datos incorrectos  ") 

    elif opcion==3: 
         bandera=False 

    else: 
        print("La opcion que se ingresó es invalida") 
