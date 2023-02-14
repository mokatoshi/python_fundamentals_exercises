command = input()

to_do = []

while command != "End":
    to_do.append(command)
    command = input()

for i in range(len(to_do)):
    to_do[i] = to_do[i].split("-")
    to_do[i][0] = int(to_do[i][0])
to_do = sorted(to_do)

for i in range(len(to_do)):
    to_do[i].pop(0)
    to_do[i] = "".join(to_do[i])

print(to_do)
