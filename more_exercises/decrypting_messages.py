key = int(input())
number_of_lines = int(input())

new_letter = ""


for i in range(number_of_lines):
    input_letter = input()
    order = ord(input_letter)
    new_letter = chr(key + order)

    print(f"{new_letter}", end="")