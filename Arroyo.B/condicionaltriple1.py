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

#Ouput
print("n1:", n1)
print("n2: ", n2)
print("n3: ", n3)
print("n4: ", n4)

print("promedio:", promedio)

#condicional multiple
#Cada nota es a base 100
#Si el pomedio es igual 100 le saldra: Muy bien alumno, excelente
#Si el pomedio es mayor a 70 y menor a 90 le saldra: Se nota, que le ha puesto empeñoe
#Si el pomedio es menor a 60 le saldra: Sigue estudiando

if (promedio == 100):
    print("excelente")
if (promedio>70 and promedio<90):
    print("Se nota, que le ha puesto empeño")
if (promedio<60):
    print("Sigua estudiando")

#fin-if
