#!/usr/bin/python3
'''
PROJECT: STRONG PASSWORD GENERATOR
AUTHOR: TITO OSADEBEY
EMAIL: osadebe.tito@gmail.com
'''

import random

def password_generator():
    password_characters = 'TIUOYASENDBtiuoyasendb0123456789#$π~©®%^[]|&()?!:;-*_@/'
    number_of_passwords = int(input("Enter the amount of passwords to generate: "))
    password_length = int(input("Enter password length: "))
    
    print("\nPasswords:")
    
    for pwd in range(number_of_passwords):
        passwords = ' '
        
        for character in range(password_length):
            passwords += random.choice(password_characters)
        print(passwords)
    
password_generator()
