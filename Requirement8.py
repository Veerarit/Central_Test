# Requirement 8

def greet8(name1, name2):
    name2 = name2.replace('\"', '')
    new_var = name2.split(', ')
    print(f'Hello, {name1} and {new_var[0]}, {new_var[1]}.')


greet8('Bob', "\"Charlie, Dianne\"")
