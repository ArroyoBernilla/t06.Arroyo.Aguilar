import os
#Boleta de venta de productos del hogar
#declarar variables
cliente,producto,cajas,pu="","",0,0.0
compra_excesiva=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cajas=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (cajas * pu)
descuento = (cajas*0.1)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>150)

#OUTPUT
print("#############################")
print("# MAYORISTA - PABLITO")
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
print("compra excesiva?:", compra_excesiva)

#condicional doble
#si el comprador es cpompulsivo mostrarle que ha ganado dos cajas mas del producto
#si el comprador no es compulsivo decirle que siga intentando
if(compra_excesiva==True):
    print("OFERTA: usted ha ganado 2 cajas de " + producto + " mas")

else:
    print("siga intentado")

#fin_if
