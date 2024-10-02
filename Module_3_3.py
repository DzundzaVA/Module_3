def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print()

values_list = ['Text', 3, 5.4]
values_dict = {'a': 1, 'b': False, 'c': 'Word'}

print_params(*values_list)
print_params(**values_dict)
print()

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)