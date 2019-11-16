import os

#declarar variables
distancia,tiempo,velocidad=0.0,0.0,0.0
excesiva_velocidad=False

#INPUT
distancia=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#PROCESSING
velocidad=int(distancia/tiempo)

#OUPUT
print("el auto ha recorrido una distancia de: ", distancia)
print("en un tiempo de: ", tiempo)
print("velocidad: ", velocidad)

#VERIFICADOR
excesiva_velocidad=(velocidad>150)

#condicional simple
#si el conductor va a excesiva velocidad multar con un costo de 1200 soles
if(excesiva_velocidad==True):
    print("MULTA, usted tendra que pagar un monto de 1200 soles")

#fin_if
