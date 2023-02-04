input_line = [int(j) for j in input().split(", ")]

for i in input_line:
    if i == 0:
        input_line.remove(i)
        input_line.append(i)


print(input_line)





