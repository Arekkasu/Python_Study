#Variables
        #count()

ejem = "hola a todos"
ejem1 = "HOLA a todos"
ejem2 = "38 edad"
cap1 = ejem.capitalize()
cap2 = ejem1.capitalize()
cap3 = ejem2.capitalize()
        #casefold()

ejem3 = "Hola A Todos"
fold = ejem.casefold()

        #center()

ejem4 = "Hola"
cent = ejem4.center(20) 
cent2 = ejem4.center(20, "p")

#count()

ejem5 = "hay sus, sus, sus, impostores"
count_1 = ejem5.count("sus")
count_2 = ejem5.count("sus", 10,30)

#encode()

ejem6 = "solo se que Ståle"
encode_1 = ejem6.encode(encoding='ascii',errors="ignore")
encode_2 = ejem6.encode(encoding='ascii',errors="backslashreplace")
encode_3 = ejem6.encode(encoding='ascii',errors="namereplace")
encode_4 = ejem6.encode(encoding='ascii',errors="replace")
encode_5 = ejem6.encode(encoding='ascii',errors="xmlcharrefreplace")
encode_6 = ejem6.encode(encoding='ascii',errors="strict")
#Textos
sep = '''------------------------------------------------------------------------------------------------------------'''
text1 = '''Se veran todos los metodos ('method') y su descripcion de usos
        se veran alguno que quizas son similares pero pues es bueno aprenderlos'''
met_ex1 = '''Capitalize() hace convertir el primer caracter en mayusculas'''
met1 = """su estructura es el siguiente "string.capitalize()" """
met_ex2 = """Converte en minusculas y es mas agresivos que lower"""
met2 = """su estructura es "string.casefold()" """
met_ex3 = """ Es te es CENTER el cual centrara el texto"""
met3 = """Estructura String.center(longitud, caracter que quieras incluir(opcional))"""
met_ex4 = """Count() Sirve para detectar y dicer cuantas variables que se buscan hay en el String"""
met4 = """Estructura: String.Count(Value, star, end) los dos ultimos son opcionales"""
met_ex5 = """enconde() Especifica la codificacion del string que no reconoce"""
met5 = """ Su estructura es String.encode(encoding='encoding',errors='errors'), en la seccion de los errores se puede usar los siguientes
        -'backslashreplace':
                Usa un slash inverso para reeemplazar el caracter que no puede codificar
        -'ignore':
                Ignora el caracter que no puede codificar
        -'namereplace':
                Reemplaza el caracter describiendo a como es la letra codificada
        -'replace'
                Reemplaza por un simbolo de interrogación
        -'xmlcharrefreplace':
                Reemplaza con un xml caracer el codificado
        -'strict':
                default response which raises a UnicodeDecodeError exception on failure"""
print(sep)
print(text1)
print(sep)
print(met_ex1)
print()
print(met1)
print()
print(cap1)
print()
print("En este ejemplo pondra las mayusculas como 'HOLA' a 'Hola' " )
print(cap2)
print()
print(cap3)
print(sep)
print(met_ex2)
print()
print(met2)
print()
print(fold)
print(sep)
print(met_ex3)
print()
print(met3)
print()
print("Este ejemplo es solo con length")
print(cent)
print()
print("Este ejemplo es con un caracter como relleno")
print(cent2)
print(sep)
print()
print(met_ex4)
print()
print(met4)
print()
print(met_ex5)
print()
print(met5)
print()
print(encode_1)
print()
print(encode_2)
print()
print(encode_3)
print()
print(encode_4)
print()
print(encode_5)