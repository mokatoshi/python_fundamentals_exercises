input_number = int(input())


if input_number == 1:
    print("False")
elif input_number > 1:
    for i in range(2, input_number//2 + 1):
        if input_number % i == 0:
            print("False")
            break
    else:
        print("True")

