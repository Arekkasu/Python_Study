#---------------------------------------Textos-----------------------------------
title = """Booleans"""
txt = """Comandos que entregan 2 valores, sean este positivo o negativo."""
Evalue = """Para Evaluar valores se usa 'bool()' el cual puede registrar
        - Strings
        - Numeros"""
Values = '''Tambien poner valores mayores que uno, dara como True'''
Zero = '''Si no hay valores o se presenta el 0, este dara False'''
Functions = '''Las funciones tambien puede dar True o False'''
isinstance_ = '''Isisntsance() tiene como funcion para utilizarse si un objeto es de un determinado tipo de datos'''
sep = '''------------------------------------------------------------------------------------------------------------'''

#-------------------------------------Variables-----------------------------------

    #Ejemplo Bool
Bool = '''Ej_1 = 10
        Ej_1_1 = 40
        Result = Ej_1 > Ej_1_1'''
Ej_1 = 10
Ej_1_1 = 40
Result = Ej_1 > Ej_1_1

    #bool()

values = '''
Ej_2 = 'Hola'
Ej_2_1 = 55
'''
Ej_2 = 'Hola'
Ej_2_1 = 55

        #Valores Vacios

Void = '''
zero = bool(False)
zero_1 = bool(None)
zero_2 = bool(0)
zero_3 = bool("")
zero_4 = bool(())
zero_5 = bool([])
zero_6 = bool({})
'''

zero = bool(False)
zero_1 = bool(None)
zero_2 = bool(0)
zero_3 = bool("")
zero_4 = bool(())
zero_5 = bool([])
zero_6 = bool({})
    #Func y Condicionales
Con = '''    
    a = 440
    b = 40*11
    if a == 2:
        print('lo son')
    else:
        print('No lo son')
'''
func = '''
    def funcion():
    return True'''
def Comparate():
    a = 440
    b = 40*11
    if a == 2:
        print('lo son')
    else:
        print('No lo son')
    #Esto seria True

def funcion():
    return True

    #Isistance()
isis = '''X = 222'''
X = 222
#-------------------------------------------------------------------------------
print(title.center(100, "="))
print()
print(txt)
print()
print(Bool)
print()
print(sep)
print()
print(Evalue)
print()
print(values)
print()
print(Values)
print()
print(bool(Ej_2))
print()
print(bool(Ej_2_1))
print()
print()
print(Zero)
print()
print(Void)
print()
print(zero)
print()
print(zero_1)
print()
print(zero_2)
print()
print(zero_3)
print()
print(zero_4)
print()
print(zero_5)
print()
print(zero_6)
print()
print(sep)
print()
print(Functions)
print()
print(Con)
print()
print(Comparate())
print()
print(func)
print()
print(funcion())
print()
print(sep)
print()
print(isinstance_)
print()
print(isis)
print()
print(isinstance(X, int))