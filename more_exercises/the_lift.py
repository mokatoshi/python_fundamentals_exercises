waiting_people = int(input())

initial_people = waiting_people
availability = [int(x) for x in input().split(" ")]
max_capacity = 4

for current_lift in range(len(availability)):
    max_people = min(max_capacity - availability[current_lift], waiting_people)
    availability[current_lift] += max_people
    waiting_people -= max_people

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")

elif len([lift for lift in availability if lift < 4]) > 0:
    print("The lift has empty spots!")


print(" ".join([str(wagon) for wagon in availability]))

