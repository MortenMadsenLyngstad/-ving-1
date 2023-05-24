l = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]

# A
def bubble_sort(list):
  if list is not sorted(list):
    for i in range(len(list)):
      for j in range(len(list)-1):
        if list[j] > list[j+1]:
          list[j], list[j+1] = list[j+1], list[j]
  
  return list


# print(bubble_sort(liste))

# B
def selection_sort(list):
  l2 = []
  for _ in range(len(list)):
    l2.append(max(list))
    l.remove(max(list))
  return sorted(l2)

print(selection_sort(l))


# C

# Vil tro metode 1 er den raskeste fordi da slipper man å appende til en liste og remove fra en annen
# I metode 1 bytter man bare plass på to verdier.

