# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format

# temp=int(input(f"Enter any temp : "))
# temp2=str(temp[:-1])
# temp3=int(temp2)
# print(f"{temp3}°C to farhenheit is {(temp3*9/5)+32} °F ")

# Get input from the user
# input_str = input("Enter temperature in the format 'X°C': ")

# # Extract the numerical part of the input (excluding the last character 'C')
# temp_celsius = float(input_str[:-1])

# # Convert Celsius to Fahrenheit
# temp_fahrenheit = (temp_celsius * 9/5) + 32

# # Display the result
# print(f"{temp_celsius}°C to Fahrenheit is {temp_fahrenheit}°F")

####################################################################
####################################################################

def celcius_to_farhenheit(celsius):
    farhenheit=(1.8*celsius)+32
    return farhenheit

def farhenheit_to_celcius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius

temp=input("Enter the tempvalue: ")

def temp_conversion():
    if temp[-1].lower()=="c":
        out=celcius_to_farhenheit(float(temp[:-1]))
    elif temp[-1].lower()=="f":
        out=farhenheit_to_celcius(float(temp[:-1]))
    else:
        out="Invalid Input!"
    return out
print(temp_conversion())
