from math import ceil

students_count = int(input())
lessons = int(input())
bonus = int(input())

max_bonus = 0
highest_att = 0
each_bonus = 0

for i in range(students_count):
    current_stud_attendance = int(input())
    if lessons > 0:
        each_bonus = current_stud_attendance / lessons * (5 + bonus)
        if each_bonus > max_bonus:
            max_bonus = each_bonus
            if current_stud_attendance > highest_att:
                highest_att = current_stud_attendance
    else:
        print(f'Max Bonus: {0}.')
        print(f'The student has attended {0} lectures.')
        exit()
print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {ceil(highest_att)} lectures.')
