random_num = float(input())

if random_num == 0:
    print("zero")

elif random_num > 0:
    if random_num < 1:
        print("small positive")
    elif random_num > 1000000:
        print("large positive")
    else:
        print("positive")
elif abs(random_num) < 1:
    print("small negative")
elif abs(random_num) > 1000000:
    print("large negative")
else:
    print("negative")
