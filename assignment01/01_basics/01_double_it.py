## Problem Statement 53

# Write a program that asks a user to enter a number. Your program will then double 
# that number and print out the result. It will repeat that process until the value 
# is 100 or greater.
# For example if the user enters the number 2 you would then print:
# 4
# 8
# 16
# Note that: 
# 2 doubled is 4
# 4 doubled is 8
# 8 doubled is 16
# and so on.

# We stop at 128 because that value is greater than 100.
# Maintain the current number in a variable named curr_value. When you double the number, 
# you should be updating curr_value. Recall that you can double the value of curr_value 
# using a line like:
# This program should have a while loop and the while l
# oop condition should test if curr_value is less than 100. Thus,
#  your program will have the line:

def main():
    # Ask the user for input
    curr_value = int(input("Enter a number: "))

    # Loop until the value reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)  # Print the doubled value

if __name__ == '__main__':
    main()
