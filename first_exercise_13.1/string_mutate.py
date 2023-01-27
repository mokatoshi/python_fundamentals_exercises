string_one = input()
string_two = input()

result = string_one

for idx in range(len(string_one)):
    if string_one[idx] == string_two[idx]:
        continue

    result = string_two[:idx + 1] + string_one[idx + 1:]
    print(result)