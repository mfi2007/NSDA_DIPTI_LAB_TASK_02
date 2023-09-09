# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True



# 5. Taking a number from the user and checking if it's prime
user_number = int(input("Enter a number: "))
if is_prime(user_number):
    print(user_number, "is a prime number.")
else:
    print(user_number, "is not a prime number.")
