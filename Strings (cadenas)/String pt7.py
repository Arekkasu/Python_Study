#------------------------------------------Variables---------------------------------------------------------
    #rstrip()
ejem1 = "     banana     "
strip = ejem1.rstrip()
ejem1_2 = "banana,,,,,ssqqqww....."
strip_2 = ejem1_2.rstrip(",.qsw")
    #split()
ejem2 = "hello, my name is Peter, I am 26 years old"
split = ejem2.split(", ")
ejem2_1 = "apple#banana#cherry#orange"
split_2 = ejem2_1.split("#", 1)
    #splitlines()
ejem3 = "Thank you for the music\nWelcome to the jungle"
splitl = ejem3.splitlines()
splitl_2 =  ejem3.splitlines(True)
    #startswith()
ejem4 = "Hello, welcome to my world."
starts = ejem4.startswith("Hello")
starts_2 = ejem4.startswith("wel", 7, 20)
    #strip()
ejem5 = "     banana     "
strip = ejem5.strip()
ejem5_1 = ",,,,,rrttgg.....banana....rrr"
strip_2  = ejem5_1.strip(",.grt")
#------------------------------------------Textos------------------------------------------------------------
tittle = "String pt8"
met_ex1 = "El método rstrip() elimina cualquier carácter final (caracteres al final de una cadena), el espacio es el carácter final por defecto a eliminar."
met1 = "string.rstrip(characters)"
met_ex2 = """El método split() divide una cadena en una lista.

Puede especificar el separador, el separador por defecto es cualquier espacio en blanco.

Nota: Cuando se especifica maxsplit, la lista contendrá el número de elementos especificado más uno."""
met2 = """string.split(separator, maxsplit)
separador Opcional. Especifica el separador que se utilizará al dividir la cadena. Por defecto, cualquier espacio en blanco es un separador

maxsplit Opcional. Especifica el número de divisiones a realizar. El valor por defecto es -1, que es "todas las ocurrencias".
"""
met_ex3 = "El método splitlines() divide una cadena en una lista. La división se realiza en los saltos de línea."
met3 = "string.splitlines(keeplinebreaks) keeplinebreaks Opcional. Especifica si los saltos de línea deben ser incluidos (True), o no (False). El valor por defecto es Falso"
met_ex4 = "El método startswith() devuelve True si la cadena empieza por el valor especificado, en caso contrario False."
met4 = "string.startswith(value, start, end)"
met_ex5 = "El método strip() elimina los caracteres iniciales (espacios al principio) y finales (espacios al final) (el espacio es el carácter inicial que se elimina por defecto)"
met5 = "string.strip(characters)"
separador = "==================================================================================================================================================================="
#--------------------------------------------------------------------------------------------------------------------------
print(tittle.center(100, "="))
print()
print(met_ex1)
print()
print(met1)
print()
print(ejem1)
print()
print(strip)
print()
print(ejem1_2)
print()
print(strip_2)
print()
print(separador)
print()
print(met_ex2)
print()
print(met2)
print()
print(ejem2)
print()
print(split)
print()
print(ejem2_1)
print()
print(split_2)
print()
print(separador)
print()
print(met_ex3)
print()
print(met3)
print()
print(ejem3)
print(splitl)
print()
print(splitl_2)
print()
print(separador)
print()
print(met_ex4)
print()
print(met4)
print()
print(ejem4)
print()
print(starts)
print()
print(starts_2)
print()
print(separador)
print()
print(met_ex5)
print()
print(met5)
print()
print(ejem5)
print()
print(strip)
print()
print(ejem5_1)
print()
print(strip_2)