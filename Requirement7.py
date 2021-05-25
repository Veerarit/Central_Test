# Requirement 7

def greet7(name1, name2):
    new_var = name2.split(', ')
    print(f'Hello, {name1}, {new_var[0]}, and {new_var[1]}.')


greet7('Bob', 'Charlie, Dianne')
