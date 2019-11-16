import os
#declarar variables
velocidad,tiempo,=0.0,0.0
aceleracion=0.0

#Input
velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#Procesing
aceleracion=int(velocidad/tiempo)

#Ouput
print("el auto va a una velocidad de:" , velocidad)
print("Tiempo recorrido: ", tiempo)
print("aceleracion: ", aceleracion, "m/s")

#condicional multiple
#Si el conductor va a una aceleracion  mayor que 80 m/s multar con un costo de 500 soles
#Si el conductor va a una aceleracion  menor que 30 decirle; Excelente conductor
#Si el conductor va a una aceleracion  igual a 50 decirle que condusca con cuidado

if (aceleracion > 20):
    print("Recibir una multa de 500 soles")
if (aceleracion < 30):
    print("Excelente conductor")
if (aceleracion==120):
    print("condusca con cuidado")

#fin-if
