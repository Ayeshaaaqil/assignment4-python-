## Problem Statement 3

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) 
# and outputs the temperature converted to Celsius.

def main():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celcius = (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature: {fahrenheit}F = {celcius}C")

if __name__ == '__main__':
    main()

