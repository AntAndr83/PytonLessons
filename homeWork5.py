def func(var_a, var_b):
    if type(var_a) is str or type(var_b) is str:
        return 'str'
    elif var_a > var_b:
        return '>'
    elif var_a == var_b:
        return '='
    elif var_a < var_b:
        return '<'
print(func(var_a, var_b))
