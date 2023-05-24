# A
def string1(str):
  print(str[::4])

# string1("I Was Told There'd Be Cake")


# def string(str):
#   new_str = ""
#   for i, j in enumerate(str):
#     if i % 4 == 0:
#       new_str += j
#     else:
#       pass
#   print(new_str)

# string("I Was Told There'd Be Cake")

# B

def twoLastElem(list):
  new_str = ""
  for i in list:
    if len(i) > 1:
      new_str += i[-2:]
    else:
      pass
  print(new_str)
twoLastElem(["banan","propan","Westerosi"])


# C

#Kodesnutt 1
# streng = "I Want Cake"
# Kan ikke bruke denne formateringen for å endre strengen
# streng[7:] = "Cupcake"
# Kan gjøre slik:
# streng = streng[:7:]
# streng = streng + "Cupcake"
# eller bruke replace
# streng = streng.replace("Cake", "Cupcake")
# print(streng)

 
#Kodesnutt 2 er riktig, men kan skrive [-4:] også
# streng = "I Want Cake"
# streng = streng[-4:100:]
# print(streng)

#Kodesnutt 3
# streng = "I Want Cake"
#Mangler index i streng[]
# streng = streng[]
# print(streng)