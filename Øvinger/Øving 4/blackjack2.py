import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt.")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled.")
        random.shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __repr__(self):
      if self.name == "Player":
        return f"{self.name} has {self.hand}."
      else:
        return f"{self.name} has {self.hand[0]} and ?."

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self

    def draw_hand(self, deck, hand_size):
        self.hand = deck.deal_hand(hand_size)
        return self

    def show_hand(self):
        for card in self.hand:
            print(card)

class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")

    def show_hand(self):
        print("Dealer's hand:")
        super().show_hand()


def winner(player, dealer):
    if dealer > 21:
        print("Dealer busts! Player wins!")
    elif player > 21:
        print("Player busts! Dealer wins!")
    
    elif player > dealer:
        print("Player wins!")

    elif player < dealer:
        print("Dealer wins!")

    else:
        print("It's a tie!")

def get_value(hand):
    value = 0
    for card in hand:
        if card.value.isnumeric():
            value += int(card.value)
        elif card.value == "A":
          if value + 11 > 21:
            value += 1
          else:
            value += 11
        else:
            value += 10

    return value


def play():
  while True:
    deck = Deck()
    deck.shuffle()

    player = Player("Player")
    dealer = Dealer()

    player.draw_hand(deck, 2)
    print(player)

    dealer.draw_hand(deck, 2)
    print(dealer)
    player_hand = get_value(player.hand)
    dealer_hand = get_value(dealer.hand)
    print("The player score:", get_value(player.hand))
    if player_hand == 21:
        print("Blackjack! Player wins!")
        break
    elif player_hand > 21:
        print("Player busts! Dealer wins!")
        break
    else:
      while player_hand < 21:
        choice = input("Hit or stand? (h/s): ")
        if choice == "h":
          player.draw(deck)
          print("The player score:", get_value(player.hand))
          if get_value(player.hand) > 21:
            print("Player busts! Dealer wins!")
            break
        else:
          break

    if dealer_hand < 17:
        dealer.draw(deck)
        print("The player score:", get_value(player.hand))
        print("The dealer score:", get_value(dealer.hand))

    elif dealer_hand > 17:
        print("The player score:", get_value(player.hand))
        print("The dealer score:", get_value(dealer.hand))

    elif dealer_hand == 21:
        print("Blackjack! Dealer wins!")
        

    elif dealer_hand > 21:
        print("Dealer busts! Player wins!")
        
    
    winner(get_value(player.hand), get_value(dealer.hand))
    break

if __name__ == "__main__":
    play()

