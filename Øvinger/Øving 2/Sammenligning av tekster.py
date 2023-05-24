def a():
  a = str(input("Skriv inn en matvare: "))
  b = str(input("Skriv enda en matvare: "))

  print(f'Sammenligner {a} og {b}')

  if a.lower() == b.lower():
    print("Det er samme matvare")

  else:
    print("Det er ikke samme matvare")

# a()


def b_1():
  a = str(input("Skriv inn et navn: " ))
  b = str(input("Skriv inn enda et navn: "))

  print("Dette er navnene i alfabetisk rekkefølge")

  if a > b:
    print(b, a)

  else:
    print(a, b)


# b_1()



def b_2():
  a = str(input("Skriv inn et navn: "))
  b = str(input("Skriv inn enda et navn: "))

  l = [a, b]
  l.sort()

  print("Dette er navnene i alfabetisk rekkefølge")

  # for-løkke som printer ut navnene på samme linje
  for i in l:  
    print(i, sep=' ', end=' ', flush=True)

# b_2()


# Svar på oppgave C

def kode_1():
  #Kodesnutt 1:
  if 'k' < 'b':
      print('k er mindre enn b')
  else:
      print('k er større enn b')

  # svar - den vil printe "k er større enn b"

# kode_1() 


def kode_2():  
  #Kodesnutt 2:
  ny = "New York"
  la = "Los Angeles"
    
  if ny < la:
      print(ny)
      print(la)
  else:
      print(la)
      print(ny)

  # svar - den vil print "Los Angeles, deretter New York"
  
# kode_2()


def kode_3():
  #Kodesnutt 3:
  d1 = "DRuEr"
  d2 = "drUer"
  if d1.lower() < d2.lower():
      print(d1)
      print(d2)
  else:
      print(d2.lower())

# svar - den vil printe "druer" fordi d1 == d2


# kode_3()