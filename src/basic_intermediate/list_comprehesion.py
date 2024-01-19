# List Comprehesion

# Crear listas

my_list = [i for i in range(1, 11)]
print(my_list)

# Lista de número elevados al cuadrado
my_number_list_squares = [i ** 2 for i in range(1, 11)]
print(my_number_list_squares)

# Aplicando condicionales
# Lista de pares a partir de otra lista
my_number_list_even = [i for i in my_number_list_squares if i % 2 == 0]
print(my_number_list_even)

# Usando dict comprehesion

my_dict = [{i: f'dict{i}'} for i in range(1, 11)]
print(my_dict)

# Obteniendo un dict

my_dict_2 = {i: f'dict{i}' for i in range(1, 11)}
print(my_dict_2)
