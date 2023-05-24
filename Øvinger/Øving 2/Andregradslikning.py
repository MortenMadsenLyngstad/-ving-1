from math import sqrt


def a_b():
  a = float(input("Skriv inn et tall for a: "))
  b = float(input("Skriv inn et tall for b: "))
  c = float(input("Skriv inn et tall for c: "))

  d = float((b**2) - (4 * a * c))

  if d > 0:
    x_1 = (-b + sqrt(d))/(2*a)
    x_2 = (-b - sqrt(d))/(2*a)

    print(f'''diskrimant = {d}
Andregradslikningen {a}*x^2 + {b}*x + {c} har to reelle løsninger: {x_1} og {x_2}''')

  elif d < 0:
    print(f'''diskrimant = {d}
Andregradslikningen {a}*x^2 + {b}*x + {c} har to imaginære løsninger''')

  elif d == 0:
    x_1 = (-b + sqrt(d))/(2*a)

    print(f'''diskrimant = {d}
Andregradslikningen {a}*x^2 + {b}*x + {c} har én reell dobbeltrot: {x_1}''')


a_b()


def c():
  a = float(input("Skriv inn et tall for a: "))
  b = float(input("Skriv inn et tall for b: "))
  c = float(input("Skriv inn et tall for c: "))

  b_sgn = ((b**2) - (4*a*c))

  def sgn(x):
    if x > 0:
      return 1
    elif x == 0:
      return 0
    else:
      return -1

  q = (-1/2)*(b + sgn(b_sgn) * sqrt(b_sgn))


  if sgn(b_sgn) > 0:
    x_1 = c/q
    x_2 = q/a
    
    print(f'''Andregradslikningen {a}*x^2 + {b}*x + {c} har to reelle løsninger: {'{:.3e}'.format(x_1)} og {'{:.3e}'.format(x_2)}''')

  elif sgn(b_sgn) < 0:
    print(f'''Andregradslikningen {a}*x^2 + {b}*x + {c} har to imaginære løsninger''')

  elif b_sgn == 0:
    x_1 = (-b + sqrt(b_sgn))/(2*a)

    print(f'''Andregradslikningen {a}*x^2 + {b}*x + {c} har én reell dobbeltrot: {x_1}''')


# c()