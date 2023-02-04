random_input = input().split()

converted_numbers = []

for i in random_input:
    converted_numbers.append(abs(float(i)))

print(converted_numbers)
