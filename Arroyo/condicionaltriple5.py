import os
#declarar variables
n1,n2,n3,n4=0.0,0.0,0.0,0.0
promedio=0.0

#input
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])

#Procesing
promedio=int((n1+n2+n3+n4)/4)


print("promedio:", promedio)

#condicional multiple
#Cada nota es a base 100
#Si el pomedio es igual 100 le saldra: Excelente, se nota que se ha esforzado
#Si el pomedio es mayor a  70 y menor a 90 le saldra: Muy bien, usted puede sacar una mejor nota
#Si el pomedio es menor a  30  le saldra: Por favor, repase sus practicas

if (promedio == 100):
    print("Excelente, se nota que se ha esforzado")
if (promedio>70 and promedio<90):
    print("Muy bien, usted puede sacar una mejor nota")
if (promedio<30):
    print("Por favor, repase sus practicas")

#fin-if
