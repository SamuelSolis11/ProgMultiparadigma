#Practica 4 
reticula = {} 
j = 0 
total = 0 
sem = int(input("Teclee el semestre: ")) 

if sem <= 2: 
    aux = 6 
else: 
    aux = 7 

while j < aux: 
    j = j+1 
    nom = input("Teclee el nombre de la materia " + str(j) + ": ") 
    cre = int(input("Teclee la cantidad creditos: ")) 
    reticula[nom] = cre 
    total = total + cre 

for llave, valor in reticula.items(): 
    print("\nLa materia " + llave + " tiene " + str(valor) + " creditos.") 

print("\nCreditos totales del semestre: " + str(total))  