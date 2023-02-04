factor_number = int(input())
count_number = int(input())
new_list = []

for i in range(1, count_number + 1):
    new_list.append(factor_number * i)

print(new_list)
