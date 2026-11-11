def name_age_printer():
    name = input('mention name : ')
    age = int(input('mention age : '))
    if age.is_integer():
        print(f'Your name is {name} and your age is {age}')
    else:
        print("Age should be a number.")

name_age_printer()