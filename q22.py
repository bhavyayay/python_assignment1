#Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    return min(numbers), max(numbers)


numbers = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = find_min_max(numbers)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")