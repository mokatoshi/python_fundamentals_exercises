def final_price(type_of_drink, quantity):
    result = 0
    if type_of_drink == "coffee":
        result = quantity * 1.50
    elif type_of_drink == "coke":
        result = quantity * 1.40
    elif type_of_drink == "water":
        result = quantity * 1.00
    elif type_of_drink == "snacks":
        result = quantity * 2.00

    return result


drink = input()
quantity_of_drink = int(input())

print(f"{final_price(drink, quantity_of_drink):.2f}")


