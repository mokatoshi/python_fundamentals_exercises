dungeons_rooms = input().split("|")

MAX_HEALTH = 100
health = 100
bitcoins = 0
room_number = 0
is_alive = True

for rooms in dungeons_rooms:
    room_number += 1
    command, amount = rooms.split()
    amount = int(amount)

    if command == "potion":
        if health + amount > MAX_HEALTH:
            print(f"You healed for {MAX_HEALTH-health} hp.")
            health = MAX_HEALTH
        else:
            print(f"You healed for {amount} hp.")
            health += amount
        print(f'Current health: {health} hp.')
    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    elif command != "potion" or command != "chest":
        health -= amount
        if not health <= 0:
            print(f"You slayed {command}.")
        else:
            is_alive = False
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_number}")
            exit(0)
if is_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
