import os
#declarar variables
cliente,producto,kg,pu="","",0,0.0
compra_excesiva=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
kg=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total =int(pu * kg)

#VERIFICADOR
compra_excesiva=(total>200)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente  : ", cliente)
print("# Producto :", producto)
print("# Item     : ",kg, "kg")
print("# P.U.     : ", pu)
print("# Total    : ", total)
print("#############################")


#condicional simple
#si el comprador es cpompulsivo mostrarle la oferta de la tarjeta
#si el comprador no  es cpompulsivo AVISO: Usted ha ganado 100 puntos por su compra
if(compra_excesiva==True):
    print("OFERTA: usted ha ganado una tarjeta dorada")
else:
    print("AVISO: Usted ha ganado 100 puntos por su compra")

#fin-if
