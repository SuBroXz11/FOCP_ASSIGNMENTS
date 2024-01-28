# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean
# Function to calculate the mean of a list of numbers
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Read temperatures from the user
# temperatures = []
# for i in range(1, 7):
#     temperature = float(input(f"Enter temperature {i}: "))
#     temperatures.append(temperature)

# # Calculate and display the maximum, minimum, and mean temperatures
# maximum_temperature = max(temperatures)
# minimum_temperature = min(temperatures)
# mean_temperature = calculate_mean(temperatures)

# print(f"\nMaximum Temperature: {maximum_temperature}")
# print(f"Minimum Temperature: {minimum_temperature}")
# print(f"Mean Temperature: {mean_temperature}")
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

temperatures = []


for i in range(1, 7):
    temperature_str = input(f"Enter temperature {i}: ")

    if temperature_str.replace(".", "", 1).isdigit():
        temperature = float(temperature_str)
        temperatures.append(temperature)
    else:
        print("Invalid input. Please enter a valid numeric temperature.")
        i -= 1


maximum_temperature = max(temperatures)
minimum_temperature = min(temperatures)
mean_temperature = calculate_mean(temperatures)

print(f"\nMaximum Temperature: {maximum_temperature}")
print(f"Minimum Temperature: {minimum_temperature}")
print(f"Mean Temperature: {mean_temperature}")

