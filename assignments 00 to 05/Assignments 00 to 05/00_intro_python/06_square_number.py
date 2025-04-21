## Problem Statement 6
# Ask the user for a number and print its square (the product of the number times itself).


def main():
    num: float = float(input("Type a number to see its square: ")) 
    print(str(num) + " squared is " + str(num ** 2)) 

if __name__ == '__main__':
    main()