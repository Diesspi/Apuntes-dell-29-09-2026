'''
Apunte3 
Diego Espinosa Galarza
Realizar un algoritmo para determinar la bonificacion que recibe un empleado
de la compañia ABC, la cual les otorgan una sola vez al año una bonificacion
de acuerdo con su salario basico y los años de antiguedad 
'''
salBas = float (input("Salario basico: "))
tieSer = int(input("Tiempo de servicio en años: "))

#Procesos parciales
if tieSer < 5:
    porBon = 5
else: 
    if tieSer < 10: 
        porBon = 10
    else:
        if tieSer <15:
            porBon = 15
        else: 
            if tieSer < 20:
                porBon = 20
            else:
                if tieSer < 25:
                    porBon = 25 
                else: 
                    if tieSer < 30:
                        porBon = 35
                    else:
                        porBon = 50
                        

valBon = salBas * porBon / 100

#Datos de salida parciales 
print("Porcentaje de bonificacion: ", porBon)
print("Valor de la bonificacion: ", valBon)