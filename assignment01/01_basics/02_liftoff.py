## Problem Statement 54

# Write a program that prints out the calls for a spaceship that is about to launch.
#  Countdown from 10 to 1 and then output Liftoff!
# Here's a sample run of the program:
# 10
# 9
# 8
# Liftoff!

# There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. Recall that i will keep track of how many times the for loop has completed executing its body. As an example this code:

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i)
    
    # Print Liftoff!
    print("Liftoff!")

if __name__ == '__main__':
    main()
