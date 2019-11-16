import os
#Boleta de venta de golosinas
#declarar variables
cliente,producto,bolsas,pu="","",0,0.0
comprador_excesivo=False
#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
bolsas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (bolsas * pu)
descuento = (bolsas*0.3)
precio_a_pagar = (total-descuento)

#VERIFICADOR
comprador_excesivo=(precio_a_pagar>250)

#OUTPUT
print("#############################")
print("# BOLETA DE VENTA")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", bolsas, "bolsas")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("comprador compulsivo?:", comprador_excesivo)

#condicional simple
#si el comprador es compulsivo, mostrar que ha ganado 10 bolsas mas del producto que lleva
if(comprador_excesivo==True):
    print("OFERTA: usted ha ganado 10 bolsas de " + producto + " mas")

#fin_if
