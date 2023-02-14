# example:
# n shell = 2*number of the shell ^ 2
# 1st shell = 2*1**2 = 3
# 2nd shell = 2*2**2 = 8
# 3rd shell = 2*3**2 = 18
# 4th shell = 2*4**2 = 32
# 5th shell = 2*5**2 = 50

number_of_electrons = int(input())

shells_distribution = []

while number_of_electrons > 0:
    number_of_shell = len(shells_distribution) + 1
    electrons = min(2 * (number_of_shell ** 2), number_of_electrons)
    shells_distribution.append(electrons)
    number_of_electrons -= electrons

print(shells_distribution)
