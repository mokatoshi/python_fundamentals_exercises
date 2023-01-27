decoration_quantity = int(input())
days_left = int(input())

total_costs = 0
spirit_points = 0

for i in range(1, days_left + 1):

    if i % 11 == 0:
        decoration_quantity = (decoration_quantity + 2)

    if i % 2 == 0:
        total_costs += (2 * decoration_quantity)
        spirit_points += 5
    if i % 3 == 0:
        total_costs += (8 * decoration_quantity)
        spirit_points += 13
    if i % 5 == 0:
        total_costs += (15 * decoration_quantity)
        spirit_points += 17
    if i % 3 == 0 and i % 5 == 0:
        spirit_points += 30

    if i % 10 == 0:
        spirit_points -= 20
        total_costs = total_costs + 23

if days_left % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {total_costs}")
print(f"Total spirit: {spirit_points}")
