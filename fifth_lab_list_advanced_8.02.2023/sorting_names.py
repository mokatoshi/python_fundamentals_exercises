random_names = input().split(", ")

sorted_names = sorted(random_names, key=lambda x: (-len(x), x))
print(sorted_names)