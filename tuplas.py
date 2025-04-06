# Son inmutables
# # settings = ("localhost", 3306, True)

# # print(settings[0])
# # print(type(settings))

# # # Desempaquetado de tuplas
# # host, port, active = settings
# # print(host)
# # print(port)
# # print(active)

# # numbers = 1,
# # # numbers = 1, 2, 3, 4, 5
# # print(numbers)
# # print(type(numbers))

# # # Ignorar elementos 
# # host, _, _ = settings
# # print(host)

# # # Agrupacion de tuplas 
# # var1, var2, *var3 = 1, 2, 3, 4, 5
# # print(var1) #1
# # print(var2) #2
# # print(var3) #[3, 4, 5]

# # var1, var2, *var3, var4 = 1, 2, 3, 4, 5
# # print(var1) #1
# # print(var2) #2
# # print(var3) #[3, 4]
# # print(var4) #5

# # var1, var2, *var3, _, var4 = 1, 2, 3, 4, 5

# # # Funcion zip
# # users = ["Juan", "Pedro", "Maria"]

# # courses = ("Python", "Java", "C#")

# # # response = list(zip(users, courses))
# # response = tuple(zip(users, courses))
# # print(response)

# Funciones de tuplas
numbers = (1, 4, 5, 3, 3, 7, 2, 10)

# print(len(numbers)) # 8
# print(max(numbers)) # 10
# print(min(numbers)) # 1
# print(sum(numbers)) # 35
# print(sorted(numbers)) # [1, 2, 3, 3, 4, 5, 7, 10]
# print(sorted(numbers, reverse=True)) # [10, 7, 5, 4, 3, 3, 2, 1]
# print(numbers.count(3)) # 2
# print(numbers.index(3)) # 2
# print(numbers.index(3, 3)) # 4
# print(numbers.index(3, 4)) # Error
# print(numbers.count(3)) # 2
# print(numbers.index(3)) # 2
print(3 in numbers) # True or False