#------------------------Variables-----------------------------------------
    #isalnum()
ejem1 = "solo"
isal = ejem1.isalnum()
    #isalpha()
ejem2 = "Seguro3"
alpha = ejem2.isalpha()
    #isdecimal()
ejem3 = "\u0033"
deci = ejem3.isdecimal()
    #isdigit()
ejem4 = "3492"
digit = ejem4.isdigit()
    #isidentifier()
ejem5 = "Company_security33"
identifi = ejem5.isidentifier()
#------------------------Textos--------------------------------------------
Intro = "String pt3"
met_ex1 = "isalnum() dice si es alfanumerico el string"
met1 = "Su estructura es string.isalnum(), lo cual reconocera si tiene letras o numeros, pero si contiene espacios o simbolos, dara False"
met_ex2 = "isalpha() dice si el string es alfabetico"
met2 = "Su estructura es string.isalpha() te dira true si solo son letrar, pero dira false si tiene numeros o espacion etc"
met_ex3 = "isdecimal() dice si decimal el string"
met3 = "Su estructura es string.isdecimal(), lo cual leera numeros y solo Unicode"
met_ex4 = "isdigit() dice si lo que contiene el string es un digito"
met4 = "su estructura es String.isdigit() detecta numeros,decimales y tambien potencias como ²"
met_ex5 = "isidentifier() dice si tiene letras, numeros o guiones bajo"
met5 = "Su estructura es String.isidentifier(), pero, no puede iniciar con numero o tener espacios"
separador = '''----------------------------------------------------------------------------------------------------'''
#------------------------------------------------------------------------------------------------------------------
print(Intro.center(100, "-"))
print()
print(met_ex1)
print()
print(met1)
print()
print(isal)
print(separador)
print()
print(met_ex2)
print()
print(met2)
print()
print(alpha)
print()
print(separador)
print()
print(met_ex3)
print()
print(met3)
print()
print(digit)
print()
print(separador)
print()
print(met_ex5)
print()
print(met5)
print()
print(identifi)