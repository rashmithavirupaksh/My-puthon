def sum_of_n_numbers():
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return sum(numbers)
print("Sum of numbers:", sum_of_n_numbers())
