def a():
    
  num = int(input("Hvor mange rekker vil du ha? "))

  for i in range(1,num+1):
      for j in range(1, i+1):
          print(j, end=" ")
      print()

# a()


def b():
  num = int(input("Hvor mange rekker vil du ha? "))
  space = " "
  for i in range(num):
    print(f'X{space * i} X')
     
b()


def b_2():
  num = int(input("Hvor mange rekker vil du ha? "))
  
  for i in range(num):
    var = "X"
    for j in range(i+1):
      space = " "
      var += space

    var += "X"
    print(var)

# b_2()
  