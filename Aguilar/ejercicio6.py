import os

#notas en base 20
#declarar variables
alumno,nota1,nota2,nota3,nota4="",0.0,0.0,0.0,0.0
nota_final=0.0

#INPUT
alumno=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])
nota4=int(os.sys.argv[5])

#PROCESSING
nota_final=int((nota1+nota2+nota3+nota4)/4)

#OUPUT
print(" NOTAS DEL CURSO DE MATEMATICAS")
print(" El alumno: ", alumno)
print("obtubo las siguientes notas")
print("primera nota: ", nota1)
print("segunda nota: ", nota2)
print("tercera nota: ", nota3)
print("cuarta nota: ", nota4)
print("nota final: ", nota_final )
print("COMENTARIO:")

#verificador
promedio=(nota_final>17)

#condicional simple
#SI el pomedio es mayor a 17 felicitar al estudiante
if (promedio == True):
    print("FELICITACONES HAS OBTENIDO UN MARAVILLOSO PUNTAJE")

#fin_if
