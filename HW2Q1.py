#once you finish uncomment this line to create python file
# Your code for Question 1 in this cell

# HW2 - Q1

Mode = input('Enter calculation mode(0 for epsilon, 1 to specify terms): ')
x = int(input('Enter x: '))
if Mode == '1':
  n = int(input('Enter number of terms to include: '))
  from math import factorial
  if n == 1:
    ex = 1
  elif n == 2:
    ex = 1 + x
  elif n > 2:
    ex = 1 + x
    for i in range (2, n):
      ex += (x**i) / factorial(i)
  print (round(ex, 8))
elif Mode == '0':
  epsilon = float(input('Enter epsilon: '))
  from math import factorial
  term = x
  n = 2
  ex = 1
  while term > epsilon:
      ex += term
      term = (x**n) / factorial(n)
      n += 1
  print (round(ex, 8))
else:
  print ('Wrong input')

#End