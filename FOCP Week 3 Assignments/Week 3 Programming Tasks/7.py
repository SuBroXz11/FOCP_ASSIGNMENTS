# Modify your "Times Table" program so that the user enters the number of the table
# they require. This number should be between 0 and 12 inclusive.
num=int(input("Enter a number between 0 and 12: "))
for i in range(0,13):
    print(f"{i} x {num} = ", i*num)