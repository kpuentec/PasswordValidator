
# PasswordValidator

PasswordValidator is a Python-based tool designed to evaluate the strength of passwords based on length, complexity, and avoidance of sequential numbers. It includes functions for salting and hashing passwords for secure storage and features a brute-force simulation to estimate the time required to crack a password based on its complexity and length.

Features:

* Password strength check based on various criteria (length, character complexity).

* Standard salting and hashing techniques for secure password storage.

* Brute-force attack simulation to estimate cracking time based on password complexity.

* Modular design for easy integration into larger security projects.

Install:

1. Clone repository:

         git clone https://github.com/kpuentec/PasswordValidator.git

4. Navigate to the project directory: cd PasswordValidator

5. Install requirements:

         pip install -r requirements.txt

Run:

* python main.py for menu options

* Navigate to the backend/ folder

* python pass_strength.py <password> to check your passwords strength

* python pass_salt_hash.py <password> to have your password salted and hashed and stored within a SQL database.

* python brute_force_sim.py <password> to see estiamte of brute force attack being successful on your passwords.

Structure:

*backend/ : Contains Python functions for the program

    *main.py : Main script to tie everything together and run the password validation checks.
    *pass_salt_hash.py : Functions for password salting and hashing.
    *pass_strength.py : Password strength evaluation logic.
    *brute_force_sim.py : Script to simulate a brute-force attack on a password.

*.gitignore : Git ignore file to exclude unnecessary files

*LICENSE : Project license info

*README.md: This file



2025
