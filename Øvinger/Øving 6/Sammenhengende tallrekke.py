import random

def randList(size, lower_bound, upper_bound):
  return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# print(randList(15, 1, 10))

def compareLists(list1, list2):
  l3 = []

  for i in range(len(list1)):
    for j in list1:
      if j in list2 and j not in l3:
        l3.append(j)
      else:
        pass
  return l3

# print(compareLists(randList(15, 1, 100), randList(15, 1, 100)))

def multiCompList(d):
  l4 = randList(5, 1, 5)
  comp = []
  rand = []

  for _ in range(d):
    rand.append(randList(5, 1, 5))
  
  for i in range(len(rand)):
    for j in l4:
      if j not in rand[i]:
        try:
            comp.remove(j)
        except:
          return "All lists does not have a common element"
      elif j in rand[i] and j not in comp:
        comp.append(j)
      
        
  return comp
  

# print(multiCompList(5))

# D

def longestEven(list):
  longest = 0
  current = 0
  cur_lst = []
  lst = []

  for i in list:
    if i % 2 == 0:
      cur_lst.append(i)
      current += 1

    else:
      if len(cur_lst) > len(lst):
        lst = cur_lst
        cur_lst = []
      else:
        pass
      if current > longest: 
        longest = current
        
      
      current = 0
        
  
  return list.index(lst[0]), longest


# print(longestEven([4,3,3,6,2,6,8,3,4,3,3]))







