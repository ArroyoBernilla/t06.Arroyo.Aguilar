import os
#Boleta de venta de utiles
#declarar variables
cliente,producto,cantidad,pu="","",0,0.0
comprador_compulsivo=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cantidad=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (cantidad* pu)
descuento = (cantidad*0.1)
precio_a_pagar = (total-descuento)

#VERIFICADOR
comprador_compulsivo=(precio_a_pagar>300)

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
print("compra excesiva?:", comprador_compulsivo)

#condicional doble
#si el comprador es compulsivo mostrarle que ha ganado una mochila
#si el comprador es compulsivo decirle que su compra no llego a lo esperado
if(comprador_compulsivo==True):
    print("OFERTA: usted ha ganado una mochila")

else:
    print("su compra no llego a lo deseado")

#fin_if
