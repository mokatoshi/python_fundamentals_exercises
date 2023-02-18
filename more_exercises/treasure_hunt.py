def is_valid_index(index, give_list):
    if 0 <= index <= len(give_list):
        return True


initial_loot = input().split("|")

loot_items = []


while True:
    loot_items.clear()
    new_commands = input()
    if new_commands == "Yohoho!":
        break

    commands_args = new_commands.split(" ")
    command = commands_args[0]

    if command == "Loot":
        for commands in range(1, len(commands_args)):
            loot_items.append(commands_args[commands])
        for item in loot_items:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command == "Drop":
        remove_el = int(commands_args[1])
        if not is_valid_index(remove_el, initial_loot):
            continue
        else:
            initial_loot.append(initial_loot[remove_el])
            initial_loot.pop(remove_el)
    elif command == "Steal":
        stolen_items = int(commands_args[1])
        items_stolen = []
        if stolen_items >= len(initial_loot):
            items_stolen = initial_loot.copy()
        else:
            idx = (len(initial_loot)) - stolen_items
            for i in range(idx, len(initial_loot)):
                items_stolen.append(initial_loot[i])

        for el in items_stolen:
            initial_loot.remove(el)
        print(*items_stolen, sep=", ")

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    treasure_gain = (sum(len(x) for x in initial_loot)) / len(initial_loot)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")

