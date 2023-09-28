def countdown(n): # the countdown() print blastoff if n is less or equal than 0
    if n <= 0: 
        print('Blastoff!') 
    else:   # if n takes a positive value, the function uses a recursion to start the count
          print(n) 
          countdown(n-1) # in the next step, n is rested 1 and n is printed, and so on 
                        # untl n becomes into Zero, at this moment the countdown() shows blastoff


def countup(n): # the countup() works in the inverse way than the countdown()
  if n >= 0:   # if n is a positive number or Zero, it shows blastoff
      print('Blastoff!') 
  else: # if n is a negative number, n is printed and the recursion is used, adding a unit to n
        # This causes n start to decrease
    print(n) 
    countup(n+1) 

# I convert on INT the value taken from the keyboard, n is the  int number where going to begin the count
n = int(input('type an integer you want to start the count to Zero: ' ))
if n >= 0: # for Positive numbers I use the countup()
  countdown(n)
elif n <= 0: # for negative numbers I use the countup()
  countup(n)
else: # I used the else if the number is Zero,
  countup(n) #  the behavior of the 2 functions is the same for the value of Zero, is the same
              # If we use countup or countdown()


