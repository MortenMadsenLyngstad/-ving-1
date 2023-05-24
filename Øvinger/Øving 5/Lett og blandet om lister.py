# A
def is_six_at_edge(l):
  if l[0] == 6 or l[-1] == 6:
    return True
  else:
    return False

l = [1, 2, 3, 4, 5, 6]
l2 = [6, 1, 2, 3, 4, 5]
l3 = [1, 2, 3, 4, 5, 6, 7]

# print(is_six_at_edge(l))
# print(is_six_at_edge(l2))
# print(is_six_at_edge(l3))


# B
def average(l):
  return (sum(l) / len(l))

l4 = [1, 3, 5, 7, 9, 11]

# print(average(l4))


# C
def median(l):
  l.sort()
  med = l[len(l) // 2]
  return med

l5 = [1,4,2,5,3]

# print(median(l5))