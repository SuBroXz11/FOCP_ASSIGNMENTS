#  Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

inputs=input("Enter 'C' for centrigade to farhenheit conversion \n and  \n'F' for farhenheit to centrigade temperature: ")
def test(temp):
    if(inputs=='C'):
        print(f"{temp}°C to farhenheit is {(temp*9/5)+32} °F ")
    elif(inputs=='F'):
        print(f"{temp}°F to centigrade is {(temp-32)*5/9} °C ")
test(100)
        
        