input_line = input().split()
text = list(input())

new_word = ''

for i in range(len(input_line)):
    sum_of_digits = 0
    for number in input_line[i]:
        digit = int(number)
        sum_of_digits += digit
    if sum_of_digits > len(text) - 1:
        new_index = sum_of_digits % len(text)
        new_word += text[new_index]
        text.pop(new_index)
    else:
        new_word += text[sum_of_digits]
        text.pop(sum_of_digits)
print(new_word)
