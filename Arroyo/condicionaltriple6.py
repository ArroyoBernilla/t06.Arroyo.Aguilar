import os
#declarar variables
peso1,peso2,peso3,peso4=0.0,0.0,0.0,0.0
promedio_de_pesos=0.0

#input
peso1=int(os.sys.argv[1])
peso2=int(os.sys.argv[2])
peso3=int(os.sys.argv[3])
peso4=int(os.sys.argv[4])

#Procesing
promedio_de_pesos=int((peso1+peso2+peso3+peso4)/4)


print("promedio de pesos:", promedio_de_pesos)

#condicional multiple

#Si el pomedio de peso  es igual 100 le saldra: Exceso de calorias
#Si el pomedio de peso  es manor a 70 y menor a 90 le saldra: Usted esta en buenas condiciones
#Si el pomedio de peso  es menor  60  le saldra: Debe consumir mas calorias

if (promedio_de_pesos == 100):
    print("Exceso de calorias")

if (promedio_de_pesos>70 and promedio_de_pesos<90):
    print("Usted esta en buenas condiciones")

if (promedio_de_pesos<60):
    print("Debe consumir mas calorias")

#fin-if
