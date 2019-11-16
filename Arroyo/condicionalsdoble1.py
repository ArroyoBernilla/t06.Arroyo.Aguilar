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
nota_final=(promedio<14)

# OUTPUT
print("promedio:", promedio)

#condicional simple
#Si el pomedio es menor a catorce le saldra como mensaje: sigue estudiando
#Si el pomedio es mayor a trece le saldra como mensaje: Bien, sigua esforzandose
if (nota_final == True):
    print("Sigue estudiando")
else:
    print("Bien, sigua esforzandose")
#fin-if
