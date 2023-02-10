def palindrome(random_input):
    result = ""
    for i in input_integers:
        if i == i[::-1]:
            print("True")
        else:
            print("False")
    return result


input_integers = input().split(", ")

print(palindrome(input_integers))
