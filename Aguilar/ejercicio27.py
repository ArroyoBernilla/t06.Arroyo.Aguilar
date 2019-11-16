import os
#Boleta de venta de artefactos
#declarar variables
cliente,producto,unidades,pu="","",0,0.0

#INPUT
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
unidades=int(os.sys.argv[3])
pu=float(os.sys.argv[4])

#PROCESSING
total = (unidades*pu)
descuento = (unidades*100.0)
monto_total = (total-descuento)

#OUTPUT
print("#############################")
print("#      RIPLEY    ")
print("#############################")
print("#")
print("# Cliente          : ", cliente)
print("# Producto         : ", producto)
print("# Item             : ", unidades, " unidades ")
print("# P.U.             : ", pu)
print("# Total            : ", total)
print("# Descuento        : ", descuento)
print("# Precio a pagar   : ", monto_total)
print("#############################")
print(" ESTIMADO CLIENTE")

#condicional multiple
#si el compra es mayor a 25000 mostrar que ha ganado una refrigeradora
#si la compra esta entre 10000 y 25000 soles decirle que ha ganado un parlante
#si la compra es menor a 10000 soles decirle que no ha ganado nada
if(monto_total>25000):
    print("ha ganado una refrigeradora SAMSUNG")
    print("RECLAME SU PREMIO")
    print("VUELVA PRONTO")
if(monto_total>=10000 and monto_total<=25000):
    print("ha ganado un parlante con amplificador")
if(monto_total<10000):
    print("no pudo ganar nada")

#fin_if
