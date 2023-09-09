# Function to sort a list in ascending order
def sort_list_ascending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

# 3. Taking a list from the user and sorting it in ascending order
user_numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
sorted_numbers = sort_list_ascending(user_numbers)
print("Sorted list in ascending order:", sorted_numbers)