titulo = 'Curso profesional de Python'

print('profesional' in titulo.lower())

# Imprime la cantidad de veces que aparece palabra en string
print(titulo.count('Curso'))

print(titulo.startswith('c'))

print(titulo.endswith('hon'))

print(titulo.find('p'))
# Eliminar espacios del inicio y fin
print(titulo.strip())

print('6'.isnumeric())