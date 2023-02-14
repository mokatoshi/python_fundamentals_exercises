random_string = input().split(" ")

searched_word = input()

palindromes = []

for word in random_string:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(f"{palindromes}")
print(f"Found palindrome {palindromes.count(searched_word)} times")

