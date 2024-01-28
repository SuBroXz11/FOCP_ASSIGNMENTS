def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If a factor is found, the number is not prime
    
    return True  # If no factors are found, the number is prime

# Test the function
number = 17
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
