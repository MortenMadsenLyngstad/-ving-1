def ex_chess():
  pos = str(input("Skriv inn dit du vil flytte sjakkbrikken:\n"))

  let_1 = ["a", "c", "e", "g"]
  let_2 = ["b", "d", "f", "h"]

  num_1 = [1, 2, 3, 4, 5, 6, 7, 8]

  let = pos[0].lower()
  num = int(pos[1])

  if let not in let_1 and let not in let_2 or num not in num_1:
    print('''Feil input!
Første tegn må være en bokstav A-H eller a-h
Andre tegn må være et tall 1-8''')
  elif let in let_1 and num % 2 == 0:
    print("Hvit")
  elif let in let_2 and num % 2 != 0: 
    print("Hvit")
  else:
    print("Svart")


ex_chess()
