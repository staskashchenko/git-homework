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
        if int(length) in [4,5,6,7,8,9,10]:
            pin_number_generator(int(length))
        else:
            pin_number_generator(4)
        print()
    elif selected_code == '3':
        valid_email_generator()
        print()
    elif selected_code == '4':
        run = False
    else:
        print('Invalid input. Please enter a number from 1-4.')