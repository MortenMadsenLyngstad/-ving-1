import random


def ex():
  print('''INFO
  I dette programmet skal du leke en gjettelek.
  Først må du skrive inn en øvre og nedre grense i form av heltall.''')

  num_lower = int(input("Skriv inn en nedre grense: "))
  num_upper = int(input("Skriv inn en øvre grense: "))
  
  num = random.randint(num_lower, num_upper)  

  guessnum = 0
 

  while True:
    guess = int(input("Nå skal du gjette tallet: "))
    guessnum += 1
    if guessnum == 1:
     print(f'Du har gjettet {guessnum} gang!')
    else:
      print(f'Du har gjettet {guessnum} ganger!')

    if guess > num:
      print("Prøv et lavere tall!")

    elif guess < num:
      print("Prøv et høyere tall!")
     
    elif guess == num:
      print(f'Helt riktig! Tallet var {num} akkurat som du gjettet!')
      break
      

ex()