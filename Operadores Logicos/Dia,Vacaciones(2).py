#Se hace con el mismo ejercicio solo que se agregara if *NOT*
Vacaciones = False
Descanso = False
#Practicamente se cambiaria la formula, en ves de saber si tiene x varaibles, va mirar si no las tiene, osea si es un false lo vera como true
if not (Vacaciones or Descanso):
    print('No puedes ir, tienes deberes')
else:    
    print('Puedes Ir')