"""
Write a program (doesn't have to be a function, but can be) that reads what's in sample.txt and prints it to the console.
"""

txt = open('sample.txt', 'r')

with txt as open:
  for line in txt:
    print(line)