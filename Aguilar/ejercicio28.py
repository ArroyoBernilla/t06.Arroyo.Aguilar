import os
#Boleta de venta de utiles
#declarar variables
cliente,producto,cantidad,pu="","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (cantidad* pu)
descuento = (cantidad*0.2)
precio_a_pagar = (total-descuento)

#OUTPUT
print("#############################")
print("# LIBRERIA BETO")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", cantidad, " cuadernos ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("ESTIMADO CLIENTE")

#condicional multiple
#si la compra supera el monto de los 300 soles mostrarle que ha ganado una mochila
#si la compra esta entre los 100 y 300 soles decirle quenha ganado un juego de escuadras
#si la compra es menor a los 100 soles decirle que no ha ganado nada
if(precio_a_pagar>300):
    print("OFERTA: usted ha ganado una mochila")
if(precio_a_pagar>=100 and precio_a_pagar<=300):
    print("ha ganado un juego de escuadras")
if(precio_a_pagar<100):
    print("lamentablemnte no ha ganado nada")

#fin_if
