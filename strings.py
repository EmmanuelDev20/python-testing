# Son de solo lectura

# message = 'Hola mundo!'

# print(message[0])
# print(type(message))
# print(len(message))
# print(max(message))

# split -> lista

# courses = 'Python PHP Mongo React'
# list_courses = courses.split(' ')

# join -> string a partir de lista
# print(list_courses)
# string_course = ', '.join(list_courses)

# print(string_course)

name = 'Emmanuel'
last_name = 'Ovares'

# 1. Unir texto
# full_name = name + last_name + str(30) + 'anos'

# 2. Unir texto
# full_name = ' '.join([name, last_name])

# 3. Unir texto
# full_name = 'El nombre completo es: %s %s y tiene 30 anhos' %(name, last_name)

# # 4. Unir texto format
# base = 'El nombre completo es: {} {}'
# full_name = base.format(name, last_name)

# # Format con nombres
# base = 'El nombre completo es: {name} {last_name}'
# full_name = base.format(
#   name=name,
#   last_name=last_name,
#   age=30
# )

# print(full_name)

# name = input('Ingresa tu nombre')
# last_name = input('Ingresa tu apellido')
# age = input('Ingresa tu edad')

# # full_name = base.format(name, last_name, age)
# print(full_name)

# 5. Unir texto f string
full_name = f'Hola {name}, este es tu apellido {last_name}'
print(full_name)