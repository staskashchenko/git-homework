# 4 FEATURES:
# license plate generator
# pin number generator
# valid email password generator
# user interface

def license_plate_generator():
    pass

def pin_number_generator():
    pass

def valid_email_generator():
    pass

print("CODE GENERATOR 1.0:")
print()
print("1. CAR LICENSE PLATE")
print("2. PIN NUMBER")
print("3. VALID EMAIL PASSWORD")
print("4. EXIT")
print()

run = True

while run:
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