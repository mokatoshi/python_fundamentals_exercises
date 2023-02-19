range_of_price_tags = [int(x) for x in input().split(", ")]
entry_point = int(input())
item_price = input()

left = range_of_price_tags[:entry_point]
right = range_of_price_tags[entry_point + 1:]

left_side_prices = 0
right_side_prices = 0


if item_price == "cheap":

    for i in left:
        if i < range_of_price_tags[entry_point]:
            left_side_prices += i
    for j in right:
        if j < range_of_price_tags[entry_point]:
            right_side_prices += j

elif item_price == "expensive":
    for k in left:
        if k >= range_of_price_tags[entry_point]:
            left_side_prices += k
    for l in right:
        if l >= range_of_price_tags[entry_point]:
            right_side_prices += l


if left_side_prices >= right_side_prices:
    print(f"Left - {left_side_prices}")
else:
    print(f"Right - {right_side_prices}")



#
# numbers = list(map(int, input().split(", ")))
# entry_point = int(input()) # index
# item_price = input()
#
# left = numbers[:entry_point]
# right = numbers[entry_point + 1:]
#
# left_sum = 0
# right_sum = 0
#
# if item_price == "cheap":
#     left_sum = sum(i for i in numbers if i < numbers[entry_point])
#     right_sum = sum(j for j in numbers if j < numbers[entry_point])
#
# elif item_price == "expensive":
#     left_sum = sum(i for i in numbers if i >= numbers[entry_point])
#     right_sum = sum(j for j in numbers if j >= numbers[entry_point])
#
# if left_sum >= right_sum:
#     print(f"Left - {left_sum}")
# else:
#     print(f"Right - {right_sum}")