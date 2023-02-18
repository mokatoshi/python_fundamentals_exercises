community = [int(x) for x in input().split("@")]

jump = 0

while True:
    command_line = input()
    if command_line == "Love!":
        break

    idx = int(command_line.split(" ")[1])
    idx += jump

    if idx >= len(community):
        idx = 0

    if community[idx] == 0:
        print(f"Place {idx} already had Valentine's day.")

    else:
        community[idx] -= 2
        if community[idx] == 0:
            print(f"Place {idx} has Valentine's day.")

    jump = idx


print(f"Cupid's last position was {jump}.")

if sum(community) == 0:
    print("Mission was successful.")

else:
    count_of_missed = [x for x in community if x > 0]
    print(f"Cupid has failed {len(count_of_missed)} places.")

