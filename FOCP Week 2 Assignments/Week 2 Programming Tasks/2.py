# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

celsius_temp=float(input("Enter the temperature in Celsius Scale: "))
fahrenheit_temp=((celsius_temp * 9 / 5) + 32)
print(f"{celsius_temp}C is equivalent to {fahrenheit_temp}F")