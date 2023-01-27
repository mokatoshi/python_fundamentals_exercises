number_of_orders = int(input())

price_per_day = 0
total_price = 0

for i in range(1, number_of_orders + 1):

    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_price < 0.01 or capsule_price > 100:
        continue
    price_per_day = capsule_price * days * capsules_per_day
    total_price += price_per_day

    print(f"The price for the coffee is: ${price_per_day:.2f}")

print(f"Total: ${total_price:.2f}")

