# Establecer comparaciones entre las edades de dos hermanos.
print('Vamos a calcular cuál es el hermano mayor y la diferencia de edades entre los dos hermanos.\n')
# Repetir los mensajes hacia el usario, para ejecutar el programa n veces.
active = True
while active:
    age_1 = input('\nIngresar edad del primer hermano: ')
    name_1 = input('Ingresar el nombre del primer hermano: ')
    age_2 = input('\nIngresar edad del segundo hermano: ')
    name_2 = input('Ingresar el nombre del segundo hermano: ')
    
# Controlar que los datos que se ingresen sean números enteros. 
    try:
        age_1 = int(age_1)
        age_2 = int(age_2)
    except:
        print('\n\tPor favor introduce edades válidas.')
        continue
# Comparar las edades de ambos hermanos e imprimir el mensaje. 
    if age_1 >= 0 and age_2 >= 0:
        if age_1 > age_2:
            print(f'\n\t{name_1.title()} con {age_1} año(s) es mayor que {name_2.title()} con {age_2} año(s).')       
        elif age_1 == age_2:
            print(f'\n\t{name_1.title()} con {age_1} año(s) tiene la misma edad que {name_2.title()} con {age_2} año(s).')
        else:
            print(f'\n\t{name_2.title()} con {age_2} año(s) es mayor que {name_1.title()} con {age_1} año(s). ')           
        diff_age = age_1 - age_2    # Calcula la diferencia de edades y luego se imprime
        diff_age = abs(diff_age)
        print(f'\n\tLa diferencia de edades entre los hermanos es de {diff_age} año(s).')
    else:
        print('\nLas edades deben ser mayor o igual a cero. ')
        print()
# Preguntarle al usuario si desea volver a ejecutar el programa
    restart = input('\nDesea volver a ejecutar este programa (s/n): ')
    if restart.lower() == 's' or restart.lower() == 'si':
        continue
    else:
        active = False

print('\nEl programa ha finalizado, nos vemos en otra ocasión.')
