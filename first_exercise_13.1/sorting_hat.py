while True:

    input_name = input()

    if input_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif input_name == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(input_name) < 5:
        print(f"{input_name} goes to Gryffindor.")
    elif len(input_name) == 5:
        print(f"{input_name} goes to Slytherin.")
    elif len(input_name) == 6:
        print(f"{input_name} goes to Ravenclaw.")
    elif len(input_name) > 6:
        print(f"{input_name} goes to Hufflepuff.")