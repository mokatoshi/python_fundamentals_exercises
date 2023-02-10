def odd_and_even_sum(num_as_string):
    even_sum = 0
    odd_sum = 0

    for digits_check in num_as_string:
        digit = int(digits_check)
        if digit % 2 == 0:
            even_sum += digit
        elif digit % 2 != 0:
            odd_sum += digit
    return [odd_sum, even_sum]


given_number = input()

result = odd_and_even_sum(given_number)
print(f'Odd sum = {result[0]}, Even sum = {result[1]}')


