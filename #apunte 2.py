#apunte 2
#Si el primer valor es menor al segundo hacer suma, de lo contrario, resta si es igual multiplicacion
#Diego Espinosa

print("Valor No.1: ")
val1 = int(input())

print("Valor No.2: ")
val2 = int(input())

#Procesos parciales
if val1 < val2:
    res = val1 + val2
else:
    if val1 > val2:
        res = val1 - val2
    else:
        res = val1 * val2

print("Resultado: ", res)