import os
#Boleta de venta de bebidas
#declarar variables
cliente,producto,six_pack,pu="","",0,0.0
comprador_compulsivo=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
six_pack=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (six_pack * pu)
descuento = (six_pack*0.5)
precio_a_pagar = (total-descuento)

#VERIFICADOR
comprador_compulsivo=(precio_a_pagar>3000)

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
print("compra excesiva?:", comprador_compulsivo)

#condicional doble
#si el comprador es cpompulsivo mostrar que ha ganado un viaje a ICA
#si el comprador no es compulsivo decirle que no pudo ganar nada
if(comprador_compulsivo==True):
    print("OFERTA: usted ha ganado un viaje a Ica todo pagado")
else:
    print("lo sentimos no pudo ganar nada :(")

#fin_if
