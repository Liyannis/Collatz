print('''The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
      start with any positive integer n. Then each term is obtained from the previous term as follows:
      if the previous term is even, the next term is one half the previous term.
      If the previous term is odd, the next term is 3 times the previous term plus 1.
      The conjecture is that no matter what value of n, the sequence will always reach 1.''')

print('more information here: https://en.wikipedia.org/wiki/Collatz_conjecture')

def collatz(value):
    while value != 1:
        if odd_or_even(value) == 0:
            value = (value // 2)
            print(value, 'even')
        elif odd_or_even(value) == 1:
            value = (3 * value + 1)
            print(value, 'odd')
        continue

def odd_or_even(intNumber):
    num_test = (intNumber % 2)
    if num_test == 2 or num_test == 0:
        return num_test
    elif num_test == 1:
        return num_test

##def user_guidance(value):
##    value = int(value)
##    if value == 1:
##        print('if you input 1 the script will stop running as it outputs 1.')
##    elif value == 0:
##        print('with 0 as an input the script will be stuck in an endless loop')
##    elif value <= 0:
##        print("negative numbers end up in a never ending loop")
##    elif value >= 2:
##        collatz(value)

#A function to get the users input
def userInput():
    print('Type a positive integer number: ')
    return input()

#User input validation
def userInValNum(): #userInputValidationNumber
    Pass = None
    while Pass != 1:
        userIn = userInput()
        try:
            int(userIn)
        except ValueError:
            print('oups something went wrong, try again')
            Pass = 0
        else:
            value = int(userIn)
            if value == 1:
                print('if you input 1 the script will stop running as it outputs 1.')
            elif value == 0:
                print('with 0 as an input the script will be stuck in an endless loop')
            elif value <= 0:
                print("negative numbers end up in a never ending loop")
            elif value >= 2:
                return int(userIn)


collatz(userInValNum())
print('end')