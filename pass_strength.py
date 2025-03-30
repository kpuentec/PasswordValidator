import string

def check_pass(password):
    has_upper =  any(char.isupper() for char in password)
    has_lower =  any(char.islower() for char in password)
    has_digit =  any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_consecutive = any(
        password[i:i+3].isdigit() and
        int(password[i+1]) == int(password[i]) + 1 and
        int(password[i+2]) == int(password[i+1]) + 1
        for i in range(len(password)-2)
    )

    score = 0


    if len(password) >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if has_consecutive:
        score -= 1

    if score >=5:
        return "Your password is Very Strong!"
    elif score == 4:
        return "Your password is Strong!"
    elif score >= 3:
        return "Your password is Medium, but it could use some improvement."
    else:
        return "Your password is Weak, please improve it by adding a mix of" \
        " characters."

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_pass(password))
