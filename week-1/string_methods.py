def string_function():
    string = input("Enter String : ")
    str_split = string.split('|')
    str_strip = string.strip()
    str_upper = string.upper()

    print(f"{str_split} \n {str_strip} \n {str_upper}")

string_function()