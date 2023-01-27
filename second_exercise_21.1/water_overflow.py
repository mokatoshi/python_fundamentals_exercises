number_of_lines = int(input())

capacity = 255
tank = 0
for i in range(1, number_of_lines + 1):
    input_liters = int(input())

    if tank + input_liters > capacity:
        print("Insufficient capacity!")
    else:
        tank += input_liters

print(tank)