# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

password=input("Enter new password: ")
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