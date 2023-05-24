def a():
  num = int(input("Skriv inn et heltall og få ut summen av tallserien: "))

  n = 1
  l = []

  while n <= num:

    if n % 2 == 0:
      even = (n**2)*(-1)
      l.append(even)
  
    
    else:
      odd = n**2
      l.append(odd)
    
  
    n += 1

  print(sum(l))
    

a()

  



