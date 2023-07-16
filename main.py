# 3 FEATURES:
# license plate generator
# pin number generator
# valid email password generator

def license_plate_generator():
    pass

def pin_number_generator(length):
    import string
    import random

    all_digits = string.digits
    pin = []
    for _ in range(length):
        pin.append(random.choice(all_digits))
    return "".join(pin)

def valid_email_generator():
    pass