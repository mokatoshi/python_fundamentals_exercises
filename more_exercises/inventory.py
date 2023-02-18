items_journal = input().split(", ")


while True:
    input_command = input()

    if input_command == "Craft!":
        break

    input_args = input_command.split(" - ")
    action = input_args[0]
    item = input_args[1]

    if action == "Collect":
        if item not in items_journal:
            items_journal.append(item)

    elif action == "Drop":
        if item in items_journal:
            items_journal.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items_journal:
            old_item_index = items_journal.index(old_item)
            items_journal.insert(old_item_index + 1, new_item)

    elif action == "Renew":
        if item in items_journal:
            items_journal.remove(item)
            items_journal.append(item)


print(* items_journal, sep=", ")



