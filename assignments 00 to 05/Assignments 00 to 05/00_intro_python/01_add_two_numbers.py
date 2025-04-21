 ## Problem Statement 1 

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

def main():
    print("This program adds two numbers.")
    num1: str = input("Enter the first number: ")
    num1: int = int(num1)  
    num2: str = input("Enter the second number: ")
    num2: int = int(num2) 
    sum: int = num1 + num2  
    print("The sum is:", sum)

# Fixing the if condition
if __name__ == "__main__":
    main()
