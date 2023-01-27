start = int(input())

for i in range(start):
    for j in range(start):
        for k in range(start):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")
