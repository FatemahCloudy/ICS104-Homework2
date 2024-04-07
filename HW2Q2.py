#once you finish uncomment this line to create python file HW2Q2.py
# Your code for Question 2 in this cell

#HW2 - Q2
# Get a binary code from user
Binary = input("Enter a binary code")
# Nake sure it is a binary code
isBinary = True
if Binary.isalpha():
    print('Please do not enter letters')
if Binary.isdigit():
    for i in range (2,10):
      i = str(i)
      if i in Binary:
        print("Please do not enter digits other than 0 or 1")
        isBinary = False
    if isBinary: # Onse everything is alright, go on with the code
      parity = input ("Enter parity type 'e' for even, 'o' for odd : ")
      parity = parity.lower() # Lower the input because python is case sensetive
     # Use if statment for the steps explained in the question
      if parity == 'e':
            if Binary.count('1') % 2 == 0:
              print ('0' + Binary)
            elif Binary.count('1') % 2 != 0:
              print ('1' + Binary)
      elif parity == 'o':
            if Binary.count('1') % 2 == 0:
                print ('1' + Binary)
            elif Binary.count('1') % 2 != 0:
                print ('0' + Binary)
      else:
        print ('Wrong input') # if the parity type entered was neither e nor o, print an erer messege
# End
