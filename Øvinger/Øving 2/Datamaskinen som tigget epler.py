def a_b_c():
  print("Dette er et program for å teste din sjenerøsitet.")

  har_epler = int(input("Hvor mange epler har du? "))

  if har_epler == 0:
    print("Æsj, det sier du bare for å slippe å gi noe!")
    
  elif har_epler > 0 :
    gir_epler = int(input("Hvor mange kan du gi til meg? "))

    if gir_epler > har_epler:
      print("Du har nå 0 epler igjen. Gi meg de", abs(har_epler - gir_epler), "du skylder meg neste gang vi møtes.")

    elif gir_epler < har_epler / 2:
      if har_epler - gir_epler == 1:
        print("Du beholder det meste for deg selv...")
        print("Du har nå", har_epler - gir_epler, "eple igjen.")
      else:
        print("Du beholder det meste for deg selv...")
        print("Du har nå", har_epler - gir_epler, "epler igjen.")

    else:
      if har_epler - gir_epler == 1:
        print("Takk, det var snilt!")
        print("Du har nå", har_epler - gir_epler, "eple igjen.")
      else:
        print("Takk, det var snilt!")
        print("Du har nå", har_epler - gir_epler, "epler igjen.")

a_b_c()