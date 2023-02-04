list_of_events = input().split("|")
energy = 100
total_coins = 100

bakery_open = True

for event in list_of_events:
    event_info = event.split("-")
    type_event = event_info[0]
    number = int(event_info[1])
    if type_event == "rest":
        temp_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - temp_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_event == "order":
        if energy >= 30:
            energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            if energy > 100:
                energy = 100
            print(f"You had to rest!")
    else:
        if total_coins >= number:
            total_coins -= number
            print(f"You bought {type_event}.")
        else:
            print(f"Closed! Cannot afford {type_event}.")
            bakery_open = False
            break

if bakery_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {energy}")
