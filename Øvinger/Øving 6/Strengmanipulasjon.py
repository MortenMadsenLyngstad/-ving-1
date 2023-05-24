# A

str1 = "iS"
str2 = "Is this the real life? Is this just fantasy?"

# str1 = "oo"
# str2 = "Never let you go let me go. Never let me go ooo"

def find_substring_indexes(str1, str2):
  global num_l
  num_l = []
  str1 = str1.lower()
  str2 = str2.lower()

  for i in range(len(str2)):

    if str1[::] == str2[i:i+len(str1):]:
      num_l.append(i)
    
  return num_l

# print(find_substring_indexes(str1, str2))


# B

def new_str(str1, str2):
  str3 = "cool"
  str1 = str1.lower()
  str2 = str2.lower()
  for i in range(len(str2)):
    if str1[::] == str2[i:i+len(str1):]:
      str2 = str2.replace(str1, str3)
      
  
  return str2

  

print(new_str(str1, str2))
