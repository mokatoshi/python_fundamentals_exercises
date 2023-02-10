def perfect_number(number):

    sum_of_divisors = 0
    for digit in range(1, number + 1):
        if digit > 0:
            if number % digit == 0:
                sum_of_divisors += digit

    if sum_of_divisors // 2 == input_number:
        is_number_perfect = True
    else:
        is_number_perfect = False

    return is_number_perfect


is_perfect = False
input_number = int(input())

if perfect_number(input_number):
    is_perfect = True
    print("We have a perfect number!")
else:
    print(f"It's not so perfect.")





#
# input_number = int(input())
#
# sum_of_divisors = 0
#
#
# for digit in range(1, input_number + 1):
#     if digit > 0:
#         if input_number % digit == 0:
#             sum_of_divisors += digit
#
# if sum_of_divisors // 2 == input_number:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")