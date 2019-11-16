import os
#declarar variables de frutas
cliente,producto,kg,pu="","",0,0.0
#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
kg=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total =float(pu * kg)

#OUTPUT
print("#############################")
print("# BODEGA - ANITA")
print("#############################")
print("#")
print("# Cliente  : ", cliente)
print("# Producto :", producto)
print("# Item     : ",kg, "kg")
print("# P.U.     : ", pu)
print("# Total    : ", total)
print("#############################")
print("PREMIO: ")

#condicional multiple
#si la compra es mayor a 200 soles mostrarle al comprador que ha ganado una canasta
#si la compra esta entre 100 y 200 soles mostrarle al comprador que ha ganado un paneton
#si la compra es menor a 100 soles decirle que no ha ganado nada

if(total>200):
    print("usted ha ganado una canasta")
if(total>=100 and total<200):
    print("usted a ganado un paneton")
if(total<100):
    print("usted no ha ganadado nada")

#fin_if
