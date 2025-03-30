import pass_strength
import pass_salt_hash
import string

def graphic():
    
    print("""
    +        PASSWORD VALIDATOR        +
    
    This program helps you validate, salt, and hash passwords.
    """)
    

def menu():
    
    print("""
    Choose an option:
    1. Check password strength
    2. Salting and Hashing password
    3. Exit
    """)

    choice = input("Enter choice (1-3): ")

    if choice == '1':
        print("""
        A secure password should have the following:
        1. Minimum length of 8 characters
        2. Atleast one lowercase character
        3. Atleast one uppercase characeter
        4. Atleast one special character
        5. Atleast on digit
        (CAUTION: Do not have multiple digits in increasing order.
        It makes the password vulnerable to brute-force attacks).
        """)
        password = input("Enter password: ")
        print(pass_strength.check_pass(password))
        menu()
    elif choice == '2':
        print("""
        Hash makes sure that the original password is not stored directly. 
        Even if the database is compromised, passwords 
        cannot be directly retrieved.
        """)
        password = input("Enter password: ")
        password_data = pass_salt_hash.hash(password)
        print(f"Salt: {password_data['salt']}")
        print(f"Hashed Password: {password_data['hashed_pass']}")
        menu()
    elif choice == '3': 
        print("Exiting program")
        return
    else:
        print("invalid choice. Please enter a valid option.")
        menu()

if __name__ == "__main__":
    graphic()
    menu()

