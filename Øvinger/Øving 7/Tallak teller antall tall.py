def number_of_lines(filename):
  with open(filename, "r") as f:
    return len(f.readlines())

# print(number_of_lines("numbers.txt"))


def number_frequency(filename):
  freq_num = {}
  with open(filename, "r") as f:
    num = f.read()
    num = num.split()
    for i in range(len(num)):
      if num[i] not in freq_num:
        freq_num[num[i]] = 1
      else:
        freq_num[num[i]] += 1
      
    for i in range(len(freq_num)):
      print(f"{num[i]}: {freq_num[num[i]]}")

number_frequency("numbers.txt")

