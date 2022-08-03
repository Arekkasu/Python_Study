multiplicador = 15
for i in range(11):
    resultado = multiplicador*i
    salida = f'{multiplicador} x {i}:\t {resultado}'
    txt = salida.expandtabs(5)
    print(txt)