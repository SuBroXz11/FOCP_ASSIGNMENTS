def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Example usage:
number = 12
result = find_factors(number)
print(f"The factors of {number} are: {result}")
