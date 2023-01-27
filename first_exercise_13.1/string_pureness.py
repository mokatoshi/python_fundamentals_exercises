n = int(input())

for _ in range(1, n + 1):
    input_line = input()

    is_pure = True
    for ch in input_line:
        if ch == "," or ch == "." or ch == "_":
            is_pure = False
            break

    if is_pure:
        print(f"{input_line} is pure.")
    else:
        print(f"{input_line} is not pure!")
