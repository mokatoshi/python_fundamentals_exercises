employees = input().split(" ")
factor = int(input())

checked_people = list(map(lambda x: int(x) * factor, employees))

filtration = list(filter(lambda x: x >= (sum(checked_people) / len(checked_people)), checked_people))

if len(filtration) >= len(checked_people) / 2:
    print(f"Score: {len(filtration)}/{len(checked_people)}. Employees are happy!")
else:
    print(f"Score: {len(filtration)}/{len(checked_people)}. Employees are not happy!")

