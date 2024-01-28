# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

password=input("Enter new password: ")
if(len(password)>=8 and len(password)<=12):
    if password:
        new_password=input("Enter the password again: ")
        while (password!=new_password):
            print("The two password doesn't match.. please try again")
            password=input("Enter new password: ")
            if password:
                new_password=input("Enter the password again: ")
        else:
            print('Password Set!')
    else:
        print('please enter an password! Try again..')
else:
    print("The password must be between 8 and 12 characters long!")        