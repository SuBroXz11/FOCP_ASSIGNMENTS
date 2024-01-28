# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

password = input("Enter new password: ")
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

for i in BAD_PASSWORDS:
    if i == password:
        print('The password cannot be this..')
        break
else:
    if 8 <= len(password) <= 12:
        new_password = input("Enter the password again: ")

        while password != new_password:
            print("The two passwords don't match. Please try again.")
            password = input("Enter new password: ")

            if 8 <= len(password) <= 12:
                new_password = input("Enter the password again: ")
            else:
                print("The password must be between 8 and 12 characters long!")

        else:
            print('Password Set!')

    else:
        print('Please enter a password between 8 and 12 characters long! Try again.')

