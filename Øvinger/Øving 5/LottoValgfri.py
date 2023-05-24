import random


myGuess = [2, 19, 32, 9, 18, 25, 30]
numbers = list(range(1, 35))


def drawNum(n):
  randLst = []
  addLst = []   
  all = random.choices(numbers, k=n + 3)
  randLst = all[:n]
  addLst = all[n:]

  return randLst, addLst 


def compList(randLst, addLst):
  correct = 0
  bonus = 0
  for i in myGuess:
    if i in randLst:
      correct += 1
    if i in addLst:
      bonus += 1
  return correct, bonus


def winnings(correct, bonus):
  if correct == 4:
    return 50
  elif correct == 5:
    return 110
  elif correct == 6:
    return 4500
  elif correct + bonus == 7:
    return 127800
  elif correct == 7:
    return 3600000
  else:
    return 0



money = 0

for i in range(1000000):
  randLst, addLst = drawNum(7)
  correct, bonus = compList(randLst, addLst)
  money += (winnings(correct, bonus))


print(f'Etter å ha spilt 1000000 ganger har du totalt brukt {1000000 * 5}kroner og vunnet {money} kroner. Dette gir en netto intekt på {money - 1000000 * 5} kroner.')




