#  Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.

def check(string):
    upper=0
    lower=0
    
    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
            
    print(f"upper character is {upper} " )
    print(f"lower character is {lower} " )

check("subraT")

            

        
