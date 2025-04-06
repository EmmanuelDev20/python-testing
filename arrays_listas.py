
# """
# Listas en Python
# Tipo list
# <variable> = []
# """

# my_list = ["String", 10, 3.14, True, ["String", 10, 3.14, True]]
# print(my_list)
# print(type(my_list))

# courses = ['History', 'Math', 'Physics', 'CompSci']
# numbers = [1, 5, 2, 4, 3]

# print(courses[2]) # Physics
# print(courses[-1]) # CompSci
# print(courses[0:2]) # ['History', 'Math']
# print(courses[:2]) # ['History', 'Math'] Es igual a 0:2
# print(courses[2:]) # ['Physics', 'CompSci']
# print(courses[1:]) # ['Math', 'Physics', 'CompSci'] 

# print(len(courses))

# Reemplazar valores
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses[0] = 'Art'

# Sublista
# courses = ['History', 'Math', 'Physics', 'CompSci', 'Art']
# sub_courses = [
#   courses[0],
#   courses[1],
#   courses[2]
# ]

# sub_courses = courses[0:3]
# sub_courses = courses[:]
# sub_courses = courses[::2] # Saltos de 2 en 2
# sub_courses = courses[::-1] # Dar la vuelta a la lista

# print(sub_courses)

# Agregar elementos
# courses.append('Art new') # Agrega al final

# courses.insert(2, 'Art new position') # Agrega en una posición específica

# print(courses)

# new_courses = ['React', 'Angular']
# courses.extend(new_courses) # Agrega una lista a otra lista

# print("Python" in courses) # False
# print("Math" in courses) # True
# print(courses.index('Math')) # 1 Si error falla, nos devuelve error

# courses.remove('Math') # Elimina un elemento de la lista
# courses.pop() # Elimina el último elemento de la lista
# courses.pop(0) # Elimina el elemento en la posición 0
# last_element = courses.pop() # Elimina el último elemento y lo guarda en una variable

# courses.clear() # Elimina todos los elementos de la lista

# # copy, reverse, sort
# courses = ['History', 'Math', 'Physics', 'CompSci']
# courses2 = courses.copy() # Es igual a courses[:]
# courses.reverse() # AL USAR ESTO SE MODIFICA LA LISTA ORIGINAL, CON SLICING NO courses[::-1] 
# courses.sort() # Ordena la lista
# courses.sort(reverse=True) # Ordena la lista de forma inversa

# matrix = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# print(matrix[0][2])



# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4] + numbers[5] + numbers[6] + numbers[7] + numbers[8])

# Lista de strings de carros con longitud de 10
# carros = ['Toyota', 'Nissan', 'Ford', 'Volkswagen', 'Chevrolet', 'Mitsubishi', 'Hyundai', 'Kia', 'Mazda', 'Mercedes']
# # Genera una sub lista con los 3 primeros y últimos elementos
# sub_carros = carros[:3]
# sub_carros.extend(carros[-3:])
# # sub_carros = carros[:3], carros[-3:]

# print(sub_carros)

#Evaluar si el primer elemento de cada fila es un número par
# for row in matrix:
#   if row[0] % 2 == 0:
#     print(row[0])
