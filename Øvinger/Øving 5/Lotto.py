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


def main():
  randLst, addLst = drawNum(7)
  correct, bonus = compList(randLst, addLst)
  win = winnings(correct, bonus)
  print(f"Your numbers: {myGuess}")
  print(f"The winning numbers are: {randLst}")
  print(f"The bonus numbers is: {addLst}")
  print(f"You got {correct} as correct number(s)")
  print(f"You got {bonus} as bonus number(s)")
  print(f"Saldo: {win - 5} NOK")


if __name__ == "__main__":
  main()

