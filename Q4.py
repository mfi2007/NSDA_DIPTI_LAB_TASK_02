# Function to separate even and odd numbers in a list
def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

# 4. Taking a list from the user and finding even and odd numbers
user_numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
even, odd = separate_even_odd(user_numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)