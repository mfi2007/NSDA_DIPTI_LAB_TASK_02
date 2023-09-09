# Function to find the maximum number in a list
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Function to find the minimum number in a list
def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# Taking a list from the user (containing your mobile number)
user_numbers = [int(input("Enter your mobile number: "))]

# Find and print the maximum and minimum numbers from the list
max_num = find_max(user_numbers)
min_num = find_min(user_numbers)

print("Maximum number:", max_num)
print("Minimum number:", min_num)
