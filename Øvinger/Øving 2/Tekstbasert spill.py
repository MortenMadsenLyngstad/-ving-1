# definerer "exercise textbased game"
def ex_text():
  com = input("You're standing on your pirate ship with your crew.\n")

  com_low = com.lower()

  com_1a = "raise the sails"
  com_1b = "order the crew to raise the sails"

  com_2a = "check treasure"
  com_2b = "ask crew how much treasure we have"

  com_3a = "check map for current location"
  com_3b = "ask crew for current location"

  if com_low == com_1a:
    print('''You raised the ships sails all by your self! 
You are ready to go on an adventure!''')

  elif com_low == com_1b:
    print('''Your crew raised the sails!
You are ready to go on an adventure!''')

  elif com_low == com_2a:
    print('''You have a total of 2.6 Mill NOK worth of treasure!
It is a combination of precious metals, gems, and other valuable objects''')

  elif com_low == com_2b:
    print('''Your crew says you have a total of 2.6 Mill NOK worth of treasure!
It is a combination of precious metals, gems, and other valuable objects''')

  elif com_low == com_3a:
    print('''According to the map you are somewhere in Trondheimsfjorden...
Approximately 1 hour away from shore''')

  elif com_low == com_3b:
    print('''Your navigator says you are in Trondheimsfjorden...
Approximately 1 hour away from shore''')

  else: 
    print("That is not a valid command!")

ex_text()