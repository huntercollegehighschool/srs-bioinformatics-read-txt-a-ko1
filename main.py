import os
program = input("A or B?").upper()

while program not in ["A", "B"]:
  os.system('clear')
  print("Invalid input.")
  program = input("A or B?").upper()

if program == "A":
  import Asampleread

elif program == "B":
  import Baminoacids
  protein = input("Enter the protein: ")
  print(Baminoacids.weightedstring(protein))
  