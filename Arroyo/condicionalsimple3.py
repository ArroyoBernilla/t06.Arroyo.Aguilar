import os
#declarar variables
peso1,peso2,peso3,peso4=0.0,0.0,0.0,0.0
promedio=False

#input
peso1=int(os.sys.argv[1])
peso2=int(os.sys.argv[2])
peso3=int(os.sys.argv[3])
peso4=int(os.sys.argv[4])

#Procesing
promedio=int((peso1+peso2+peso3+peso4)/4)

#verificador
promedio=(promedio<12)

print("promedio:", promedio)

#condicional simple
#SI el pomedio es menor a 11 le saldra estudie mas, de lo contrario reprobara el curso de matematicas
if (promedio == True):
    print("Sigue estudiando, de lo contrario reprobara el curso de matematicas")

#fin-if
