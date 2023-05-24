def write_to_file(data):
  with open("my_file.txt", "w") as f:
    f.write(data)

write_to_file("String")


def read_from_file(filename):
  with open(filename, "r") as f:
    return f.read()

print(read_from_file("my_file.txt"))

def main():
  filename = "my_file.txt"
  while True:
    choice = input("w, r or done? ")
    if choice.lower() == "w":
      sentence = input("Write to file: ")
      write_to_file(sentence)
      print(sentence)
    elif choice.lower() == "r":
      print(read_from_file(filename))
    elif choice.lower() == "done":
      print("You are done")
      break

main()