# list_of_numbers = input().split()
# removed_count = int(input())
#
# digits = []
# string_numbers = []
#
# for i in list_of_numbers:
#     digits.append(int(i))
#
# for min_number in range(removed_count):
#     min_num = min(digits)
#     digits.remove(min_num)
#
#
# for j in digits:
#     str_num = str(j)
#     string_numbers.append(str_num)
#
# print(", ".join(string_numbers))




list_of_numbers = input().split()
removed_count = int(input())

digits = []


for i in list_of_numbers:
    digits.append(int(i))

for min_number in range(removed_count):
    min_num = min(digits)
    digits.remove(min_num)


string_number = map(str, digits)

print(", ".join(string_number))




