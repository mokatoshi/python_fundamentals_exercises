lines = int(input())

opening_count = 0
closing_count = 0


for i in range(1, lines + 1):
    new_string = input()
    if new_string == "(":
        opening_count += 1
    elif new_string == ")":
        closing_count += 1

    if closing_count == 1 and opening_count == 0:
        print("UNBALANCED")
        break
    elif opening_count == 2 and closing_count == 0:
        print("UNBALANCED")
        break
    elif closing_count == 2 and opening_count == 1:
        print("UNBALANCED")
        break
if opening_count == closing_count:
    print("BALANCED")

