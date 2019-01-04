#TODO: print at the end the highest number that occured & the number of steps it took to get to 1
#TODO: implement a memoryList (after the script finishes it should print a list of the numbers
#      that already occured/tested) that you can add to the same memoryList so that the next time
#      the script is run it would ignore already tested numbers.
# i am running in an endless loop when i add the .append code within the collatz function.
# one idea is
# 1: ask if you want to use the testedNumbers list before starting.
# 2: when you encounter a tested number ask to skip or not.
print('''The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
      start with any positive integer n. Then each term is obtained from the previous term as follows:
      if the previous term is even, the next term is one half the previous term.
      If the previous term is odd, the next term is 3 times the previous term plus 1.
      The conjecture is that no matter what value of n, the sequence will always reach 1.''')

print('more information here: https://en.wikipedia.org/wiki/Collatz_conjecture')
# https://trinket.io/python/d3bdba0162
# https://github.com/Liyannis/Collatz

def collatz(value):
    testedNumbersCheck(value)
    while value != 1:
        test = odd_or_even(value)
        if test == 0:
            value = (value // 2)
            testedNumbersCheck(value)
        elif test == 1:
            value = (3 * value + 1)
            testedNumbersCheck(value)
        continue



def odd_or_even(number):
    num_test = (number % 2)
    if num_test == 2 or num_test == 0:
        print(number, 'even')
        return num_test
    elif num_test == 1:
        print(number, 'odd')
        return num_test
    


# TODO
def runMode():
    '''ask user if he wants to use:
       A) handsfree approach & watch the numbers,
       B) check for already tested numbers in the testedNumbers list
       C) run for a single number''' 
    print('''Hello, this script supports 3 ways to run the Collatz conjecture.\n
          in what mode do you want to run the script?\n
          1: Full auto
          2:
          3: ''')
    uC = int(input()) #userChoice
    if uC == 1:
        global full_auto_on
        full_auto_on = 1
        fullAuto()
    elif uC == 2:
        pass
    elif uC == 3:
        pass
        

def fullAuto():
    while True:
#        testedNumbers.sort()
        for n in range(1, len(testedNumbers)):
            if n in testedNumbers:
                n += 1
                if n not in testedNumbers:
                    collatz(n)
                else:
                    pass
            else:
                pass



YES = ['y', 'Y']
testedNumbers = []
full_auto_on = 0
def testedNumbersCheck(value):
    if full_auto_on == 1:
        if value in testedNumbers:
            print('skipping ' + str(value) + ' as it has been tested')
        else:
            pass
    elif value in testedNumbers:
        print('number ' + str(value) + ' has been tested in the past')
        print('Do you want to stop?')
        print('y/Y to stop or press Enter to continue')
        userAnswer = input('')
        if userAnswer in YES:
            print('''if you want to rerun the script but not compute
                     for the numbers that you already tested, \n
                     then simply copy-paste the testedNumbers below into the code''')
            print(testedNumbers)
            exit()
        else:
            value += 1
            return value
    else:
        testedNumbers.append(value)
        

#User input validation
def userInNumVal(): #userInputNumberValidation
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



collatz(userInNumVal())
print('end')
#print('''if you want to rerun the script but not compute for the numbers that you already tested, \n
#         then simply copy-paste the testedNumbers below into the code''')
#print(testedNumbers)
runMode()