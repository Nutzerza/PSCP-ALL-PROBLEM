"""Blackjack"""
def check_value_a_card(value_card, card):
    """check value a card"""
    value = 0
    con_a_1 = value_card < 11 and len(card) == 1
    con_a_2 = value_card < 10 and len(card) == 2
    con_a_3 = value_card < 9 and len(card) == 3

    if con_a_1 or con_a_2 or con_a_3:
        value += 11
        card = card[1:]
    value += 1*len(card)

    return value

def main(num, value_card=0):
    """print ans"""
    a_card = ""
    for _ in range(num):
        card = input()
        if card in "JQK":
            value_card += 10
        elif card.isnumeric():
            value_card += int(card)
        else:
            a_card += "A"

    if a_card:
        value_card += check_value_a_card(value_card, a_card)

    print(value_card)
main(int(input()))
