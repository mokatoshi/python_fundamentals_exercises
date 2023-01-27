number_of_letters = int(input())

total_sum = 0

for i in range(1, number_of_letters + 1):
    input_line = input()
    number = ord(input_line)
    total_sum += number
print(f"The sum equals: {total_sum}")
