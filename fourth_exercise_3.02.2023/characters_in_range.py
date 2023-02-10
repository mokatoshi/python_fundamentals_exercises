def ascii_chars(a, b):
    symbols = []
    for i in range(ord(a) + 1, ord(b)):
        symbols.append(chr(i))
    return symbols


char_one = input()
char_two = input()

symbols_chars = ascii_chars(char_one, char_two)
print(" ".join(symbols_chars))

