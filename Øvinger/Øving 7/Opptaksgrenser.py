with open("poenggrenser_2011.csv", "r", encoding= "UTF-8") as f:
  lines = [x.strip('\n') for x in f.readlines()]
  lines = [x.split(',') for x in lines]

  counter = 0
  counter2 = 0
  avr_point = 0
  
  for i in range(len(lines)):     
      if lines[i][1] == '"Alle"':
        counter += 1
      elif "NTNU" in lines[i][0]:
        avr_point += float(lines[i][1])
        counter2 += 1
      
  avr_grade = round(avr_point / counter2, 3)
  
  # print(avr_grade)

def lowest_grade(filename):
  with open(filename, "r", encoding= "UTF-8") as f:
    lines = [x.strip('\n') for x in f.readlines()]
    lines = [x.split(',') for x in lines]
    
    lowest_grade = 100
    lowest_grade_school = ""

    for i in range(len(lines)):
      if lines[i][1] == '"Alle"':
        pass
      elif float(lines[i][1]) < lowest_grade:
          lowest_grade = float(lines[i][1])
          lowest_grade_school = lines[i][0]
          
    return lowest_grade_school, lowest_grade

# print(lowest_grade("poenggrenser_2011.csv"))


def dict_schools(filename):
  with open("poenggrenser_2011.csv", "r", encoding= "UTF-8") as f:
    lines = [x.strip('\n') for x in f.readlines()]
    lines = [x.strip('"') for x in lines]
    lines = [x.split(' ') for x in lines]
    for i in range(len(lines)):
      for j in range(len(lines[i])):
        # print(j)
        try:
          lines = lines[i][-1].split(',')
        except:
          pass
    

    print(lines)
  
    # for i in range(len(lines)):
    #   print(lines[i][-1].split(','))
  
         
      

dict_schools("poenggrenser_2011.csv")

