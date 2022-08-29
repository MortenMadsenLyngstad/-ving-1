def vitnot_a():

  av_kon = 6.022e23

  stoff = input("Si et stoff du er i besittelse av: ")
  molvekt = int(input(f'Hva er molvekten i gram for {stoff}? '))
  vekt = int(input(f'Hvor mange gram {stoff} har du? '))

  ant_mol = (vekt/molvekt)*av_kon

  print(f'Du har {format(ant_mol,".1e")} molekyler {stoff}')

# vitnot_a()

def vitnot_b():

  mel_lin = 8.25e19

  kjent = int(input("Hvor mange ulike 10-toners melodilinjer har du komponert/hørt?"))

  prosent = (kjent)/(mel_lin * 100)

  print(f'Du har hørt {format(prosent,".3e")} prosent av melodier som er mulig!')


# vitnot_b()