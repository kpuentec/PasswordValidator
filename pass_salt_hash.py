import secrets
import bcrypt

def hash(password):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)

    password_data = {
        "salt": salt,
        "hashed_pass": hashed_pass
    }

    return password_data

if __name__ == "__main__":
    password = input("Enter your password: ")
    password_data = hash(password)

    print(f"Salt: {password_data['salt']}")
    print(f"Hashed Password: {password_data['hashed_pass']}") 
    
