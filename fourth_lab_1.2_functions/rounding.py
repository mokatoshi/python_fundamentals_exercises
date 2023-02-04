random_numbers = input().split()

new_nums = []

for nums in random_numbers:
    new_nums.append(round(float(nums)))


print(new_nums)