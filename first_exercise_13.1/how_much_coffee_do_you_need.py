counter = 0
while True:
    input_line = input()

    if input_line == "END":
        print(f"{counter}")
        break

    elif input_line == "coding" or input_line == "dog" or \
            input_line == "cat" or input_line == "movie":
        counter += 1
    elif input_line == "CODING" or input_line == "DOG" or \
            input_line == "CAT" or input_line == "MOVIE":
        counter += 2
    else:
        continue

    if counter > 5:
        print("You need extra sleep")
        break