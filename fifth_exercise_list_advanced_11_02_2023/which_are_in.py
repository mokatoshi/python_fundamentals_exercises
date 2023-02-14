first_line = input().split(", ")
second_line = input().split(", ")

new_list = []

for substring in first_line:
    for word in second_line:
        if substring in word:
            new_list.append(substring)
            break

print(new_list)

