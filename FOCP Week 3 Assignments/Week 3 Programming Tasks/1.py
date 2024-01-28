# Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.

name=input("Enter you name: ")
if name:
    print(f"Hello {name.title()}, Good to see you.")
else:
    print('Hello Stranger!')