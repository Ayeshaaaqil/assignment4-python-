## Problem Statement 27

# Print 10 random numbers in the range 1 to 100.
# Here is an example run:
# 45
# 79

# Each time you run your program you should get different numbers
# 81
# 76
# Recall that the python random library has a function randint which returns an integer 
# in the range set by the parameters (inclusive). For example this call would produce a 
# random integer between 1 and 6, which could include 1 and could include 6:


import random

N_NUMBERS: int = 17
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints 17 random numbers in the range 1 to 100.
    """
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

if __name__ == '__main__':
    main()
