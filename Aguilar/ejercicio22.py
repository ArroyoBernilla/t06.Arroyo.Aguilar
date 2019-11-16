import os

#declarar variables
distancia,tiempo,velocidad=0.0,0.0,0.0

#INPUT
distancia=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#PROCESSING
velocidad=int(distancia/tiempo)

#OUPUT
print("el auto ha recorrido una distancia de: ", distancia)
print("en un tiempo de: ", tiempo)
print("velocidad: ", velocidad)
print("el chofer tendra que: ")

#condicional multiple
#si el conductor va a una velocidad mayor que 120 multar con un costo de 1200 soles
#si el conductor va a una velocidad menor que 120 dejarlos seguir su ruta
#si el conductor va a una velocidad igual a 120 decirle que conduzca con cuidado
if(velocidad>120):
    print("RECIBIR UNA MULTA DEL 1200 SOLES")

if(velocidad<120):
    print("SIGUIR SU RUTA")

if(velocidad==120):
    print("CONDUCIR CON CUIDADO")

#fin-if
