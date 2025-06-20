## Problem Statement 24

# Write a program which asks a user for their age and lets them know if they can 
# or can't vote in the following three fictional countries. Around the world, 
# different countries have different voting ages. In the fictional countries of 
# Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different the voting
#  age in Peturksbouipo is 20 (in real life, this is the voting age in, for example,
#  Scotland, Ethiopia, and Austria) the voting age in Stanlau is 40 (in real life
#  this is the voting age in the United Arab Emirates) the voting age in Mayengua 
# is 58 (in real life, as far as we can tell, this isn't the voting age anywhere)

PETURKSBOUIPO_AGE : int = 20
STANLAU_AGE : int = 40
MAYENGUA_AGE : int = 58

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    
    # Check if the user can vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    
    # Check if user can vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
