import os
#declarar variables
distancia,tiempo,=0.0,0.0
velocidad=0.0

#Input
distancia=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#Procesing
velocidad=int(distancia/tiempo)

#Ouput
print("el auto ha recorrido una distancia de: ", distancia)
print("en un tiempo de: ", tiempo)
print("velocidad: ", velocidad)


#condicional multiple
#Si el conductor va a una velocidad  mayor que 120 multar con un costo de 1200 soles
#Si el conductor va a una velocidad  menor que 120 decirle; sigua manejando
#Si el conductor va a una velocidad  igual a 120 decirle que conduca con cuidado

if (velocidad > 120):
    print("Recibir una multa de 1200 soles")
if (velocidad < 120):
    print("Sigua manejando")
if (velocidad==120):
    print("conducir con cuidado")

#fin-if
