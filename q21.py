#Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, elem):
    return lst.count(elem)

# Test the function
my_list = [1, 2, 3, 2, 4, 2, 5]
element = 2
print(count_occurrences(my_list, element))  # Should print 3