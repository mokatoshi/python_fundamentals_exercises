secret_message = input().split(" ")

result = []

for word in secret_message:
    ascii_letter = [char for char in word if char.isdigit()]
    words = [char for char in word if char.isalpha()]

    first_letter = chr(int("".join(ascii_letter)))
    words[0], words[-1] = word[-1], words[0]
    new_word = first_letter + "".join(words)
    result.append(new_word)

print(' '.join(result))
