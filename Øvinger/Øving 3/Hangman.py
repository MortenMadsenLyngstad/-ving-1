secret_word = str(input("Hemmelig ord: ")).lower()
num_lives = int(input("Antall liv: "))

guess = []
l_secret_word = (list(map(str, secret_word)))

tip = "*"*len(secret_word)

while True:
  let = str(input("Skriv inn en bokstav som skal passe i det hemmelige ordet: ")).lower()

  if let in secret_word:
    print(f'Stemmer, {let} er i ordet, du har fortsatt {num_lives} liv igjen')

    guess.append(let)

    tip_update = ""
  
    for i, char in enumerate(secret_word):
      if char == let:
        tip_update += let
      else:
        tip_update += tip[i]

    tip = tip_update

    print(tip)
    
    if all(elem in guess  for elem in l_secret_word):
      print(f'Du gjettet hele ordet! Ordet var {secret_word}')
      break 
    else:
      print(f'Dette har du gjettet så langt: {guess}')

  else:
    if num_lives >= 1:
      num_lives -= 1
      print(f'''Bokstaven {let} er ikke i ordet...
Du har {num_lives} liv igjen''')

      if num_lives == 0:
        print("Det var ditt siste forsøk! Bedre lykke neste gang.")

        break
    
  
      
