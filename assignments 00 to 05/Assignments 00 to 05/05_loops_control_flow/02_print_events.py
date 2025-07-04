## Problem Statement 33

# Write a program that prints the first 20 even numbers. There are several correct 
# approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:
# 0
# 2
# 4
def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop
   
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()
