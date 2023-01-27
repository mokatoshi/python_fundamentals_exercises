random_number = int(input())

odd_list = []
even_list = []
positive_list = []
negative_list = []

for _ in range(random_number):

    current_number = int(input())

    if current_number % 2 == 0:
        even_list.append(current_number)
    elif current_number % 2 != 0:
        odd_list.append(current_number)

    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)

command = input()

if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
elif command == "negative":
    print(negative_list)
