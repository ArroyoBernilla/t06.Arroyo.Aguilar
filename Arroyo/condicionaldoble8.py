import os
#Declaracion de variables
cliente,mesero,pollada,pu_de_la_pollada="","",0.0,0.0
gasto_estimado=False

#INPUT
cliente=os.sys.argv[1]
mesero=os.sys.argv[2]
pollada=int(os.sys.argv[3])
pu_de_la_pollada=float(os.sys.argv[4])

# PROCESSING
total = (pollada*pu_de_la_pollada)

# VERIFICADOR
gasto_estimado=(total>200)

# OUTPUT
print("#######################")
print("# RESTAURANTE -EL RINCON DE MIS RECUERDOS")
print("#######################")
print("# Cliente:  ", cliente, " -  # Mesero:", mesero)
print("# Item   :  ",pollada,"platos de arroz con pollo")
print("# P.U.   :  S/.", pu_de_la_pollada)
print("# Total  :  S/.", total)
print("#######################")

#condicional doble
# si el comprador se pasa de 200 soles, ya no podra comprar mas pollada
# si el comprador no se pasa de 200 soles se mostrara: No se olvide de recargar, cada vez que compre

if(gasto_estimado==True):
    print("ALERTA: Solo tiene 200 en su cuenta ")
else:
    print("No se olvide de recargar, cada vez que compre")

#fin-if
