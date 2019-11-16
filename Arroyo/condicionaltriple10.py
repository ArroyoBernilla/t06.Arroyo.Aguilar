import os
#declarar variables
fuerza,area=0.0,0.0
presion=0.0

#Input
fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])

#Procesing
presion=int(fuerza/area)

#Ouput
print("La fuerza ejercida es: " , fuerza)
print("el area utilizada es: ", area)
print("La presion es: ", presion)

#condicional multiple
#Si la presion es mayor a 120 le saldra, Excelente, sigue asi
#Si la presion es mayor a 90 y menor a 110 le saldra, Ejerce mas fuerza sobre el area
#Si la presion es menor a 40 le saldra; usted no apto para el trabajo

if (presion> 100):
    print("Excelente, sigue asi")

if (presion > 50 and presion<90):
    print("Ejerce mas fuerza sobre el area")

if (presion<40):
    print("usted no apto para el trabajo")

#fin-if
