def add_and_subtract(a, b, c):
    sum_result = add_function(first_num, second_num)
    result = subtract(sum_result, third_num)
    return result


def add_function(a, b):
    return a + b


def subtract(a, b):
    return a - b


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
