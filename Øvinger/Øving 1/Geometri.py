
def geo_a():
  r = 5
  print(f'Vi har en sirkel med radius {r}')
  omkrets = 2 * 3.14 * r
  print("Omkretsen er", omkrets)
  areal = 3.14 * r ** 2
  print("Arealet er", areal)
  h = 8
  volum = areal * h
  print("Sylinder med høyde", h, ": Volumet er", volum)

# geo_a()


def geo_b():
  r = 5
  print(f'Vi har en sirkel med radius {r}')
  omkrets = 2 * 3.14 * r
  print("Omkretsen er", "{:.2f}".format(omkrets))
  areal = 3.14 * r ** 2
  print("Arealet er", areal)
  h = 8
  volum = areal * h
  print("Sylinder med høyde", h, ": Volumet er", volum)

geo_b()
