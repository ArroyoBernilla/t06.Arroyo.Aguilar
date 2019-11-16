import os
#declarar variables
velocidad_angular,radio=0.0,0.0
velocidad_tangencial=0.0

#Input
velocidad_angular=int(os.sys.argv[1])
radio=int(os.sys.argv[2])

#Procesing
velocidad_tangencial=int(velocidad_angular*radio)

#Ouput
print("El radio de la llanta del carro es:" , radio)
print("La velocidad angular de la llanta : ", velocidad_angular)
print("velocidad tangencial de la llanta : ", velocidad_tangencial, "m/s")

#condicional multiple
#Si el conductor va a una velocidad tangencial  mayor a 70, le saldra: excesiva velocidad
#Si el conductor va a una velocidad tangencial mayor a 30 y menor a 60 le saldra: Usted maneja con velocidad normal
#Si el conductor va a una velocidad tangencial  igual a 20 le saldra: usted maneja con precausion

if (velocidad_tangencial > 70):
    print("Excesiva velocidad")
if (velocidad_tangencial > 30 and velocidad_tangencial<60):
    print("Usted maneja con velocidad normal")
if (velocidad_tangencial==20):
    print("Usted maneja con precausion")

#fin-if
