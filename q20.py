#Write a python program that takes a list of numbers and returns their sum.
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers=[5,7.9,26,78,87]
print(sum_numbers(numbers))

