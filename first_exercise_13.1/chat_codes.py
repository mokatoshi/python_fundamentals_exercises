n = int(input())

for i in range(n):
    input_number = int(input())
    if input_number < 88:
        if input_number != 86:
            print("GREAT!")
        elif input_number == 86:
            print("How are you?")
    elif input_number == 88:
        print("Hello")
    elif input_number > 88:
        print("Bye.")