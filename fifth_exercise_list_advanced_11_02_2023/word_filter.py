fruits_list = input().split(" ")

result = [word for word in fruits_list if len(word) % 2 == 0]
# for word in result:
#     print(word)

print("\n".join(result))
#
#

######## using LAMBDA function ########

# words = input().split(" ")
# result = list(filter(lambda x: len(x) % 2 == 0, words))
# print("\n".join(result))
#

