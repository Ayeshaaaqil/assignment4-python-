## Problem Statement 35

# Write a program that prints out the calls for a spaceship that is about to launch. 
# Countdown from 10 to 1 and then output Liftoff!

# Here's a sample run of the program:
# 10
# 9
# 8
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

if __name__ == '__main__':
    main()
