random_number = int(input())

word = input()
word_list = []
list_of_strings = []

for _ in range(random_number):

    current_string = input()
    list_of_strings.append((current_string))

    if word in current_string:
        word_list.append(current_string)

print(list_of_strings)
print(word_list)
