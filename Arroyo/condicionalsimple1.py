#Condicion Nª1
import os
#declarar variables
nota1,nota2,nota3,nota4=0.0,0.0,0.0,0.0
nota_final=0.0

#input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])

#Procesing
promedio=int((nota1+nota2+nota3+nota4)/4)

#verificador
nota_final=(promedio<16)

# OUTPUT
print("promedio:", promedio)

#condicional simple
#Si el pomedio es menor a trece le saldra como mensaje: sigue estudiando

if (nota_final == True):
    print("Sigue estudiando")

#fin-if
