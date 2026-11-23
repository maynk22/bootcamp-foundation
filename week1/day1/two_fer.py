def two_fer():
    name = input("Enter name : ")
    if len(name) == 0:
        print("One for you, one for me.")
    else:
        print(f"One for {name}, one for me.")

two_fer()