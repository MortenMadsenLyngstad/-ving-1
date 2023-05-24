def a():
  print('''INFO  
Dette programmet besvarer om din utleie av egen bolig er skattepliktig. 
Først trenger vi å vite hvor stor del av boligen du har leid ut.
Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
20 en mindre del av boligen som f.eks. en hybel.''')

  print("DATAINNHENTING:")

  rent = int(input("Oppgi hvor mye av boligen som ble utleid: "))

  if rent < 50:
    print("SKATTEBEREGNING:\nInntekten er ikke skattepliktig")
  elif rent > 50:
    income = int(input("Skriv inn hva du har hatt i leieinntekt: "))
    if income < 20000:
     print("SKATTEBEREGNING:\nInntekten er ikke skattepliktig")
    elif income > 20000:
      print(f'SKATTEBEREGNING:\nInntekten er skattepliktig\nSkattepliktig beløp er {income}')
    

# a()


def b():
  print('''INFO
Dette programmet besvarer om din utleie en annen type bolig,
her sekundær- eller fritidsbolig, er skattepliktig.
Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.''')

  print("DATAINNHENTING:")
  housing = input("Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut: ")

  if "sekundærbolig" in housing:
    print('''INFO
Du har valgt sekundærbolig.
Nå trenger vi først å vite om sekundærboligen(e) primært brukes til utleie eller fritid.
Deretter trenger vi å vite hvor mange sekundærboliger(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. sekundærbolig.''')

    num = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    rent = int(input("Skriv inn utleieinntekten pr. sekundærbolig: "))
    tax = 0.4

    print("Inntekten er skattepliktig")
    print(f'Skattepliktig beløp er {int((rent*tax)*num)}kr --> 40 prosent av utleieinntekten per bolig')

  elif "fritidsbolig" in housing:
    print('''INFO
Du har valgt fritidsbolig.
Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.
Deretter trenger vi å vite hvor mange fritidsbolig(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.''')


    purpose = input("Skriv inn formålet med fritidsboligen(e) - Fritid/Utleie: ")
    num = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    rent = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))

    if purpose.lower() == "utleie":
      tax = rent * 0.4

      print(f'''Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {rent}kr
Skattepliktig inntekt pr. fritidsbolig er {int(tax)}kr
Totalt skattepliktig beløp er {int(tax * num)}kr''')

    elif purpose.lower() == "fritid" and rent < 10000:
      print("Inntekten er ikke skattepliktig")
    
    elif purpose.lower() == "fritid" and rent >= 10000:
      over = rent - 10000
      tax = over * 0.85
      print(f'''Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {over}kr
Skattepliktig inntekt pr. fritidsbolig er {int(tax)}kr
Totalt skattepliktig beløp er {int(tax * num)}kr''')


# b()


def c():
  print('''INFO  
Dette programmet besvarer om din utleie av egen bolig er skattepliktig. 
Først trenger vi å vite hvilken type bolig du har leid ut.''')

  rent_out = input("Hva leier du ut? (egen bolig / sekundærbolig / fritidsbolig): ")

  if "egen" in rent_out:
    print('''Du har valgt egen bolig.
Vi trenger å vite hvor stor del av boligen du har leid ut.
Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
20 en mindre del av boligen som f.eks. en hybel.''')

    print("DATAINNHENTING:")

    rent = int(input("Oppgi hvor mye av boligen som ble utleid: "))

    if rent < 50:
      print("SKATTEBEREGNING:\nInntekten er ikke skattepliktig")
    elif rent > 50:
      income = int(input("Skriv inn hva du har hatt i leieinntekt: "))
    if income < 20000:
      print("SKATTEBEREGNING:\nInntekten er ikke skattepliktig")
    elif income > 20000:
      print(f'SKATTEBEREGNING:\nInntekten er skattepliktig\nSkattepliktig beløp er {income}')

  
  elif "sekundær" in rent_out:
    print('''Du har valgt sekundærbolig.
Nå trenger vi å vite hvor mange sekundærboliger(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. sekundærbolig.''')

    print("DATAINNHENTING:")

    num = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    rent = int(input("Skriv inn utleieinntekten pr. sekundærbolig: "))
    tax = 0.4

    print("Inntekten er skattepliktig")
    print(f'Skattepliktig beløp er {int((rent*tax)*num)}kr --> 40 prosent av utleieinntekten per bolig')


  elif "fritid" in rent_out:
    print('''Du har valgt fritidsbolig.
Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.
Deretter trenger vi å vite hvor mange fritidsbolig(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.''')

    print("DATAINNHENTING:")

    purpose = input("Skriv inn formålet med fritidsboligen(e) - Fritid/Utleie: ")
    num = int(input("Skriv inn antallet fritidsboliger du leier ut: "))
    rent = int(input("Skriv inn utleieinntekten pr. fritidsbolig: "))

    if purpose.lower() == "utleie":
      tax = rent * 0.4

      print(f'''Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {rent}kr
Skattepliktig inntekt pr. fritidsbolig er {int(tax)}kr
Totalt skattepliktig beløp er {int(tax * num)}kr''')

    elif purpose.lower() == "fritid" and rent < 10000:
      print("Inntekten er ikke skattepliktig")
    
    elif purpose.lower() == "fritid" and rent >= 10000:
      over = rent - 10000
      tax = over * 0.85
      print(f'''Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {over}kr
Skattepliktig inntekt pr. fritidsbolig er {int(tax)}kr
Totalt skattepliktig beløp er {int(tax * num)}kr''')

    else:
      print("OBS - skriv inn en av verdiene som er listet")

  else:
    print("OBS - skriv inn en av verdiene som er listet")


c()