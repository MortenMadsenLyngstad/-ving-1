def ex_prices():
  days = int(input("Hvor mange dager til du skal reise? "))

  if days >= 14:
    print("Minipris 199,- kan ikke refunderes/endres")
    answer = input("Ønskes dette J/N ? ")

    if answer.lower() == "j":
      print("Takk for pengene, god reise!")

    # her kan man gjøre koden kortere ved å legge sammen over 60 og militær/student, men da må kunden svare på flere spørsmål
    elif answer.lower() == "n":
      age = int(input("Skriv inn din alder: "))

      if age < 16:
        price = 440 * 0.5
        print(f'Da får du 50% rabatt, og må betale {price}')

      elif age > 60:
        price = 440 * 0.75
        print(f'Da får du 25 % rabatt, og må betale {price}')

      else:
        mil_stud = input("Er du militær eller student? J/N: ")

        if mil_stud.lower() == "j":
          price = 440 * 0.75
          print(f'Da får du 25 % rabatt, og må betale {price}') 

        else:
          print("Da tilbyr vi fullpris: 440,-")

  elif days < 14:
    age = int(input("Skriv inn din alder: "))

    if age < 16:
      price = 440 * 0.5
      print(f'Da får du 50% rabatt, og må betale {price}')

    elif age > 60:
      price = 440 * 0.75
      print(f'Da får du 25 % rabatt, og må betale {price}')

    else:
      mil_stud = input("Er du militær eller student? J/N: ")

      if mil_stud.lower() == "j":
        price = 440 * 0.75
        print(f'Da får du 25 % rabatt, og må betale {price}') 

      else:
          print("Da tilbyr vi fullpris: 440,-")
    

ex_prices()


# mulighet for ekstra oppgave, men må tolke oppgaven - skjønner ikke hva han mener.