#------------------------Variables-----------------------------------
    #Replace()
ejem1 = "Se va a este -----------> reemplazar"
replace = ejem1.replace("reemplazar", "hola")
ejem1_2 = "Ahora se reemplazara estos dos porque se reemplazara por la cantidad de palabras"
replace_2 = ejem1_2.replace("reemplazara", "Listo")
    #rfind()
ejem2 = "Entonces esto sera asi, ¿como asi?"
r_find = ejem2.rfind("asi")
    #rindex
ejem4 = "Hola a todos si no me encuentra es porque no hay o ¿si hay?"
r_index = ejem4.rindex("hay")
    #rjust
ejem3 = "Banana"
rjust = ejem3.rjust(20)
    #rpartition
ejem5 = "Se que puedes hacerlo"
rpartition = ejem5.rpartition("puedes")
    #Rsplit()
ejem6 = "se dividira las palabras en una lista, pero seleccionare 2 palabras que son hola adios"
rsplit = ejem6.rsplit(" ", 2)
#------------------------Textos--------------------------------------
Tittle = "Strings pt6.py"
met_ex1 = "Replace() para reemplazar variable por otra"
met1 = "Su estructura es string.replace(oldvalue, newvalue, count) donde cunt es la cantidad de veces que se repite la palabra"
met_ex2 = "Rfind() Encontrara el ultimo caracter, en vez de find que hace encontrar el primero"
met2 = "Su estructura es string.rfind(value, start, end) en caso que no lo enceuntre dara -1"
met_ex3 = "rjust() Pondra el espaciado hacia la izquierda y pondra la palabra a la derecha"
met3 = "Su estructura es string.rjust(length, character), diferencia de ljust es que quedará en la izquierda y el espaciado a la derecha"
met_ex4 = "Rindex() lo mismo que index solo que sera el ultimo caracter"
met4 = "Su estructura es string.rindex(value, start, end)"
met_ex5 = "Rpartition() Encontara al ultima variable que se refera en el string"
met5 = "Su estrcutura es String.rpartition(), si no encuentro los valores los dejara en la izquierda"
met_ex6 = "Rsplit() separara o eliminara los o las letras qeu estan separando en un string"
met6 = "Su estructura es string.rsplit(separator, maxsplit)"
separador = "----------------------------------------------------------------------------------------------------"
#==================================================================================================================
print(Tittle.center(100, "="))
print()
print(met_ex1)
print()
print(met1)
print()
print(ejem1)
print()
print(replace)
print()
print(ejem1_2)
print()
print(replace_2)
print()
print(separador)
print()
print(met_ex2)
print()
print(met2)
print()
print(ejem2)
print()
print(r_find)
print()
print(separador)
print()
print(met_ex3)
print()
print(met3)
print()
print(ejem4)
print()
print(r_index)
print(separador)
print()
print(met_ex4)
print()
print(met4)
print()
print(ejem3)
print()
print(rjust, "A mil pesos")
print()
print(separador)
print()
print(met_ex5)
print()
print(met5)
print()
print(ejem5)
print()
print(rpartition)
print()
print(separador)
print()
print(met_ex6)
print()
print(met6)
print()
print(ejem6)
print()
print(rpartition)
print()
print(separador)
