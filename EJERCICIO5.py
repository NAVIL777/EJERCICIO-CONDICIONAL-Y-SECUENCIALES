import os
os.system("cls")
# Preguntar al usuario por la renta
renta = float(input("¿Cual es tu renta anual?"))
# Condicional para determinar el tipo impositivo dependien de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 40000:
    tipo = 25
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impsitivo
print("Tienes que pagar", renta * tipo / 100, "$", sep='')

