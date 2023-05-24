import math


def recursion_sum(n):
  if n==1:
    return 1
  else:
    return n + recursion_sum(n - 1)

# print(recursion_sum(53))


# make a function that takes inn a list, splits it into two lists, and sums the two parts recursively
# Path: Rekursjon.py
def merge_sum(list):
  if len(list) == 1:
    return list[0]
  else:
    middle = int(len(list)/2)
    return merge_sum(list[:middle]) + merge_sum(list[middle:])

  
# print(merge_sum([1,2,3,4,5,6]))


def find_smallest_element(n):
  if n[0] < n[1]:
    if len(n) == 2:
      return n[0]
    else:
      n.pop(1)
      return find_smallest_element(n)
  else:
    if len(n) == 2:
      return n[1]
    else:
      n.pop(0)
      return find_smallest_element(n)

# print(find_smallest_element([5,3,2,6,7,6,5,1]))  


def binary_search(numbers, element, minimum, maximum):
  binary_search.counter += 1
  if minimum <= maximum:
    middle = int((minimum + maximum)/2)
    if numbers[middle] == element:
      return middle

    elif numbers[middle] > element:
      return binary_search(numbers, element, minimum, middle - 1)

    else:
      return binary_search(numbers, element, middle + 1, maximum)

  else:
    return (-float('inf')), binary_search.counter

binary_search.counter = 0


numbers = [i for i in range(2264)]

print(binary_search(numbers, 220, 0, len(numbers) - 1))


#Bonus
# Hvis tallet ikke er i listen så vil funksjonen kalles ceiling(log(2)) + 1 ganger ||| (For len(n) > 4 iallefall)*
# Dvs at hvis tallet er 1000 vil funksjonen kalles 11 ganger

numbOfFunc = math.ceil(math.log(len(numbers), 2)) + 1 
print(numbOfFunc)
# 
