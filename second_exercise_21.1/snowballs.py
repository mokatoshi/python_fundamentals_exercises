number_of_balls = int(input())

max_value = 0
outcome = ""

for i in range(1, number_of_balls + 1):

    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > max_value:
        max_value = value
        outcome = f"{weight} : {time} = {value:.0f} ({quality})"

print(outcome)
