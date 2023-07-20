# Declaracion de meses y sueldo correspondiente
enero_junio = 300
julio_octubre = 500
noviembre_diciembre = 700
total_anual = (enero_junio * 6 + julio_octubre * 4 + noviembre_diciembre * 2)

# Inicio del programa
print("Inicio del programa")
# Imprimir sueldo anual
print("El sueldo anual de Juan es: ", "u$d", total_anual, "al año.")
# Calcular sueldo promedio y el resultado sea un entero
sueldo_promedio = int(total_anual / 12)
# Imprimir sueldo promedio
print("El sueldo promedio es: ", "u$d", sueldo_promedio, "al mes.")
# Comparacion de sueldo
if sueldo_promedio < 300:
    print("El sueldo es bajo!")
elif sueldo_promedio >= 300 and sueldo_promedio <= 500:
    print("El sueldo es normal!")
else:
    print("Sueldo mejor de lo normal!")
if sueldo_promedio < 300:
    print("Sueldo bajo")
elif sueldo_promedio >= 300 and sueldo_promedio <= 500:

    # Fin del programa
    print("Fin del programa")
