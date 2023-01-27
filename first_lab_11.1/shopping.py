budget = int(input())

command_line = input()

while command_line != "End":
    price = int(command_line)
    budget -= price

    if budget < 0:
        print("You went in overdraft!")
        break
    command_line = input()
else:
    print("You bought everything needed.")