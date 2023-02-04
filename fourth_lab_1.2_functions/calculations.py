operator_code = input()
first_num = int(input())
second_num = int(input())


def solution(a, b, operator):

    result = None

    if operator_code == "multiply":
        result = a * b
    elif operator_code == "divide":
        result = a // b
    elif operator_code == "add":
        result = a + b
    elif operator_code == "subtract":
        result = a - b
    return result


print(solution(first_num, second_num, operator_code))
