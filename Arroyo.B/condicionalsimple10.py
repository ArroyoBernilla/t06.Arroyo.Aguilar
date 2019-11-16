import os
#declarar variables
n1,n2,n3,n4=0.0,0.0,0.0,0.0
promedio=False

#input
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])

#Procesing
promedio=int((n1+n2+n3+n4)/4)

#verificador
promedio=(promedio==100)

print("promedio:", promedio)

#condicional simple
#Cada nota es a base 100
#Si el pomedio es igual 100 le saldra: Muy bien alumno, excelente
if (promedio == True):
    print("Muy bien alumno, excelente")

#fin-if
