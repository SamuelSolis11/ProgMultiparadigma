def suma(**knumeros): 
    suma=0 
    for key, value in knumeros.items(): 
        print(key,value) 
        suma+=value 
        print("El resultado del producto final  es:" , suma) 


#Pueden mandar n parametros 
suma(a=5,b=50,c=40) 