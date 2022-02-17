#-------------------------------------Variables------------------------------------------------------------
    #endswith()
ejem1 = "Hola como estan"
swith_1 = ejem1.endswith("Hola") 
    #expandtabs()
    #find()
    #format() es como format_map()
    #index

#-------------------------------------Textos----------------------------------------------------------------
Intro = "Strings PT.2"
met_ex1 = """'endswith()' Verifica si el tring termina con cierto caracter diciendo true o false"""
met1 = """Su es estructura es String.endswith(Value, start, end) donde 'star y end' define donde se hace la busqueda"""
met_ex2 = """Expandtabs() sirve para definir la distancia de los tabulador '.\.t.' """
met2 = """Su estructra es STRING.EXPANDTABS(TABSIZE)"""
met_ex3 = """Find() Encontrar un caracter en el string"""
met3 = """Su estructura es STRING.EXPANDTABS(VALUE, START, END)"""
met_ex4 = """Format() y Format_map() para dar formato a un string que esta en un placeholder, lo cual un palceholder
            Se define con '{ }'"""
fact_met4 = """Estos son las caracteristicas que se pueden dar en 'format()', los que tenga X son los que pueden definir su distancia

    1. :<x : este hace un especiado hacia la izquierda

    2. :>x : este hace un especiado hacia la derecha

    3. :^x : Centrar 

    4. := :  distacian del valo del simbolo

    5. :+ : para indicar si el resultado es positivo o negativo

    6. :- : para solo señalal los negativos

    7. ': ' : un espacio solo para numeros positivos

    8. :, : para separar miles y miles

    9. :_ : separar miles y miles pero con "_"

    10. :b : Formato binario

    11. :c : Lo convuerte en Unicode

    12. :d : formato decimal

    13. :e : Exponencial en minuscula

    14. :E : Exponencil en mayuscula

    15. :fx : decimal
    
    16. :F : decimales pero dice su formaato inf nan

    17. :g o :G : formato general

    18. :o : formato octal

    19. :x o :X : hex format, lower case o uppercase

    20. :n : formato numerico

    21. :% : para porcentajes
"""
met4 = """Estructura 
        variable = "string {name_placeholder:caracteristica} y {name_placeholder2:caracteristica}" 
        variable.format(name_placeholder = "x", name_placeholder2 = 33)"""

met_ex5 = """Index() encuentra el primer valor especificado, tambien hace una excepción si el valor no es encontrado"""
met5 = """Su estructura es similar a Find() pero PERO, si find no encuentra el enunciado ese dara -1, entonces string.index(value, star, end)"""
separador = '''--------------------------------------------------------------------------------------------------------------------------------------------------------------'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------
