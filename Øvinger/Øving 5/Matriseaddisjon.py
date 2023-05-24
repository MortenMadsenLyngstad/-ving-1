import random

def random_matrise(bredde, høyde):
  matrix = [[0 for i in range(bredde)] for j in range(høyde)]
  for i in range(høyde):
    for j in range(bredde):
      matrix[i][j] = random.randint(0, 10)

  return matrix


def print_matrise(matrise, navn):
  if matrise is None:
    new = navn.split("+")
    print(f'{new[0]} og {new[1]} er ikke samme dimensjon')
  else:
    print(f'{navn} = {matrise}')


def matrise_addisjon(a, b):
  
  if len(a) != len(b) or len(a[0]) != len(b[0]):
    pass
  else:
    c = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
      for j in range(len(a[0])):
        c[i][j] = a[i][j] + b[i][j]

    return c


def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(4,3)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')

    D = matrise_addisjon(A, B)
    print_matrise(D, 'A+B')

    E = matrise_addisjon(A, C)
    print_matrise(E, 'A+C')
  
if __name__ == "__main__":
  main()