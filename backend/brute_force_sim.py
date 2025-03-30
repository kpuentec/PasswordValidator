import time
import string

def estimate_brute_force_time(password, charset):
    attempts_per_second= 1000000
    total_combos = len(charset) ** len(password)
    estimated_seconds = total_combos / attempts_per_second
    estimated_hours = estimated_seconds / 3600
    return estimated_hours

def brute_force(target_password, charset):
    password_length = len(target_password)
    total_combos = len(charset) ** password_length

    print(f"\nEstimated time to brute force: {estimate_brute_force_time(target_password, charset):.2f} hours")

    if estimate_brute_force_time(target_password, charset) > 1:
        confirm = input("\nThis may take over an hour. Are you sure? (y/n): ")
        if confirm.lower() != 'y':
            return "Brute force aborted."

        confirm_again = input("\nFinal warning! This will take a long time. Proceed? (y/n): ")
        if confirm_again.lower() != 'y':
            return "Brute force aborted."

    start_time = time.time()
    attempts = 0

    for password in generate_combos(charset, password_length):
        attempts += 1
        if password == target_password:
            return f"Password found: {password}, Attempts: {attempts}, Time taken: {time.time() - start_time:.4f} seconds"

        # Allow the user to cancel mid-process
        if attempts % 100000 == 0:
            user_input = input(f"Attempts: {attempts}. Type 'cancel' to stop or press Enter to continue: ")
            if user_input.lower() == 'cancel':
                return "Brute force process cancelled by user."
        
def generate_combos(charset, length):
    if length == 1:
        for char in charset:
            yield char
    else:
        for char in charset:
            for sub in generate_combos(charset, length - 1):
                yield char + sub

if __name__ == "__main__":
    password = input("Enter the password to crack: ")
    charset = string.ascii_lowercase + string.digits
    print(brute_force(password, charset))