import os
#Declaracion de variables
cliente,mesero,cantidad_de_platos_de_arroz_con_pollo,pu_del_arroz_con_pollo="","",0.0,0.0
compra_limite=False

#INPUT
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
cantidad_de_platos_de_arroz_con_pollo=int(os.sys.argv[3])
pu_del_arroz_con_pato=float(os.sys.argv[4])

# PROCESSING
total = (pu_del_arroz_con_pollo * cantidad_de_platos_de_arroz_con_pollo)

# VERIFICADOR
compra_limite=(total>100)

# OUTPUT
print("#######################")
print("# RESTAURANTE -EL RINCON DE MIS RECUERDOS")
print("#######################")
print("# Cliente:  ", cliente, " -  # Mesero:", mesero)
print("# Item   :  ",cantidad_de_platos_de_arroz_con_pollo,"platos de arroz con pollo")
print("# P.U.   :  S/.", pu_del_arroz_con_pollo)
print("# Total  :  S/.", total)
print("#######################")

#condicional simple
# si el comprador se pasa de 100 soles no podra pagar la cuenta
if(compra_limite==True):
    print("AVISO: Recargue su tarjeta")

#fin-if
