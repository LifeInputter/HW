def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(a=1, b='string', c=False)
print_params(c=False)
# print_params(a, b, c='strong')  # Expected type 'bool', got 'str' instead
# print_params(a, b, c)  # Unresolved reference
# print_params(b)  # Unresolved reference
# print_params(b=25)  # Expected type 'str', got 'int' instead
# print_params(c=[1, 2, 3])  # Expected type 'bool', got 'list[int]' instead

values_list = [2, 'string is strong', True]
values_dict = {'a': 1, 'b': 'string', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'bananas']
print_params(*values_list_2, 42)
print_params(42, *values_list_2)
