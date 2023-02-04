random_nums_as_string = input().split(", ")
beggars = int(input())

final_list = []
counter_of_index = 0
sum_list_as_digits = []

for element in random_nums_as_string:
    sum_list_as_digits.append(int(element))

while counter_of_index < beggars:
    current_beggar_sum = 0
    for current_index in range(counter_of_index, len(sum_list_as_digits), beggars):
        current_beggar_sum += sum_list_as_digits[current_index]
    counter_of_index += 1
    final_list.append(current_beggar_sum)

print(final_list)




