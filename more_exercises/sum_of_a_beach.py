random_text = input()

small_letters = random_text.lower()

result = small_letters.count("water") + small_letters.count("sand") + small_letters.count("fish") + small_letters.count("sun")

print(result)