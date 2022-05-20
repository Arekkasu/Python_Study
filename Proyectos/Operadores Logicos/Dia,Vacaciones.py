Vacaciones = str(input('Vacaciones?: '))
Descanso = str(input('dias de descanso?: '))
#Operador Or
if Vacaciones == 'y' or Descanso == 'y':
    print('Puedes ir')
elif Vacaciones == 'n' or Descanso == 'n':
    print('No puedes ir')
else:
    print('mal')