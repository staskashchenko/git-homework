# 4 FEATURES:
# license plate generator
# pin number generator
# valid email password generator

import random
import string
# user interface


def license_plate_generator():
    license_plate = []
    upper_case_letters = string.ascii_uppercase
    all_digits = string.digits

    for digit in range(3):
        license_plate.append(random.choice(upper_case_letters))

    for letter in range(3):
        license_plate.append(random.choice(all_digits))
    return "".join(license_plate)

def pin_number_generator(length):
    all_digits = string.digits
    pin = []
    for _ in range(length):
        pin.append(random.choice(all_digits))
    return "".join(pin)

def valid_email_generator():
    all_digits = string.digits
    all_lowercase = string.ascii_lowercase
    all_uppercase = string.ascii_uppercase
    special_characters = ['@',"#","$","*","&","!"]
    password = []

    for letter in range(4):
        password.append(random.choice(all_lowercase))

    for digit in range(4):
        password.append(random.choice(all_digits))

    for capital in range(2):
        password.append(random.choice(all_uppercase))

    for special_char in range(2):
        password.append(random.choice(special_characters))
    return "".join(password)



run = True

while run:
    print("CODE GENERATOR 1.0:")
    print()
    print("1. CAR LICENSE PLATE")
    print("2. PIN NUMBER")
    print("3. VALID EMAIL PASSWORD")
    print("4. EXIT")
    print()
    selected_code = input("What type of code would you like to generate (1,2 or 3) :")
    if selected_code == '1':
        print(license_plate_generator())
        print()
    elif selected_code == '2':
        length = input("How many digits would you like in the PIN?: ")
        if (length) in ['4','5','6','7','8','9','10']:
            print(pin_number_generator(int(length)))
        else:
            print(pin_number_generator(4))
        print()
    elif selected_code == '3':
        print(valid_email_generator())
        print()
    elif selected_code == '4':
        run = False
    else:
        print('Invalid input. Please enter a number from 1-4.')
