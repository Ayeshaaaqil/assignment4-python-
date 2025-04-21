## Problem Statement 31

# You want to be safe online and use different passwords for different websites. 
# However, you are forgetful at times and want to make a program that can match which 
# password belongs to which website without storing the actual password!

# This can be done via something called hashing. Hashing is when we take something and 
# convert it into a different, unique identifier. This is done using a hash function. 
# Luckily, there are several resources that can help us with this.
# For example, using a hash function called SHA256(...) something as simple as 
# hello
# can be hashed into a much more complex 
# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    email: the email we are checking the password for
    stored_logins: a dictionary pointing from an email to its hashed password
    password_to_check: a password we want to test alongside the email to login with
    """
    
    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

# There is no need to edit code beyond this point

def hash_password(password):
    """
    Takes in a password and returns the ASH256 hashed value for that specific password.
    
    Inputs:
        password: the password we want
    
    Outputs:
        the hashed form of the input password
    """

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "87bgfrtw9hbzxgft635b4eincx5rfvizkwg",
        "code_in_placer@cip.org": "c8gbxszkn345734vdjo2myt3840kjk",
        "student@stanford.edu": "765fbfi8h38t3vxjh992nisn2y7hbxiu"
    }
    
    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))
    
    print(login("code_in_placer@cip.org", stored_logins, "leech"))
    print(login("code_in_placer@cip.org", stored_logins, "leech"))
    
    print(login("student@stanford.edu", stored_logins, "password"))
    print(login("student@stanford.edu", stored_logins, "987@654!321"))


if __name__ == '__main__':
    main()
