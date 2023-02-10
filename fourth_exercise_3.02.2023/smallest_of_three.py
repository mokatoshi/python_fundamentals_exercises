def smallest_num(list_of_num):
    min_number = float("inf")
    for num in list_of_num:
        if num < min_number:
            min_number = num

    return min_number


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_num([first_num, second_num, third_num]))


