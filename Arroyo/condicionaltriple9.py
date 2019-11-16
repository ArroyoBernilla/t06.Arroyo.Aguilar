import os
#declarar variables
trabajo,tiempo=0.0,0.0
potencia=0.0

#Input
trabajo=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

#Procesing
potencia=int(trabajo/tiempo)

#Ouput
print("El trabajo realizado por el motor:" , trabajo)
print("Tiempo utilizado por el motor : ", tiempo)
print("Potencia del motor : ", potencia)

#condicional multiple
#Si la potencia realizada por el motor es mayor a 200, le mostrara; La condicion del motor esta optima
#Si la potencia realizada por el motor es mayor 100 y menor a 170, le mostrara; El motor esta trabando muy bien
#Si la potencia realizada por el motor es menor a 90, le mostrara; El motor necesita revision tecnica

if (potencia > 200):
    print("La condicion del motor esta optima")

if (potencia > 100 and potencia<170):

    print("El motor esta trabando muy bien")
if (potencia==90):
    print("El motor necesita revision tecnica")

#fin-if
