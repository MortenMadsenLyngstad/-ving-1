def weekday_newyear(year):
  days = ["man", "tir", "ons", "tor", "fre", "lor", "son"]

  day = 0
  while year < 1920:
    check_leap = year - 1900

    if check_leap % 4 == 0 and check_leap != 0:
      print(f"{year} {days[day]}")
      day += 2
           
    else:
      y_d = f"{year} {days[day]}"
      print(y_d)
      day += 1
      
    if day == 7:
      day = 0
    
    year += 1 
    
weekday_newyear(1900)


