# TODO: print at the end the highest number that occured & the number of steps it took to get to 1
# TODO:
# 1: ask if you want to use the testedNumbers list after finishing.
# 2: implement runMode() at the end of the first run & ask what the user want to do next

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
        if (value % 2) == 0:
            value = (value // 2)
            testedNumbersCheck(value)
            print(value, 'even')
        elif (value % 2) == 1:
            value = (3 * value + 1)
            testedNumbersCheck(value)
            print(value, 'odd')
        continue


testedNumbers = []
YES = ['y', 'Y']


def testedNumbersCheck(value):
    if value in testedNumbers:
        print('number ' + str(value) + ' has been tested in the past')
        print('Do you want to stop?')
        print('y/Y to stop or press Enter to continue')
        userAnswer = input('')
        if userAnswer in YES:
            print('''\nif you want to rerun the script but not compute
for the numbers that you already tested,
then simply copy-paste the testedNumbers below into the code \n''')
            print(testedNumbers)
            exit()
        else:
            pass
    else:
        testedNumbers.append(value)


# User input validation
def userInValNum():  # userInputValidationNumber
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


# TODO
def runMode():
    pass
    '''ask user if he wants to use:
       A) Auto mode where the script runs by itself,
       B) Check for already tested numbers in the testedNumbers list
       C) run for a single number'''
    print('''Hello, this script supports 3 ways to run the Collatz conjecture.\n
          in what mode do you want to run the script?\n
          1: Full auto (it will continue indefenetlly)
          2: Semi-auto
          3: Manual''')
    uC = int(input())  # userChoice
    if uC == 1:
        autoMode()
    elif uC == 2:
        pass
    elif uC == 3:
        pass


def autoMode():
    for n in testedNumbers:
        numberOut = n + 1
        if numberOut not in testedNumbers:
            collatz(numberOut)
        else:
            pass
        

collatz(userInValNum())
print('Script finished')
print('''\nif you want to rerun the script but not compute for the numbers that you already tested,
then simply copy-paste the testedNumbers below into the code
find this line "testedNumbers = []" and paste the numbers WITH the [] and rerun the script \n''')
print(testedNumbers)
runMode()