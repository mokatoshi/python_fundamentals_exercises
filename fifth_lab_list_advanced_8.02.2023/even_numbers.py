# random_nums = input().split(", ")
#
# int_nums = []
#
# for i in range(len(random_nums)):
#     int_nums.append(int(random_nums[i]))
#
# even_index = [x for x in range(len(int_nums)) if int_nums[x] % 2 == 0]
#
# print(even_index)


# 1st variety of solution with for and comprehension
#####################################################################
# 2nd variety of solution entirely with for loops

# random_nums = input().split(", ")
#
# int_nums = []
#
# even_index = []
#
# # for i in range(len(random_nums)):
# #     int_nums.append(int(random_nums[i]))
# #
# # for x in range(len(int_nums)):
# #     if int_nums[x] % 2 == 0:
# #         even_index.append(x)
# #
# # print(even_index)

# 3rd variety of solution with lambda function

random_nums = list(map(int, input().split(", ")))

found_indexes_or_no = map(lambda x: x if random_nums[x] % 2 == 0 else "no", range(len(random_nums)))

even_indexes = list(filter(lambda a: a != "no", found_indexes_or_no))
print(even_indexes)
