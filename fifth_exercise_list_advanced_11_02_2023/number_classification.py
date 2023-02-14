list_of_nums_string = input().split(", ")

list_of_numbers = [int(x) for x in list_of_nums_string]

positives = [x for x in list_of_numbers if x >= 0]
negatives = [y for y in list_of_numbers if y < 0]
evens = [z for z in list_of_numbers if z % 2 == 0]
odds = [a for a in list_of_numbers if a % 2 != 0]

print(f"Positive: {', '.join([str(x) for x in positives])}")
print(f"Negative: {', '.join([str (y) for y in negatives])}")
print(f"Even: {', '.join([str(z) for z in evens])}")
print(f"Odd: {', '.join([str (a) for a in odds])}")


