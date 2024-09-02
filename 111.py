def print_params(a=1, b='строка', c=True):
 print(a, b, c)
print_params()
print_params(5)
print_params(1, "новая строка")
print_params(8, "новая строка", False)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [2, "другая строка", False]
values_dict = {"a": 3, "b": "еще одна строка", "c": True}
print_params(*values_list)
print_params(*values_dict)
values_list_2 = [23, "еще еще одна строка"]
print_params(*values_list_2, 42)