a, b, c = [int(x) for x in input().split(".")]

c += 1

if c == 10:
    c = 0
    b += 1
    if b == 10:
        b = 0
        a += 1

print(f"{a}.{b}.{c}")
