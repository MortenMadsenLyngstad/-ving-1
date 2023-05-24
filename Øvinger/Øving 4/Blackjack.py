import random

suit = ['Hjerter', 'Ruter', 'Spar', 'Kloever']
rank = ['Ess', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knekt', 'Dronning', 'Konge']

deck = []
my_cards = []

for i in range(len(suit)):
  for j in range(len(rank)):
    deck.append((rank[j] + ' av ' + suit[i]))

random.shuffle(deck)


def hit():
  global tot_val
  global card3
  card3 = deck.pop()
  value3 = card3[0]
  if card3[0] == 'K' or card3[0] == 'D' or card3[0] == "1":
    value3 = 10
  elif card3[0] == 'E':
    value3 = 11
  else:
    pass

  my_cards.append(card3)
  
  tot_val += int(value3)
  return card3, tot_val


def dealCards():
  card1 = deck.pop()
  my_cards.append(card1)
  card2 = deck.pop()
  my_cards.append(card2)
  
  

  value1, value2 = card1[0], card2[0]

  if card1[0] == 'K' or card1[0] == 'D' or card1[0] == "1":
    value1 = 10
  elif card2[0] == 'K' or card2[0] == 'D' or card2[0] == "1":
    value2 = 10
  elif value1 == value2 == 'E':
    value1 = 1
    value2 = 11
  elif value1 == 'E':
    if int(value2) + 11 == 21 or int(value2) + 11 < 21:
      value1 = 11
    else:
      value1 = 1
  elif value2 == 'E':
    if int(value1) + 11 == 21 or int(value1) + 11 < 21:
      value2 = 11
    else:
      value2 = 1

  else:
    pass

  global tot_val
  tot_val = int(value1) + int(value2)
  

  if tot_val == 21:
    print('Blackjack!')

  elif tot_val > 21:
    print('Du har tapt!')

  else:
    while True:
      print(f'Kortene dine er {my_cards}')
      print(f'Du har {tot_val} poeng')
      print('Vil du ha flere kort?')
      answer = input('Svar J eller N: ')

      if answer.lower() == 'j':
        hit()
        if tot_val == 21:
          print(f'Kortene dine er {my_cards}')
          print(f'Du har {tot_val} poeng')
          print('Blackjack!')
          break
        elif tot_val > 21:
          print(f'Kortene dine er {my_cards}')
          print(f'Du har {tot_val} poeng')
          print('Du har tapt!')
          break
      else:
        break

  return card1, card2, tot_val



def dealer_cards():
  dealer_card1 = deck.pop()
  dealer_card2 = deck.pop()

  dealer_value1, dealer_value2 = dealer_card1[0], dealer_card2[0]

  if dealer_card1[0] == 'K' or dealer_card1[0] == 'D' or dealer_card1[0] == "1":
    dealer_value1 = 10
  elif dealer_card2[0] == 'K' or dealer_card2[0] == 'D' or dealer_card2[0] == "1":
    dealer_value2 = 10
  elif dealer_value1 == dealer_value2 == 'E':
    dealer_value1 = 1
    dealer_value2 = 11
  elif dealer_value1 == 'E':
    if int(dealer_value2) + 11 == 21 or int(dealer_value2) + 11 < 21:
      dealer_value1 = 11
    else:
      dealer_value1 = 1
  elif dealer_value2 == 'E':
    if int(dealer_value1) + 11 == 21 or int(dealer_value1) + 11 < 21:
      dealer_value2 = 11
    else:
      dealer_value2 = 1

  else:
    pass

  dealer_tot_val = int(dealer_value1) + int(dealer_value2)
  
  print(f'Dealer har {dealer_card1} og ?')

  dealCards()

  while dealer_tot_val < 17 and dealer_tot_val < tot_val:
    dealer_card3 = deck.pop()
    dealer_value3 = dealer_card3[0]
    if dealer_card3[0] == 'K' or dealer_card3[0] == 'D' or dealer_card3[0] == "1":
      dealer_value3 = 10
    elif dealer_card3[0] == 'E':
      if int(dealer_tot_val) + 11 == 21 or int(dealer_tot_val) + 11 < 21:
        dealer_value3 = 11
      else:
        dealer_value3 = 1
    else:
      pass

    dealer_tot_val += int(dealer_value3)

  print(f'Dealer har kortene {dealer_card1}, {dealer_card2} og {dealer_card3}')

  if tot_val > 21:
    pass
  elif dealer_tot_val == 21:
    print('Dealer har Blackjack!')
  elif dealer_tot_val > 21:
    print('Dealer har tapt!')
  elif dealer_tot_val > tot_val:
    print(f'Dealer vant med totalsum: {dealer_tot_val}')
  elif dealer_tot_val == tot_val:
    print(f'Det er helt likt, begge har totalsum {dealer_tot_val}')
  


dealer_cards()


