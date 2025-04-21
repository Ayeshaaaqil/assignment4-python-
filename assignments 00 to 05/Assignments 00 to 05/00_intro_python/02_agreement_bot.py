## Problem Statement 2

# Write a program which asks the user what their favorite flower is, 
# and then always responds with "My favorite flower is also ___!" 
# (the blank should be filled in with the user-inputted flower, of course).
# Asking the user for their favorite flower

def main():
   favorite_flower = input("What's your favorite flower? ")

# Responding with the same flower
   print(f"My favorite flower is also {favorite_flower}!")

if __name__ == '__main__':
    main()
