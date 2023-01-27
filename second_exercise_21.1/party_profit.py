group_size = int(input())
days = int(input())

coins_total = 0
coins_per_member = 0

for i in range(1, days + 1):

    coins_total += 50

    if i % 15 == 0:
        group_size += 5

    if i % 10 == 0:
        group_size -= 2

    coins_total = coins_total - (group_size * 2)

    if i % 5 == 0:
        coins_total = coins_total + (20 * group_size)

    if i % 3 == 0:
        coins_total = coins_total - (group_size * 3)

    if i % 3 == 0 and i % 5 == 0:
        coins_total = coins_total - (2 * group_size)

coins_per_member = coins_total // group_size

print(f"{group_size} companions received {coins_per_member} coins each.")