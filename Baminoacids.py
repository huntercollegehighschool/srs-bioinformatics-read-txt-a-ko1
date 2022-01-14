"""
Define a function weightedstring that takes a string input protein. The function returns the weighted string of that protein based on masstable.txt.

weightedstring should read from masstable.txt. It's helpful to have those masses in a dictionary.
"""
table = open('masstable.txt', 'r')

def weightedstring(protein):
  prot_weighted_strings = {}
  with table as open:
    for dat in table:
      corr_values = dat.split()
      prot_weighted_strings[corr_values[0]] = float(corr_values[1])
  return prot_weighted_strings[protein]

      
