# 3 FEATURES:
# license plate generator
# pin number generator
# valid email password generator
import random
import string

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
    pass

def valid_email_generator():
    pass