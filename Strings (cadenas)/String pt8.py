#-------------------------------Variables--------------------------------------------
    #swapcase()
ejem1 = "Hello My Name Is PETER"

swap = ejem1.swapcase()

    #title()

ejem2 = "Welcome to my world"

title = ejem2.title()
    #translate()
maketrans = {83:  80}
ejem3 = "Hello Sam!"
trans = (ejem3.translate(maketrans))

    #upper()
ejem4 = "Hello my friends"

upper = ejem4.upper()


    #zfill()
a = "hello"
b = "welcome to the jungle"
c = "10.000"

zf = a.zfill(10)
zf_2 = b.zfill(10)
zf_3 = c.zfill(10)

#-------------------------------textos-----------------------------------------------
tittle = "String pt8"
met_ex1 = "El método swapcase() devuelve una cadena donde todas las letras mayúsculas son minúsculas y viceversa."
met1 = "string.swapcase()"
met_ex2 = "El método title() devuelve una cadena en la que el primer carácter de cada palabra es mayúscula. Como una cabecera, o un título."
met2 = "string.title() Si la palabra contiene un número o un símbolo, la primera letra después se convertirá en mayúscula."
met_ex3 = """El método translate() devuelve una cadena en la que algunos caracteres especificados se sustituyen por el carácter descrito en un diccionario, o en una tabla de asignación.

Utilice el método maketrans() para crear una tabla de asignación.

Si un carácter no está especificado en el diccionario/tabla, el carácter no será reemplazado.

Si utiliza un diccionario, debe utilizar códigos ascii en lugar de caracteres.
"""
met3 = "string.translate(table), table Requerido. Un diccionario o una tabla de asignación que describa cómo realizar la sustitución"
met_ex4 = "El método upper() devuelve una cadena en la que todos los caracteres están en mayúsculas."
met4 = "string.upper()  Los símbolos y los números se ignoran."
met_ex5 = "El método zfill() añade ceros (0) al principio de la cadena, hasta alcanzar la longitud especificada."
met5 = "string.zfill(len) Si el valor del parámetro len es menor que la longitud de la cadena, no se realiza ningún relleno."
separador = "==================================================================================================================================================================="
#---------------------------------------------------------------------------------------------------------------------------
print(tittle.center(100, "="))
print()
print(met_ex1)
print()
print(met1)
print()
print(ejem1)
print()
print(swap)
print()
print(separador)
print()
print(met_ex2)
print()
print(met2)
print()
print(ejem2)
print()
print(title)
print()
print(separador)
print()
print(met_ex3)
print()
print(met3)
print()
print(ejem3)
print()
print(trans)
print()
print(separador)
print()
print(met_ex4)
print()
print(met4)
print()
print(ejem4)
print()
print(upper)
print()
print(separador)
print()
print(met_ex5)
print()
print(met5)
print()
print(a)
print()
print(b)
print()
print(c)
print()
print(zf)
print()
print(zf_2)
print()
print(zf_3)