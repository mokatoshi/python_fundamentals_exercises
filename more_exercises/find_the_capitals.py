input_string = input()

res = [idx for idx in range(len(input_string)) if input_string[idx].isupper()]

print(str(res))
