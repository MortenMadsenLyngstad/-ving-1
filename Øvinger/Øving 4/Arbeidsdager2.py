def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekday_newyear(year):
    lst = []
    day = 0
    while year < 1920:
      
      if is_leap_year(year) == True:
        result = f"{year} {day}"
        lst.append(result)
        day += 1

      else:
        result = f"{year} {day}"
        lst.append(result)
      day += 1
      if day == 7:
        day = 0
      year += 1
    
    return lst



def workdays_in_year(year):
  x = weekday_newyear(1900)
  days = ["man", "tir", "ons", "tor", "fre", "lor", "son"]
  all_days = []


  def is_workday(day):
    if day in days[:5]:
      return True
    else:
      return False

  for i in x:
    year_day = i.split(" ")
  
    for j in range(len(days)):
      if year_day[-1].isdigit():
        year_day[-1] = days[int(year_day[-1])]

        all_days.append(year_day[-1])
     
    else: 
      pass

  month = ["jan", "feb", "mar", "apr", "mai", "jun", "jul", "aug", "sep", "okt", "nov", "des"]
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  workdays = 0

  cur_day = all_days[year - 1900]
  work = days.index(cur_day)
  

  if is_leap_year(year) == False:

    for i in range(len(month)):
      for _ in range(days_in_month[i - 1]):
        
        if is_workday(days[work]) == True:
          workdays += 1
          work += 1
         

        else:
          work += 1
          if work == 7:
            work = 0
          pass
  else:
    days_in_month[1] = 29

    for i in range(len(month)):
      for _ in range(days_in_month[i - 1]):
        
        if is_workday(days[work]) == True:
          workdays += 1
          work += 1
         

        else:
          work += 1
          if work == 7:
            work = 0
          pass

  return workdays


for i in range(1900, 1920):
  print(f'{i} har {workdays_in_year(i)} arbeidsdager')
