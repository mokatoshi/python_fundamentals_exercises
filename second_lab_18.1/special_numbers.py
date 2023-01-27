n = int(input())

for num in range(1, n + 1):
    is_special = False
    num_as_string = str(num)
    digit_sum = 0
    for char in num_as_string:
        digit_sum += int(char)

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        is_special = True
        print(f"{num} -> {is_special}")
    else:
        print(f"{num} -> {False}")