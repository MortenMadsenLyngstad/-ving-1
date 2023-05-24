from math import *


def tetraeder():

  h = int(input("Skriv in høyden til tetraederet:\n"))
  a = (3*h)/(sqrt(6))

  A = sqrt(3)*a**2

  V = (sqrt(2)*a**3)/12
  
  print(f'Et tetraeder med høyden {h} har volum', round(V,3),"og areal", round(A,3))

tetraeder()


