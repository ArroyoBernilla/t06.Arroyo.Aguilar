import os
#Boleta de venta productos del hogar
#declarar variables
cliente,producto,cajas,pu="","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cajas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (cajas * pu)
descuento = (cajas*0.1)
precio_a_pagar = (total-descuento)

#OUTPUT
print("#############################")
print("# MAYORISTA - PABLITO #")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", cajas, "cajas")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("PREMIO")

#condicional multiple
#si la compra supera los 200 mostrarle que ha ganado dos cajas mas del producto
#si la compra esta entee 100 a 200 soles mostrarle que ha ganado una caja mas del producto
#si la compra si la compra es menor que 100 soles, decirle que no gano nada

if(precio_a_pagar>200):
    print("OFERTA: usted ha ganado 2 cajas de " + producto + " mas")
if(precio_a_pagar>=100 and precio_a_pagar<200):
    print("usted ha ganado un caja mas de ", producto)
if(precio_a_pagar<100):
    print("usted no ha ganado nada")

#fin_if
