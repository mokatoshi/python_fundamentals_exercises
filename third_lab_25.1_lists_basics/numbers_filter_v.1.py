random_number = int(input())

list_of_num = []
filtered = []

for i in range(random_number):

    current_number = int(input())
    list_of_num.append(current_number)

command_line = input()

if command_line == "even":
    for element in list_of_num:
        if element % 2 == 0:
            filtered.append(element)
elif command_line == "odd":
    for element in list_of_num:
        if element % 2 != 0:
            filtered.append(element)
elif command_line == "positive":
    for element in list_of_num:
        if element >= 0:
            filtered.append(element)
elif command_line == "negative":
    for element in list_of_num:
        if element < 0:
            filtered.append(element)

print(filtered)
