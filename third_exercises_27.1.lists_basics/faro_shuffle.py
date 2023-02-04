random_deck = input().split()
shuffles = int(input())


for shuffle in range(shuffles):
    final_deck = []
    middle_of_cards = len(random_deck) // 2
    left_deck = random_deck[0:middle_of_cards]
    right_deck = random_deck[middle_of_cards::]
    for idx_of_cards in range(len(left_deck)):
        final_deck.append(left_deck[idx_of_cards])
        final_deck.append(right_deck[idx_of_cards])
    random_deck = final_deck

print(random_deck)
