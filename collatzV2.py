print('''The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
      start with any positive integer n. Then each term is obtained from the previous term as follows:
      if the previous term is even, the next term is one half the previous term.
      If the previous term is odd, the next term is 3 times the previous term plus 1.
      The conjecture is that no matter what value of n, the sequence will always reach 1.''')

print('more information here: https://en.wikipedia.org/wiki/Collatz_conjecture')
# https://github.com/YanSoum/Collatz
#V1.0: https://trinket.io/python/32e27b5beb
#V2.0: https://trinket.io/python/b1adabe04f
#V3.0: https://trinket.io/python/d3bdba0162
#V4.0: https://trinket.io/python/85917cb31d
#V4.1: https://trinket.io/python/c8f3efc641
#V4.2: https://trinket.io/python/c5d06fac04
#V4.3: https://trinket.io/python/8ba4d67136

def odd_or_even(intNumber):
    num_test = (intNumber % 2)
    if num_test == 2 or num_test == 0:
        return num_test
    elif num_test == 1:
        return num_test

def collatz(value):
    while value != 1:
        if odd_or_even(value) == 0:
            value = (value // 2)
            print(value, 'even')
        elif odd_or_even(value) == 1:
            value = (3 * value + 1)
            print(value, 'odd')
        continue

def user_guidance(value):
    if value == 1:
        print('if you input 1 the script will stop running as it outputs 1.')
    elif value == 0:
        print('with 0 as an input the script will be stuck in an endless loop')
    elif value <= 0:
        print("negative numbers end up in a never ending loop")
    elif value >= 2:
        collatz(value)

def num_or_let(value): # function to check if the user input is a number(integer) or a letter(string)
    try:
        value = int(input('Type a positive integer number: '))
    except ValueError:
        print("Letter's are not numbers, read the instructions plz pl0x")
    except TypeError:
        print("?")
    if type(value) == None:
        print("N")
    elif type(value) == int:
        user_guidance(value)


value = None # dummy value
# value = int(input('Type a positive integer number: '))
# user_guidance(value)
num_or_let(value)

