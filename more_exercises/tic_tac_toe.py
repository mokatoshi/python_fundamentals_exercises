first_line, second_line, third_line = input().split(), input().split(), input().split()

total_lines = first_line + second_line + third_line

int_lines = []

player_one_win = False
player_two_win = False


if total_lines[0] == "1" and total_lines[1] == "1" and total_lines[2] == "1" or \
        total_lines[3] == "1" and total_lines[4] == "1" and total_lines[5] == "1" or\
        total_lines[6] == "1" and total_lines[7] == "1" and total_lines[8] == "1":
    player_one_win = True

if total_lines[0] == "1" and total_lines[3] == "1" and total_lines[6] == "1":
    player_one_win = True
elif total_lines[1] == "1" and total_lines[4] == "1" and total_lines[7] == "1":
    player_one_win = True
elif total_lines[2] == "1" and total_lines[5] == "1" and total_lines[8] == "1":
    player_one_win = True

if total_lines[0] == "1" and total_lines[4] == "1" and total_lines[8] == "1":
    player_one_win = True
elif total_lines[2] == "1" and total_lines[4] == "1" and total_lines[6] == "1":
    player_one_win = True


for i in range(len(total_lines)):
    int_lines.append(int(total_lines[i]))

if int_lines[0] + int_lines[1] + int_lines[2] == 6 or int_lines[3] + int_lines[4] + int_lines[5] == 6 or \
        int_lines[6] + int_lines[7] + int_lines[8] == 6:
    player_two_win = True

elif int_lines[0] + int_lines[3] + int_lines[6] == 6 or int_lines[1] + int_lines[4] + int_lines[7] == 6 or \
        int_lines[2] + int_lines[5] + int_lines[8] == 6:
    player_two_win = True
elif int_lines[0] + int_lines[4] + int_lines[8] == 6 or int_lines[2] + int_lines[4] + int_lines[6] == 6:
    player_two_win = True


if player_one_win:
    print("First player won")
elif player_two_win:
    print("Second player won")
elif not player_two_win or not player_one_win:
    print("Draw!")
