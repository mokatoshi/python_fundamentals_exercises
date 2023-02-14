rooms = int(input())

chairs_needed = 0
chairs_left = 0
game_on = True

for room in range(1, rooms + 1):
    chars, guests_as_string = input().split(" ")
    guests = int(guests_as_string)
    if guests > len(chars):
        chairs_needed = guests - len(chars)
        print(f"{chairs_needed} more chairs needed in room {room}")
        game_on = False
    else:
        current_row = len(chars) - guests
        chairs_left += current_row

if game_on:
    print(f"Game On, {chairs_left} free chairs left")
