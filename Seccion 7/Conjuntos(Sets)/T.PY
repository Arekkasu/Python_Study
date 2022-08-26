listado_a = str(input()).split()
listado_b = str(input()).split()
listado_a = set(listado_a)
listado_b = set(listado_b)

palabras_compartidas = print(len(listado_a & listado_b))
palabras_unicas = print(len(listado_a ^ listado_b))