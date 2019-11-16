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

#VERIFICADOR
compra_excesiva=(total>200)

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
print("compra excesiva?:", compra_excesiva)

#condicional simple
#si el comprador es cpompulsivo mostrarle que ha ganado una canasta
if(compra_excesiva==True):
    print("OFERTA: usted ha ganado una canasta")

#fin_if
