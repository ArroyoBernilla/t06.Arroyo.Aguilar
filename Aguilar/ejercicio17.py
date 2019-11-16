import os
#Boleta de venta de artefactos
#declarar variables
cliente,producto,unidades,pu="","",0,0.0
compra_excesiva=False

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
unidades=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (unidades*pu)
descuento = (unidades*100.0)
precio_a_pagar = (total-descuento)

#VERIFICADOR
compra_excesiva=(precio_a_pagar>25000)

#OUTPUT
print("#############################")
print("#      RIPLEY     ")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", unidades, " unidades ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", precio_a_pagar)
print("#############################")
print("compra excesiva?:", compra_excesiva)

#condicional doble
#si el compra es excesiva mostrarle que ha ganado una regrigeradora
#si el compra no es excesiva decirle que su compra fue muy baja
if(compra_excesiva==True):
    print("OFERTA: usted ha ganado una refrigeradora SAMSUNG")
    print("RECLAME SU PREMIO")
    print("VUELVA PRONTO")

else:
    print("su compra fue muy baja para recibir la oferta")

#fin_if
