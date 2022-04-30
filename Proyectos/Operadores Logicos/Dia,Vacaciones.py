Y = bool(1)
N = bool(0)

Vacaciones = str(input('Vacaciones?: '))
Descanso = str(input('dias de descanso?: '))
print(Y)
print(N)
#Operador Or
if Vacaciones:
    print('Puede ir')

elif Descanso:
    print('Puede ir')
else:    
    print('No puedes ir, tienes deberes')