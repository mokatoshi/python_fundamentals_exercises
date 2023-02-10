# def is_even(numbers):
#     result = numbers % 2 == 0
#     return result
#
#
# input_numbers = input().split()
#
# nums_as_int = []
# for nums in input_numbers:
#     digit = int(nums)
#     nums_as_int.append(digit)
#
#
# print(list(filter(is_even, nums_as_int)))


def is_even(numbers):
    result = numbers % 2 == 0
    return result


nums_as_int = [int(x) for x in input().split()]

print(list(filter(is_even, nums_as_int)))
