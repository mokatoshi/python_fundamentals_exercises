from math import ceil

sequence_of_numbers = input().split(", ")

sequence_as_digits = [int(num) for num in sequence_of_numbers]

low_level = 1
high_level = 10

groups_count = ceil((max(sequence_as_digits) / 10))

for num in range(low_level, groups_count + 1):
    filtered_nums = [x for x in sequence_as_digits if low_level <= x <= high_level]
    print(f"Group of {10 * num}'s: {filtered_nums}")
    low_level += 10
    high_level += 10


