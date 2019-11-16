import os
#Declaracion de variables
cliente,mesero,cantidad_de_cemento,pu_del_cemento="","",0.0,0.0
comprador_compulsivo=False


#INPUTN4
cliente=os.sys.argv[1]
cajero=os.sys.argv[2]
cantidad_de_cemento=int(os.sys.argv[3])
pu_del_cemento=float(os.sys.argv[4])

# PROCESSING
total = (pu_del_cemento*pu_del_cemento)
#verificador
comprador_compulsivo=(total>200)

# OUTPUT
print("#######################")
print("# FERRERTERIA - PERNO LOCO")
print("#######################")
print("# Cliente:  ", cliente, " -  # cajero:", cajero)
print("# Item   :  ",cantidad_de_cemento," cementos pacasmayo")
print("# P.U.   :  S/.", pu_del_cemento)
print("# Total  :  S/.", total)
print("#######################")

#condicional simple
#si el comprador es compulsivo mostrarle la ofecta de descuento
if(comprador_compulsivo==True):
    print("AVISO: Usted ha ganado un descuento")

#fin-if
