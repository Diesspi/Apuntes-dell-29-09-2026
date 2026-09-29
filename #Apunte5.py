#Apunte5
#Diego Espinosa

print("Sueldo base: ")
suelBas = int(input())
print("Valor de venta:")
valVen = int(input())

if valVen < 100000:
    porCom = 10
else :
    porCom = 15
    
valCom = valVen * porCom / 100
suelNet = suelBas + valCom

print("Porcentaje de comisión: ", porCom)
print("Valor comisión: ", valCom)
print("Sueldo neto: ", suelNet)