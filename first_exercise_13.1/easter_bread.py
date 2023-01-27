budget = float(input())
flour_price = float(input())

colored_eggs_counter = 0
loaves_counter = 0

eggs_price = flour_price * 0.75
total_milk_price = flour_price * 1.25

milk_price = total_milk_price / 4

one_loaf_price = flour_price + eggs_price + milk_price

while budget >= one_loaf_price:
        budget -= one_loaf_price
        loaves_counter += 1
        colored_eggs_counter += 3
        if loaves_counter % 3 == 0:
            colored_eggs_counter = colored_eggs_counter - (loaves_counter - 2)

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
