#--------------Variables------------------
    #Isupper()
ejem1 = "HOLA A TODOS"
upp = ejem1.isupper()
    #join
#Forma uno de hacer el separador
ejem2 = {"Name:" "John", "Country", "England"}
ejem2_1 = ("Hola", "Como", "Estas")
join_1 = "#".join(ejem2)
join_2 = " ".join(ejem2_1)
#forma dos de hacer el separador
Separador_1 = "X"
Separador_2 = " "
join_3 = Separador_1.join(ejem2)
join_4 = Separador_2.join(ejem2)
    #ljust()
ejem3 = "Banana"
x = ejem3.ljust(20, "p" )
y = "a mil pesos"
    #lower
ejem4 = "HOLA A TODOS"
lower = ejem4.lower()
    #lstrip()
ejem5 = "                     SUS                     "
strip = ejem5.lstrip()
ejem5_2 = "......lkkkkkasd`fiowjgiojsdigoj¡ifdhg¡DHola"
strip_2 = ejem5_2.lstrip(".lkasd`fiowjg¡")
    #Maketrans()
ejem6 = "Hola a todos"
Cambio = ejem6.maketrans("H", "S")
trans = Cambio
tradu = ejem6.translate(trans)
cambio_1 = "olHa"
cambio_2 = "pido"
trans_2 = ejem6.maketrans(cambio_1, cambio_2)
tradu_2 = ejem6.translate(trans_2)
#este borarrá
cambio_3 = "osd"
trans_3 = ejem6.maketrans(cambio_1, cambio_2, cambio_3)
tradu_3 = ejem6.translate(trans_3)
    #Partition()
ejem7 = "Se vender papayas a mil 500 pesos"
partition_1 = ejem7.partition("papayas")
partition_2 = ejem7.partition("agua")

#-------------Textos----------------------
Tittle = "String pt5"
met_ex1 = "isupper() es para detectar si el texto està en mayuscula"
met1 = "Su estructura String.isupper(), solo permite ALFABETICOS"
met_ex2 = "join() unir los itens en una cadena"
met2 = "su estructura es tring.join(iterable), lo cual se puede hace un separador"
met_ex3 = "ljust() alineara a la izquierda el string usando un caracter especificado que en este caso es el espacio para llenar"
met3 = "su estructura es string.ljust(length, character(opcional))"
met_ex4 = "lower() pone el string en minuscula"
met4 = "Su estructura es String.lower()"
met_ex5 = "lstrip() remueve los espacios de la izquierda"
met5 = "Su estructura es string.lstrip(characters) y su formato original es borrar el espacio"
met_ex6 = "Maketrans() se usa para reemplazar variables"
met6 = """Su estructura e String.Maketrans(x, y, z), se usa translate() para sustituir los valores especificados

    x Obligatorio. Si sólo se especifica un parámetro, éste tiene que ser un diccionario que describa cómo realizar el reemplazo. Si se especifican dos o más parámetros,
    este parámetro tiene que ser una cadena que especifique los caracteres que se quieren reemplazar.
    
    y Opcional. Una cadena con la misma longitud que el parámetro x.
    Cada carácter del primer parámetro se sustituirá por el carácter correspondiente de esta cadena.

    z Opcional. Una cadena que describa los caracteres que se van a eliminar de la cadena original.
"""
met_ex7 = """Partition() El método partition() busca una cadena especificada y la divide en una tupla que contiene tres elementos.
El primer elemento contiene la parte anterior a la cadena especificada.

El segundo elemento contiene la cadena especificada.

El tercer elemento contiene la parte posterior a la cadena.

Nota: Este método busca la primera aparición de la cadena especificada.
"""
met7 = "Su estructura es string.partition(value)"
separador = '''----------------------------------------------------------------------------------------------------'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
print(Tittle.center(100, "-"))
print()
print(met_ex1)
print()
print(met1)
print()
print(ejem1)
print()
print(upp)
print()
print(separador)
print()
print(met_ex2)
print()
print(met2)
print()
print(ejem2)
print()
print(join_1)
print()
print(ejem2_1)
print()
print(join_1)
print()
print(ejem2_1)
print()
print(join_2)
print()
print("""Esta es otra forma de hacer los separadores Separador_1 = "X"
Separador_2 = " "
join_3 = Separador_1.join(ejem2)
join_4 = Separador_2.join(ejem2)

""")
print()
print(join_3)
print()
print(join_4)
print()
print(separador)
print()
print(met_ex3)
print()
print(met3)
print()
print(x + y)
print()
print(separador)
print()
print(met_ex4)
print()
print(met_ex4)
print()
print(ejem4)
print()
print(lower)
print()
print(separador)
print()
print(met5)
print()
print(met_ex5)
print()
print(strip + "impostor")
print()
print("ahora veras como se puede borrar")
print()
print(strip_2 + "mundo")
print()
print(separador)
print()
print(met_ex6)
print()
print(met6)
print()
print("Si solo ponemos el maketrans sin el translate saldrà esto")
print(ejem6)
print()
print(Cambio)
print()
print("como ves sale en formato unicode, por eso es necesario usar el translate() que se verá mas adelante")
print()
print(trans)
print()
print(tradu)
print()
print(tradu_2)
print()
print("Este sirve para borrar")
print()
print(tradu_3)
print()
print(separador)
print()
print(met_ex7)
print()
print(met7)
print()
print("Este es el tuple" + ejem7)
print()
print("Si detecta el obejeto lo separará")
print()
print(partition_1)
print()
print("Si no lo encuentra, que en este caso sera 'agua' dejara espacio en blanco")
print()
print(partition_2)
print()
print(separador)
