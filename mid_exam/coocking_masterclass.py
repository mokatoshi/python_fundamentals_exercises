from math import ceil

budget = float(input())
students = int(input())
one_flour = float(input())
one_egg = float(input())
one_apron = float(input())

total_item_cost = 0
free_flour = 0


for flours in range(1, students + 1):
    if flours % 5 == 0:
        free_flour += 1

total_flour_cost = (students * one_flour) - (free_flour * one_flour)
total_aprons_cost = (ceil(students * 1.2) * one_apron)
total_eggs = students * one_egg * 10

total_item_cost = total_aprons_cost + total_flour_cost + total_eggs

if total_item_cost <= budget:
    print(f"Items purchased for {total_item_cost:.2f}$.")
else:
    print(f"{abs(budget - total_item_cost):.2f}$ more needed.")
