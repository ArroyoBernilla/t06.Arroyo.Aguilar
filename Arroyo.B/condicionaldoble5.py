import os
#declarar variables
cliente,producto,cantidad,pu="","",0,0.0
compra_excesiva=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total =int(pu * cantidad)

#VERIFICADOR
compra_excesiva=(total>200)

#OUTPUT
print("#############################")
print("# FACTURA DE COMPRA")
print("#############################")
print("#")
print("# Cliente  : ", cliente)
print("# Producto :", producto)
print("# Cantidad : ",cantidad, )
print("# P.U.     : ", pu)
print("# Total    : ", total)
print("#############################")


#si el comprador es compulsivo le saldra AVISO: No malgaste su dinero en cosas innecesarias
#si el comprador no es compulsivo le saldra Excelente compra, feliidades, disfrutela
if(compra_excesiva==True):
    print("AVISO: No malgaste su dinero en cosas innecesarias")
else:
    print("Excelente compra, feliidades, disfrutela")

#fin-if
