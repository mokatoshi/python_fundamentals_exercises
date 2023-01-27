animals = input().split(", ")

an = list(animals)

wolf = ""

if an[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    wolf = an.index("wolf")
    print(f"Oi! Sheep number {len(an) - 1 - wolf}! You are about to be eaten by a wolf!")
