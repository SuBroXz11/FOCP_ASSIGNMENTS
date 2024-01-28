BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
i = 1
while (i==1):
    password = input("Enter a password: ")
    if password in BAD_PASSWORDS:
        i = 1
    else:
        if 8 <= len(password) <= 12:
            new_password = input("Enter the password again: ")
            if password == new_password:
                print("Password set")
                i = 2  
            else:
                print("The password and the new password doesn't match!")  
        else:
            print('The password must be between 8 and 12 characters long!')    
        
         