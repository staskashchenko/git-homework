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

def pin_number_generator():
    import string
    import random
    all_digits = string.digits
    pin = []
    for _ in range(4):
        pin.append(random.choice(all_digits))
    return "".join(pin)

def valid_email_generator():
    pass



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
        pin_number_generator()
        print()
    elif selected_code == '3':
        valid_email_generator()
        print()
    elif selected_code == '4':
        run = False
    else:
        print('Invalid input. Please enter a number from 1-4.')