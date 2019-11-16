import os
#Boleta de venta de golosinas
#declarar variables
cliente,producto,bolsas,pu="","",0,0.0
#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
bolsas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (bolsas * pu)
descuento = (bolsas*0.3)
precio_a_pagar = (total-descuento)

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
print("USTED:")

#condicional multiple
#si la compra supera los 500 soles decirle al comprador que ha ganado 10 bolsas mas del producto
#si la compra esta entre los 250 y 500 soles mostrarle al comprador que ha ganado 5 bolsas mas del producto
#si la compra es menor a 250 soles decirle que no ha gando nada
if(precio_a_pagar>500):
    print("ha ganado 10 bolsas de " + producto + " mas")
if(precio_a_pagar>=250 and precio_a_pagar<=500):
    print("ha ganado 5 bolsas mas de " + producto)
if(precio_a_pagar<250):
    print("no ha ganado nada")

#fin_if
