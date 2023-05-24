import binascii
 
def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)


def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')




def encrypt(message, key):
  string1 = toHex(bytes(message, encoding = 'ascii'))
  string2 = toHex(bytes(key, encoding = 'ascii'))

  code = string1 ^ string2


  return code, string2

# print((encrypt("hei", "abc")))


def decrypt(code_key):
  code, key = code_key
  message = code ^ key
  
  message = toString(message)

  return message

# print(decrypt(encrypt("hei", "abc")))


def main():
  message = input("Enter message: ")
  lst_msg = message.split()
  crypto_lst = []
  for i in range(len(lst_msg)):
    crypto_lst.append(toHex(bytes(lst_msg[i], encoding = 'ascii')))

  crypto = ' '.join(str(e) for e in crypto_lst)
  crypto_joined = crypto.replace(' ', '')

  print(f'Encrypted message: {crypto_joined}\nMessage: {message}')


main()



# D (frivillig)
# Dersom samme nøkkel blir brukt til å kryptere to forskjellige ord kan man bruke resultatet og en "ordbok" til å finne tilbake til de opprinnelige ordene, og derfor også nøkkelen. Forklar hvordan dette kan gjøres
#  Hvis vi vil finne nøkkelen og har to krypterte ord som er kryptert med den nøkkelen, kan vi bruke XOR-operatoren på de to ordene og få ut nøkkelen ? Litt usikker på hvordan man kan gjøre dette.




