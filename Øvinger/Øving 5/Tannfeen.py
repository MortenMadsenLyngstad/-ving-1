teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
money = []


def tannfeen():
  
  for i in range(len(teeth)): 
    addLst = []
    elem = teeth[i]
    # print(i, elem)
    if elem // 20 > 0:
      addLst.append(elem // 20)
      elem = elem % 20  
    else:
      addLst.append(0)

    if elem // 10 > 0:
      addLst.append(elem // 10)
      elem = elem % 10
    else:
      addLst.append(0)

    if elem // 5 > 0:
      addLst.append(elem // 5)
      elem = elem % 5
    else:
      addLst.append(0)

    if elem // 1 > 0:
      addLst.append(elem // 1)
      elem = elem % 1
    else:
      addLst.append(0)

    money.append(addLst)
      
       
    
  print(money)

tannfeen()
# remover = [[4, 1, 1, 0], [5, 0, 0, 3], [3, 1, 0, 1], [4, 1, 1, 4], [5, 1, 0, 4], [3, 0, 0, 4],  
# [4, 1, 1, 0], [2, 1, 0, 3], [4, 1, 1, 2], [5, 1, 0, 4], [5, 0, 1, 4], [0, 1, 0, 1],  
# [0, 0, 0, 2], [1, 0, 0, 1], [2, 0, 1, 0], [0, 0, 0, 2], [1, 0, 1, 1], [4, 0, 0, 1],  
# [2, 1, 0, 4], [0, 1, 0, 4], [5, 1, 1, 3], [5, 0, 1, 3], [5, 1, 1, 2], [1, 0, 1, 2],  
# [5, 1, 1, 0], [2, 0, 0, 3], [3, 1, 0, 0], [2, 1, 1, 3], [5, 0, 1, 2]]
# money.remove(remover)

# print(money)