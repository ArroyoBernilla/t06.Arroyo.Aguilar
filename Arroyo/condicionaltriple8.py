import os
#declarar variables
fuerza,diatancia=0.0,0.0
trabajo=0.0

#Input
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])

#Procesing
trabajo=int(fuerza*distancia)

#Ouput
print("La fuerza utilizada es: " , fuerza)
print("la distancia recorrida es: ", distancia)
print("el trabajo realizado es: ", trabajo)

#condicional multiple
#Si el trabajo realizado es mayor a 100, le saldra: Ya ha trabajado lo sufiiciente descanse
#Si el trabajo realizado es mayor a 50 y menor a 90, le saldra, sigua trabajando aun le falta poco
#Si el trabajo realizado es menor a 40 le saldra, Debe esforzarse mas, le falta bastante

if (trabajo > 100):
    print("Ya ha tranajado lo suficiente, descanse")
if (trabajo > 50 and trabajo<90):
    print("Sigua trajando, aun le falta poco")
if (trabajo<40):
    print("Debe esforzarse mas, le falta bastante")

#fin-if
