number_list = list(range(0, 100))
print(f'Oppgave A: Listen mellom 0 og 100: {number_list}\n')

addlst = []


def sumlst():
  for i in number_list:
    if i % 3 == 0:
      addlst.append(i)
    elif i % 10 == 0:
      addlst.append(i)
    else:
      pass

  s = sum(addlst)
  return s


print(f'Oppgave B: Summen av alle tall som er delelig med 3 eller 10 er i number_list: {sumlst()}\n')


def swap(l):
  temp = l
  for i in range(len(temp)):
    for j in range(i+1, len(temp)):
      if temp[i] % 2 == 0:
        temp[i] = temp[j]
  
  for i, j  in enumerate(temp):
    if i % 2 == 0:
     temp[j] = temp[j] - 1
      
  return temp


print(f'Oppgave C: {swap(number_list)}\n')


def reverse(lst):
  return lst[::-1]


print(f'Oppgave D: {reverse(swap(number_list))}\n')


  