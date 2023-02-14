wagons_count = int(input())
wagons = [0] * wagons_count

command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
        num_people: int = int(command.split()[1])
        wagons[-1] += num_people
    elif action == "insert":
        num_people = int(command.split()[2])
        given_wagon = int(command.split()[1])
        wagons[given_wagon] += num_people
    elif action == "leave":
        given_wagon = int(command.split()[1])
        num_people = int(command.split()[2])
        wagons[given_wagon] = wagons[given_wagon] - num_people
    command = input()

print(wagons)





