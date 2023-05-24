def a():
  tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))

  if tid >= 50:
    print("Kaken kan tas ut av ovnen.")
    print("Tips til servering: vaniljeis.")

  else:
    print("Det har enda ikke gått 50 minutter, så la kaken stå i ovnen en stund til.")

# a()

def b():
  epler = int(input("Hvor mange epler har du? "))
  barn = int(input("Hvor mange barn passer du? "))
  if barn > 0:
    print("Da blir det", epler // barn, "epler til hvert barn")
    print("og", epler % barn, "epler til overs til deg selv.")
    print("Takk for i dag!")

  else:
    print("Siden du ikke passer noen barn, får du alle eplene for deg selv.")
    print("Takk for i dag!")

# b()


def c_d():
  alder = int(input("Skriv inn din alder: "))

  if alder >= 18:
    print("Du kan stemme ved både lokalvalg og Stortingsvalg!")

  elif alder in range (16, 18):
    print("Du kan stemme ved lokalvalg, men ikke ved Stortingsvalg")
  
  elif alder < 16:
    print("Du kan ikke stemme")

  else:
    print("Skriv inn en gyldig alder!")
    return

# c_d()


def e():
  alder = int(input("Skriv inn din alder: "))

  if alder in range (0, 3):
    print("Billetten er gratis!")

  elif alder in range (3, 12):
    print("30 kroner for billett")

  elif alder in range (12, 26):
    print("50 kroner for billett")
  
  elif alder in range (26, 67):
    print("80 kroner for billett")
  
  elif alder >= 67:
    print("40 kroner for billett")
  
  else:
    print("Skriv inn en gyldig alder!")


e()