#-------------------------------------Variables------------------------------------------------------------
    #endswith()
from os import sep


ejem1 = "Hola como estan"
swith_1 = ejem1.endswith("Hola") 
swith_2 = ejem1.endswith("eis")
swith_3 = ejem1.endswith("estan", 5, 10)
    #expandtabs()
ejem2 = "\tHola"
expand = ejem2.expandtabs(50)
    #find()
ejem3 = "Podrias hacer que me encuentres?"
find1 = ejem3.find("encuentres")
find2 = ejem3.find("Hacer", 3, 10)
    #format() es como format_map()
ejem4 = "Su nombre es {name} y su edad es {age} "
ejem4_1 = "Su nombre es {name:<8} y su edad es {age:<8}"
ejem4_2 = "Su nombre es {name:>8} y su edad es {age:>8}"
ejem4_3 = "Su nombre es {name:^9}"
ejem4_4 = "la prueba dio con un resultado de {:=4}"
ejem4_5 = "en rusia la temperatura es de {temp:+}"
ejem4_6 = "en rusia la temperatura es de {temp:-7} y en colombia es {temp2:-}"
ejem4_7 = "su calificacion en {:8}"
ejem4_8 = "Su producto cuesta {:,} COP"
ejem4_9 = "Su producto cuesta {:_} COP"
ejem4_10 = "1413 en binario es {:b}"
ejem4_11 = "123 en unicode es {:c}"
ejem4_12 = "tengo {:d} gallos"
ejem4_13 = "el resultado es {:e}"
ejem4_14 = "el resultado es {:E}"
ejem4_15 = "el precio es de ${:.2f}"
ejem4_16 = "el precio es de ${:F}"
ejem4_17 = "hola esto es octal {:o}"
ejem4_18 = "el hexa de {0} es {0:x} o {0:X}"
ejem4_19 = "este es un formato numerico {0} y {0:n}"
ejem4_20 = "el porcentaje fue de {0:%} o tambien aumentó del {0:.0%}"
form = ejem4.format(name = "Alexander", age = 16)
form_1 = ejem4_1.format(name = "Alexander", age = 16)
form_2 = ejem4_2.format(name = "Alexander", age = 16)
form_3 = ejem4_3.format(name = "Alexander")
form_4 = ejem4_4.format(-333)
form_5 = ejem4_5.format(temp = -10)
form_6 = ejem4_6.format(temp = -10, temp2 = 26)
form_7 = ejem4_7.format(10)
form_8 = ejem4_8.format(20000)
form_9 = ejem4_9.format(20000)
form_10 = ejem4_10.format(1413)
form_11 = ejem4_11.format(123)
form_12 = ejem4_12.format(0b101)
form_13 = ejem4_13.format(30)
form_14 = ejem4_14.format(30)
form_15 = ejem4_15.format(45)
form_16 = ejem4_16.format(45)
form_17 = ejem4_17.format(333)
form_18 = ejem4_18.format(3)
form_19 = ejem4_19.format(3)
form_20 = ejem4_20.format(50)

    #index
ejem5 = "Hola a todos"
index = ejem5.index("Hola", 0, 7)
#-------------------------------------Textos----------------------------------------------------------------
Intro = "Strings PT.2"
met_ex1 = """'endswith()' Verifica si el tring termina con cierto caracter diciendo true o false"""
met1 = """Su es estructura es String.endswith(Value, start, end) donde 'star y end' define donde se hace la busqueda"""
met_ex2 = """Expandtabs() sirve para definir la distancia de los tabulador '.\.t.' """
met2 = """Su estructra es STRING.EXPANDTABS(TABSIZE)"""
met_ex3 = """Find() Encontrar un caracter en el string"""
met3 = """Su estructura es STRING.FIND(VALUE, START, END)"""
met_ex4 = """Format() y Format_map() para dar formato a un string que esta en un placeholder, lo cual un palceholder
            Se define con '{ }'"""
fact_met4 = """Estos son las caracteristicas que se pueden dar en 'format()', los que tenga X son los que pueden definir su distancia"""
caract = "1. :<x : este hace un especiado hacia la izquierda"

caract2 = "2. :>x : este hace un especiado hacia la derecha"

caract3 = "3. :^x : Centrar "

caract4 = "4. := :  distacian del valo del simbolo"

caract5 = "5. :+ : para indicar si el resultado es positivo o negativo"

caract6 = "6. :- : para solo señalal los negativos"

caract7 = "7. ': ' : un espacio solo para numeros positivos"

caract8 = "8. :, : para separar miles y miles"

caract9 = "9. :_ : separar miles y miles pero con '_'"

caract10 = "10. :b : Formato binario"

caract11 = "11. :c : Lo convuerte en Unicode"

caract12 = "12. :d : formato decimal"

caract13 = "13. :e : Exponencial en minuscula"

caract14 = "14. :E : Exponencil en mayuscula"

caract15 = "15. :fx : decimal"

caract16 = "16. :F : decimales pero dice su formaato inf nan"

caract17 = "17. :g o :G : formato general"

caract18 = "18. :o : formato octal"

caract19 = "19. :x o :X : hex format, lower case o uppercase"

caract20 = "20. :n : formato numerico"

caract21 = "21. :% : para porcentajes"
met4 = """Estructura 
        variable = "string {name_placeholder:caracteristica} y {name_placeholder2:caracteristica}" 
        variable.format(name_placeholder = "x", name_placeholder2 = 33)"""

met_ex5 = """Index() encuentra el primer valor especificado, tambien hace una excepción si el valor no es encontrado"""
met5 = """Su estructura es similar a Find() pero PERO, si find no encuentra el enunciado ese dara -1, entonces string.index(value, star, end)"""
separador = '''----------------------------------------------------------------------------------------------------'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------
print(Intro.center(100, "-"))
print()
print(separador)
print(met_ex1)
print()
print(met1)
print(swith_1)
print()
print(swith_2)
print()
print(swith_3)
print()
print(separador)
print(met_ex2)
print()
print(met2)
print()
print(expand)
print()
print(separador)
print(met_ex3)
print()
print(met3)
print()
print(find1)
print()
print(find2)
print(separador)
print()
print(met_ex4)
print()
print(met4)
print()
print(fact_met4)
print()
print(form)
print()
print(caract)
print()
print(form_1)
print()
print(caract2)
print()
print(form_2)
print()
print(caract3)
print()
print(form_3)
print()
print(caract4)
print()
print(form_4)
print()
print(caract5)
print()
print(form_5)
print()
print(caract6)
print()
print(form_6)
print()
print(caract7)
print()
print(form_7)
print()
print(caract8)
print()
print(form_8)
print()
print(caract9)
print()
print(form_9)
print()
print(caract10)
print()
print(form_10)
print()
print(caract11)
print()
print(form_11)
print()
print(caract12)
print()
print(form_12)
print()
print(caract13)
print()
print(form_13)
print()
print(caract14)
print()
print(form_14)
print()
print(caract15)
print()
print(form_15)
print()
print(caract16)
print()
print(form_16)
print()
print(caract17)
print()
print(caract18)
print()
print(form_17)
print()
print(caract19)
print()
print(form_18)
print()
print(caract20)
print()
print(form_19)
print()
print(caract21)
print()
print(form_20)
print()
print(separador)
print(met_ex5)
print()
print(met5)
print()
print(index)
