num = int(input("Hvilket nummer er i fibonacci tallfølgen vil du ha ut? "))

def a():
  # gjør num-variabelen til en global variabel slik at den kan brukes inne i funksjonen
  global num

  # if-setning med elif printer ut en feilmelding, eller hvis de vil ha ut en av de to første tallene i rekken
  if num < 0:
    print("Skriv inn et positivt heltall")

  elif num == 0:
    print(f'Tall nr  {num} i fibonacci-tallfølgen er 0')

  elif num == 1:
    print(f'Tall nr  {num} i fibonacci-tallfølgen er 1')

  else:   
    def fib(k):
      # counter-variabel som oppdateres i enden av for-løkken senere i programmet
      counter = 0
      # definerer de to første tallene i følgen
      f_0, f_1 = 0, 1

      # while-løkke som kjører så lenge counter er mindre enn k-argumentet
      while counter < k:

        # bruker yield som returnerer f_0 hver gang løkken kjøres
        # dette oppdaterer verdien av f_0 slik at vi kan regne videre ut i tallfølgen
        yield f_0
        # oppdaterer verdiene for f_0 og f_1 variabelene 
        f_0, f_1 = f_1, f_0 + f_1
        
        # oppdaterer counter-verdien
        counter += 1

    # kaller på funksjonen med argumentet num
    fib(num)

    # liste med alle tallene fra for-løkken
    fib_num = list(fib(num))

    # siste tallet i listen
    print(f'Det {num}te fibonaccitallet er: {fib_num[-1]}\n')

    # summerer opp alle tallene frem til num
    print(f'Summen opp til det {num}te fibonaccitallet er: {sum(fib_num)}\n')

    # printer ut liste med alle tallene opp til num
    print(f'Liste over alle tallene opp til det {num}te fibonaccitallet:\n{fib_num}')


a()

