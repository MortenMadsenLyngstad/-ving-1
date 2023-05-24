# importerer floor fra math-biblioteket
from math import floor

# definerer en funksjon uten argumenter
def jamesbond_a():
  # lager variabler for input
  num = float(input("Skriv inn desimaltall her:\n"))
  dec = int(input("Hvor mange desimaler skal det rundes av til?\n"))

  # definerer en ny funksjon for å runde av desimalene riktig
  def round_half_up(n, decimals):
    multiplier = 10 ** decimals

    # bruker .floor for å runde NED til nermeste integer
    # plusser på 0.5 for å få avrundingen riktig iforhold til oppgaven
    return floor(n*multiplier + 0.5) / multiplier

  # kaller på funksjonen og lagrer svaret i en variabel
  svar = round_half_up(num, dec)
  
  # printer ut svaret
  print(svar)

# kaller på funksjonen
# jamesbond_a()


def jamesbond_b():
  # lager variabler for input
  num = int(input("Oppgi heltallsdelen av tallet (det foran punktum):\n"))
  dec = int(input("Oppgi desimaldelen av tallet (det bak punktum):\n"))
  rounding = int(input("Oppgi ønsket antall desimaler i avrunding:\n"))

  # lager variabel som gjør dec om til et desimal
  dec_1 = dec * 10**(-len(str(dec)))
  # legger til dec_1 til num for å få det hele desimaltallet
  num_1 = num + dec_1

  # bruker samme funksjon som i oppg a)
  def round_half_up(n, decimals):
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.5) / multiplier

  svar = round_half_up(num_1, rounding)

  print(svar)


# jamesbond_b()


def jamesbond_c():
  name = input("My name is: ")
  # bruker .split() for å lage en liste av inputten
  last_name = name.split()
  # last_name[-1] tar siste element i listen
  answer = f'The name is {last_name[-1]}, {name}'

  print(answer)

# jamesbond_c()


def jamesbond_valgfri():
  name = str(input("My name is: "))
  part_name = name.split()
  answer = f'The name is {part_name[-1]}, {name}'

  # lager lister som inneholder det som "ikke skal brukes" i svaret
  name_prefix = ["Von", "Van", "De", "Di"]
  rom_num = ["M", "D", "C", "L", "X", "V", "I", "II", "III", "IV", "(", ")"]
  last = ["Jr", "Sr"]


  # for løkke for element "i" i part_name
  for i in part_name:
    
    # if setning som sjekker om en av elementene i listen er noe som ikke skal være med
    if str(i) in name_prefix or rom_num or last:
      
      # hvis element i name_prefix
      if str(i) in name_prefix:
        # sjekker hvilken plass elementet er i listen og lager en variabel
        index = part_name.index(i)

        # plasserer name_prefix-elementet før etternavnet
        answer =  f'The name is {part_name[index]} {part_name[-1]}, {name}'

      elif str(i) in rom_num or str(i) in last:
        answer =  f'The name is {part_name[-2]}, {name}'

    else:
      break

  print(answer)

   
jamesbond_valgfri()  