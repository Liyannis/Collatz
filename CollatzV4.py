#TODO: print at the end the highest number that occured & the number of steps it took to get to 1
#TODO: implement a memoryList (after the script finishes it should print a list of the numbers
#      that already occured/tested) that you can add to the same memoryList so that the next time
#      the script is run it would ignore already tested numbers.

print('''The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
      start with any positive integer n. Then each term is obtained from the previous term as follows:
      if the previous term is even, the next term is one half the previous term.
      If the previous term is odd, the next term is 3 times the previous term plus 1.
      The conjecture is that no matter what value of n, the sequence will always reach 1.''')

print('more information here: https://en.wikipedia.org/wiki/Collatz_conjecture')
# https://trinket.io/python/d3bdba0162
# https://github.com/Liyannis/Collatz

memoryList = []



def collatz(value):
    while value != 1:
        if value in memoryList:
#            print('this number has been tested in the past: ' + str(value))
            pass
        elif odd_or_even(value) == 0:
            value = (value // 2)
            print(value, 'even')
            memoryList.append(value)
        elif odd_or_even(value) == 1:
            value = (3 * value + 1)
            print(value, 'odd')
            memoryList.append(value)
        continue

def odd_or_even(intNumber):
    num_test = (intNumber % 2)
    if num_test == 2 or num_test == 0:
        return num_test
    elif num_test == 1:
        return num_test

#User input validation
def userInValNum(): #userInputValidationNumber
    Pass = None
    while Pass != 1:
        userIn = input('Type a positive integer number: ')
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
print('if you want to rerun the script but not compute for the numbers that you already tested, \nthen simply copy-paste the memoryList below into the code')
print(memoryList)
