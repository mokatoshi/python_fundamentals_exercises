shopping_list = input().split("!")

command = input()

while command != "Go Shopping!":
    arguments = command.split(" ")
    commands = arguments[0]
    item = arguments[1]

    if commands == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif commands == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
    elif commands == "Correct":
        new_product = arguments[2]
        if item in shopping_list:
            idx = shopping_list.index(item)
            shopping_list[idx] = new_product
    elif commands == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

print(*shopping_list, sep=", ")
