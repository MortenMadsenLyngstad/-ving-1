# importerer kvadratrot fra math biblioteket
from math import sqrt

# funksjon som regner ut areal og omkrets av et tetraeder, gitt høyden
def tetraeder():
  # ber personen skrive inn høyder til tetraederet 
  h = int(input("Skriv in høyden til tetraederet:\n"))
  a = (3*h)/(sqrt(6))

  A = sqrt(3)*a**2

  V = (sqrt(2)*a**3)/12
  
  print(f'Et tetraeder med høyden {h} har volum', round(V,3),"og areal", round(A,3))

tetraeder()


