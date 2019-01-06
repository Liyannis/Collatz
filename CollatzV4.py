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
      The conjecture is that no matter what number of n, the sequence will always reach 1.''')

print('more information here: https://en.wikipedia.org/wiki/Collatz_conjecture')
# V3   https://trinket.io/python/d3bdba0162
# V4.2 https://trinket.io/python/c5d06fac04
# https://github.com/Liyannis/Collatz

def collatz(number):
    while number != 1 and testedNumbersCheck(number) != 0:
        test = odd_or_even(number)
        if test == 0:
            testedNumbers.append(number)
            print(number, 'even')
            number = (number // 2)
            if testedNumbersCheck(number) == 0:
                break
        elif test == 1:
            testedNumbers.append(number)
            print(number, 'odd')
            number = (3 * number + 1)
            if testedNumbersCheck(number) == 0:
                break
        continue



def odd_or_even(number):
    num_test = (number % 2)
    if num_test == 2 or num_test == 0:
        return num_test
    elif num_test == 1:
        return num_test
    

YES = ['y', 'Y', 'YES', 'yes']
testedNumbers = []
full_auto_on = 0
def testedNumbersCheck(number):
    if full_auto_on == 1:
        if number in testedNumbers:
            print('skipping ' + str(number) + ' as it has been tested')
            escape_number = 0
            return escape_number
        else:
            pass
    elif number in testedNumbers:
        print('number ' + str(number) + ' has been tested in the past')
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
            number += 1
            return number
    else:
        pass
        

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
            number = int(userIn)
            if number == 1:
                print('if you input 1 the script will stop running as it outputs 1.')
            elif number == 0:
                print('with 0 as an input the script will be stuck in an endless loop')
            elif number <= 0:
                print("negative numbers end up in a never ending loop")
            elif number >= 2:
                return int(userIn)

# TODO
def runMode():
    '''ask user if he wants to use:
       A) handsfree approach & watch the numbers,
       B) check for already tested numbers in the testedNumbers list
       C) run for a single number''' 
    print('''Hello, this script supports 3 ways to run the Collatz conjecture.\n
          in what mode do you want to run the script?\n
          1: Full auto
          2: (not implemented yet) Semi-auto?
          3: (not implemented yet) Manual ''')
    uC = int(input()) #userChoice
    if uC == 1:
        global full_auto_on
        full_auto_on = 1
        fullAuto()
    elif uC == 2:
        pass
    elif uC == 3:
        pass
    else:
        print('Wrong choice, exiting')
        pass
        

def fullAuto():
    while True:
        for n in range(1, len(testedNumbers)):
            if n in testedNumbers:
                n += 1
                if n not in testedNumbers:
                    collatz(n)
                    print_1000()
                else:
                    pass
            else:
                pass


def print_1000():
    if len(testedNumbers) in range(0, 1000000, 50):
        #change the number 1000 if you want a smaller list to print
        print('Do you want to print the tested numbers?')
        print('y/Y to print or press Enter to continue')
        choice = input()
        if choice in YES:
            print(testedNumbers)
            input('Just press Enter to continue')
        else:
            pass


collatz(userInNumVal())
print('end')
#print('''if you want to rerun the script but not compute for the numbers that you already tested, \n
#         then simply copy-paste the testedNumbers below into the code''')
print(testedNumbers)
runMode()