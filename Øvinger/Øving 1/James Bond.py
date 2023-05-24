import math

# Oppgaven din her er å lage et program som får til kjøpmannsavrunding. Det skal be bruker om å skrive inn et desimaltall, samt ønsket antall desimaler det skal avrundes til - og så foreta denne avrundingen. Dette må da gjøres på annet vis enn å bruke Pythons round()-funksjon, siden du f.eks. skal runde 2.5 til 3 (hvis null desimaler) og 2.25 til 2.3 (hvis en desimal) mens round() ville runde nedover her.
def jamesbond_a():
  num = float(input("Skriv inn desimaltall her:\n"))
  dec = int(input("Hvor mange desimaler skal det rundes av til?\n"))

  def round_half_up(n, decimals = 0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

  svar = round_half_up(num, dec)
  
  print(svar)


jamesbond_a()

