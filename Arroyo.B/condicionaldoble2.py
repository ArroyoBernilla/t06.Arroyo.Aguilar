#Condicion Nª2
import os
#Boleta de venta
#declarar variables
cliente,cajero,cantidad_de_cemento,pu_del_cemento="","",0.0,0.0
comprador_compulsivo=False

#INPUTN4
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
cantidad_de_cemento=int(os.sys.argv[3])
pu_del_cemento=float(os.sys.argv[4])

# PROCESSING
total = (pu_del_cemento*pu_del_cemento)
#verificador
comprador_compulsivo=(total>500)

# OUTPUT
print("#######################")
print("# FERRERTERIA - PERNO LOCO")
print("#######################")
print("# Cliente:  ", cliente, " -  # cajero:", cajero)
print("# Item   :  ",cantidad_de_cemento," cementos pacasmayo")
print("# P.U.   :  S/.", pu_del_cemento)
print("# Total  :  S/.", total)
print("#######################")

#si el comprador es compulsivo mostrarle la ofecta de descuento
#si el comprador no es compulsivo mostrarle AVISO:Sigua comprando y obtendra multiples beneficios
if(comprador_compulsivo==True):
    print("AVISO: Usted ha ganado un descuento")
else:
    print("AVISO: Sigua comprando y obtendra multiples beneficios.")

#fin-if
