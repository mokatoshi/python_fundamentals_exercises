random_word = input()

reverse_word = ""

for i in range(len(random_word) - 1, -1, -1):
    reverse_word += random_word[i]
print(reverse_word)
