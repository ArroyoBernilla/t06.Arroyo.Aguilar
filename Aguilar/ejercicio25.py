import os
#Boleta de venta de bebidas
#declarar variables
cliente,producto,six_pack,pu="","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
six_pack=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (six_pack * pu)
descuento = (six_pack*0.5)
precio_a_pagar = (total-descuento)

#OUTPUT
print("#############################")
print("#           METRO          #")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", six_pack, "six pack")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("USTED:")

#condicional multiple
#si la compra es mayor a 3000 soles mostras que ha ganado un viaje a ICA
#si la compra esta entre 1000 y 3000 soles decirleque ga ganado una licuadora
#si la compra es menor a 1000 soles decirle que lamentablemente no ha ganado nada
if(precio_a_pagar>3000):
    print("ha ganado un viaje a Ica todo pagado")
if(precio_a_pagar>=1000 and precio_a_pagar<=3000):
    print("ha ganado una licuadora")
if(precio_a_pagar<1000):
    print("no ha ganado nada")

#fin_if
