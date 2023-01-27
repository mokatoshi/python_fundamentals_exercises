divisor = int(input())
boundary = int(input())

largest_num = 0

for N in range(1, boundary + 1):
    number_check = N / divisor
    if 0 < N and N <= boundary and number_check.is_integer():
        largest_num = N
print(largest_num)
