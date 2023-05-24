# definerer måde max og r utenfor funksjonene slik at de kan brukes i alle funksjonene
max = int(input("Skriv inn et heltall: "))
r = float(input("Skriv inn et reelt tall: "))

def a():
  global max
  global r
  n = 0
  s = 0

  while n in range(0, max + 1):
    num = r**n

    s += num

    n += 1

  print(f'''#a
Summen av rekken er {s}''')
  
a()


def oppg_besvarelse():
  global r

  n = 0
  s = 0

  limit = 1/(1-r)
  tol = 0.001
  s_1 = ((1 - ((r)**(n+1)))/(1-r))

  while s_1 < limit +- tol:
    num = r**n

    s += num
    s_1 = ((1 - ((r)**(n+1)))/(1-r))

    n += 1

  print(f'''#b_c
For å være innen toleransegrensen kjørte løkken {n} ganger.
Differansen mellom virkelig estimert verdi er da {2 - s_1}.''')
  

oppg_besvarelse()
  

# trodde oppgaven skulle løses slik først. 
def b_c():
  global r

  limit = 1/(1-r)

  tol = 0.001

  n = 0
  s = ((1 - ((r)**(n+1)))/(1-r))
  # counter = 0

  while s < limit +- tol:
    n += 1

    s = ((1 - ((r)**(n+1)))/(1-r))
    # counter += 1

  print(f'''Summen av rekken er {s}.
For å være innen toleransegrensen kjørte løkken {n} ganger.
Differansen mellom virkelig estimert verdi er da {2 - s}.''')


# b_c()



