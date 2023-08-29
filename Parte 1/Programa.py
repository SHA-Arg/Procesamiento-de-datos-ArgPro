# Declaracion de meses y sueldo correspondiente
enero_junio = 300
julio_octubre = 500
noviembre_diciembre = 700
total_anual = (enero_junio * 6 + julio_octubre * 4 + noviembre_diciembre * 2)


print("===================================")
print("PARTE 1 v1.0 Consigna")
print("===================================")
print("El empleado llamado Juan cobró: ")
print("...................................")
print("""300 dólares por mes desde enero a junio, 
500 dólares de julio a octubre, 
700 dólares por mes en noviembre y en diciembre. """)
print("...................................")
# Imprimo el sueldo anual
print("El sueldo anual de Juan es:", f"u$d {total_anual}" , "al año.")

# Calculo del sueldo promedio 
sueldo_promedio = int(total_anual / 12)

# Muestro por consola el sueldo promedio
print( "El sueldo promedio es:", f"u$d {sueldo_promedio}" , "al mes.")
print("______________________________________")

# Comparacion de sueldo
if sueldo_promedio < 300:
    print("El sueldo es bajo!")
elif sueldo_promedio >= 300 and sueldo_promedio <= 500:
    print("El sueldo es normal!")
else:
    print("Sueldo mejor de lo normal!")    
print("#######################################")


#Version colorida
from colorama import init, Fore

# Declaracion de meses y sueldo correspondiente
enero_junio = 300
julio_octubre = 500
noviembre_diciembre = 700
total_anual = (enero_junio * 6 + julio_octubre * 4 + noviembre_diciembre * 2)

print(Fore.MAGENTA + "===================================" + Fore.RESET)
print(Fore.CYAN + "PARTE v1.1 (Version colorida)" + Fore.RESET)
print(Fore.MAGENTA + "===================================" + Fore.RESET)
print(Fore.BLUE + "El empleado llamado Juan cobró: " + Fore.RESET)
print(Fore.CYAN + "..................................." + Fore.RESET)
print(Fore.YELLOW + """300 dólares por mes desde enero a junio, 
500 dólares de julio a octubre, 
700 dólares por mes en noviembre y en diciembre. """ + Fore.RESET)
print(Fore.CYAN + "..................................." + Fore.RESET)


# Imprimir sueldo anual
print(Fore.MAGENTA + "El sueldo anual de Juan es:", Fore.GREEN + f"u$d {total_anual}" , "al año."+ Fore.RESET)

# Calculo del sueldo promedio 
sueldo_promedio = int(total_anual / 12)

# Muestro por consola el sueldo promedio
print(Fore.MAGENTA + "El sueldo promedio es:", Fore.GREEN + f"u$d {sueldo_promedio}" , "al mes."+ Fore.RESET)

print(Fore.CYAN + "____________________________________" + Fore.RESET)
# Comparacion de sueldo
if sueldo_promedio < 300:
    print(Fore.RED + "El sueldo es bajo!" )
elif sueldo_promedio >= 300 and sueldo_promedio <= 500:
    print(Fore.YELLOW + "El sueldo es normal!" + Fore.RESET)
else:
    print(Fore.GREEN + "Sueldo mejor de lo normal!" + Fore.RESET)
    print(Fore.CYAN + "########################################" + Fore.RESET)
