import os

#simulacros academicos
#declarar variables
estudiante,simulacro1,simulacro2,simulacro3,simulacro4,simulacro5,simulacro6="",0.0,0.0,0.0,0.0,0.0,0.0
puntaje_final=0.0

#INPUT
estudiante=os.sys.argv[1]
simulacro1=int(os.sys.argv[2])
simulacro2=int(os.sys.argv[3])
simulacro3=int(os.sys.argv[4])
simulacro4=int(os.sys.argv[5])
simulacro5=int(os.sys.argv[6])
simulacro6=int(os.sys.argv[7])

#PROCESSING
puntaje_final=int((simulacro1+simulacro2+simulacro3+simulacro4+simulacro5+simulacro6)/6)

#OUPUT
print(" NOTAS DE EXAMENES SIMULACROS")
print(" El alumno: ", estudiante)
print("obtubo los siguientes puntajes")
print("primer simulacro: ", simulacro1)
print("segundo simulacro: ", simulacro2)
print("tercer simulacro: ", simulacro3)
print("cuarto simulacro: ", simulacro4)
print("quinto simulacro: ", simulacro5)
print("sexto simulacro: ", simulacro6)
print("puntaje final: ", puntaje_final)
print("COMENTARIO:")

#verificador
ingresa=(puntaje_final>90)

#condicional simple
#SI el puntaje final es mayor a 90 tenga toda la certeza de que va a ingresar
if (ingresa == True):
    print("TENGA TODA LA SEGURIDAD DE QUE VA A INGRESAR")
    print("NO SE DEJE LLEVAR POR LO NERVIOS")

#fin_if
