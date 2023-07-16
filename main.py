# 3 FEATURES:
# license plate generator
# pin number generator
# valid email password generator

def license_plate_generator():
    pass

def pin_number_generator():
    import string
    import random
    all_digits = string.digits
    pin = []
    for _ in range(5):
        pin.append(random.choice(all_digits))
    return "".join(pin)

def valid_email_generator():
    import string
    import random
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
