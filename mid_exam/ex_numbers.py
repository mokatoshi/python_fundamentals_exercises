numbers_sequence = [int(x) for x in input().split(" ")]


while True:
    input_seq = input()
    if input_seq == "Finish":
        break

    arguments = input_seq.split(" ")
    command = arguments[0]
    element = int(arguments[1])

    if command == "Add":
        numbers_sequence.append(element)

    elif command == "Remove":
        if element in numbers_sequence:
            numbers_sequence.remove(element)

    elif command == "Replace":
        element = int(arguments[1])
        new_element = int(arguments[2])
        if element in numbers_sequence:
            idx_old_element = numbers_sequence.index(element)
            numbers_sequence[idx_old_element] = new_element
    elif command == "Collapse":
        numbers_sequence = [num for num in numbers_sequence if num >= element]


print(* numbers_sequence, sep=" ")
