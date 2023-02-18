def is_idx_valid(f_idx, seq):
    return 0 <= f_idx < (len(seq))


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]

max_health = int(input())

is_running = True

while is_running:
    input_line = input()
    if input_line == "Retire":
        break

    cmd_arguments = input_line.split(" ")
    command = cmd_arguments[0]

    if command == "Fire":
        idx = int(cmd_arguments[1])
        damage = int(cmd_arguments[2])
        if not is_idx_valid(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_index = int(cmd_arguments[1])
        end_index = int(cmd_arguments[2])
        damage = int(cmd_arguments[3])
        if not is_idx_valid(start_index, pirate_ship) or not is_idx_valid(end_index, pirate_ship):
            continue
        for idx in range(start_index, end_index + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                is_running = False
                break
    elif command == "Repair":
        idx = int(cmd_arguments[1])
        health = int(cmd_arguments[2])
        if not is_idx_valid(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, (pirate_ship[idx] + health))

    elif command == "Status":
        minimum_health_allowed = max_health * 0.20
        counter_of_damaged_sections = 0
        for section in pirate_ship:
            if section < minimum_health_allowed:
                counter_of_damaged_sections += 1

        print(f"{counter_of_damaged_sections} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
