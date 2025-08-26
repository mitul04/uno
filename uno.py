class Card:
    def __init__(self, value, color='wild'):
        self.color = color
        self.value = value

    def __str__(self):
        return f'{self.color}-{self.value}'

    def __repr__(self):
        return self.__str__()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def discard_card(self, card):
        self.hand.remove(card)

    def show_all_cards(self):
        print(self.hand)

    def play_cards(self):
        playable = [card for card in self.hand if card.color == discard_top.color or card.value == discard_top.value]

        if playable == []:
            print('No cards playable')
            self.add_card(draw_top)

        else:
            print('Playable cards:', playable)
            index = int(input('\nEnter index of desired card: '))
            card = playable.pop(index)
            self.hand.remove(card)