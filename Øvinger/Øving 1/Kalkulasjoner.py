# importerer alt fra math-biblioteket
from math import *


def kalk_a():
  print('1+2(−3) =', 1 + 2 * (-3))
  print('[(3+5·2) + 1] : 2 =', ((3 + 5 * 2) + 1) / 2)
  print('-3^2+5*3-7 =', -3**2 + 5 * 3 - 7)
  #1)
  print('5:2-4 =', (5/2) - 4)
  #2)
  print('5·12+6-1 =', (5*12) + 6 - 1)
  #3)
  print('3(5+2) =', 3*(5+2))
  #4)
  print('4[(5+3):2 +7] =', 4*((5+3)/2 + 7))
  #5)
  print('(−4)^(-3)+5·(3−7:2) =', (-4)**(-3) + 5*(3-(7/2)))

# kalk_a()


def kalk_b():
  print(355, "minutt blir", 355 // 60, "timer og", 355 % 60, "minutt.")
  print(403, "sekund blir", 403 // 60, "minutt og", 403 % 60, "sekund.")
  print(67, "dager blir", 67 // 7, "uker og", 67 % 7, "dager.")
  print(100, "timer blir", 100 // 24, "døgn og", 100 % 24, "timer.")

# kalk_b()


def kalk_c():
    
  print("|-8|, dvs. absoluttverdien til -8, er", abs(-8))
  print(2.544, "avrundet til helt tall er", round(2.544))
  print("Funksjonen int() derimot bare kutter vekk desimalene:", int(2.544) )
  print(2.544, "avrundet til to desimaler er", round(2.544, 2))
  print("Kvadratroten til", 10, "er", sqrt(10))
  print("En sirkel med radius 7 har omkrets", tau * 7)
  print("En sirkel med radius 7 har areal", pi * 7**2)

# kalk_c()