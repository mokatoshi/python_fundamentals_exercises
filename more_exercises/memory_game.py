def is_idx_in_range(checked_idx, sequence):
    if 0 <= checked_idx < sequence:
        return True
    return False


def are_idxs_valid(card_1, card_2, stack):
    if is_idx_in_range(card_1, stack) and is_idx_in_range(card_2, stack) and card_1 != card_2:
        return True
    return False


seq_of_elements = input().split(" ")
moves = 0

while True:
    command_line = input()
    moves += 1
    if command_line == "end":
        break

    game_arguments = command_line.split(" ")
    first_card = int(game_arguments[0])
    second_card = int(game_arguments[1])

    if are_idxs_valid(first_card, second_card, len(seq_of_elements)):
        if seq_of_elements[first_card] == seq_of_elements[second_card]:
            found_element = seq_of_elements[first_card]
            seq_of_elements.pop(first_card)
            seq_of_elements.remove(found_element)
            print(f"Congrats! You have found matching elements - {found_element}!")
        else:
            print("Try again!")
    else:
        added_cards = f"-{moves}a"
        insert_index = len(seq_of_elements) // 2
        seq_of_elements.insert(insert_index, added_cards)
        seq_of_elements.insert(insert_index, added_cards)
        print("Invalid input! Adding additional elements to the board")

    if not seq_of_elements:
        print(f"You have won in {moves} turns!")
        exit(0)

print("Sorry you lose :(")
print(* seq_of_elements, sep=" ")





