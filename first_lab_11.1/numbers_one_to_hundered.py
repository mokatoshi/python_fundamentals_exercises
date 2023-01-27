random_num = float(input())

while random_num < 1 or random_num > 100:
    random_num = float(input())

print(f"The number {random_num} is between 1 and 100")