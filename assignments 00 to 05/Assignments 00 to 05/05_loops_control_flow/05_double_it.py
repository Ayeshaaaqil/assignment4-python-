## Problem Statement 36

# Write a program that asks a user to enter a number. Your program will then double that 
# number and print out the result. It will repeat that process until the value is 100 
# or greater.

# For example if the user enters the number 2 you would then print:

# 4
# 8
# 16
# 2 doubled is 4
# 4 doubled is 8
# 8 doubled is 16
# and so on.
# We stop at 128 because that value is greater than 100.
# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

import random

N_NUMBERS, MIN_VALUE, MAX_VALUE = 10, 1, 100

def main():
    print(*[random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)], sep='\n')
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))
    fruit_list.append('mango')
    print(fruit_list)
    
    # Countdown from 10 to 1 and then output Liftoff!
    for i in range(10, 0, -1):
        print(i)
    print("Liftoff!")
    
    # Ask user for a number and double it until it reaches 100 or more
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)

if __name__ == '__main__':
    main()

