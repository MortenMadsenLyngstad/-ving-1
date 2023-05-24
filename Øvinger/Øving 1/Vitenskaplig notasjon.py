def vitnot_a():
  # lagrer konstanten gitt i oppgaven som en variabel
  av_kon = 6.022e23

  # spør person om ulike verdier som brukes i utregningen og svaret
  stoff = input("Si et stoff du er i besittelse av: ")
  molvekt = int(input(f'Hva er molvekten i gram for {stoff}? '))
  vekt = int(input(f'Hvor mange gram {stoff} har du? '))

  # bruker inputen og lagrer svaret som en variabel
  ant_mol = (vekt/molvekt)*av_kon

  print(f'Du har {format(ant_mol,".1e")} molekyler {stoff}')

# vitnot_a()

def vitnot_b():

  mel_lin = 8.25e19

  kjent = int(input("Hvor mange ulike 10-toners melodilinjer har du komponert/hørt?"))

  prosent = (kjent)/(mel_lin * 100)

  print(f'Du har hørt {format(prosent,".3e")} prosent av melodier som er mulig!')


# vitnot_b()