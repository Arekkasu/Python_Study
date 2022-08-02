# -------Titulo------

Tittle = 'Calculadora de Area y Perimetro de un Rectangulo'

# -----------------------------------------------------------
print(Tittle.center(100, '='))
# ------Operaciones------

Alto = int(input("Ingrese el alto del Rectangulo: "))
Ancho = int(input("Ingrese el ancho del Rectangulo: "))
Area = Alto*Ancho
Perimetro = (Ancho+Area)*2

# -----------------------------
print()
print('El Area es: ', Area)
print()
print('El Perimetro es: ', Perimetro)