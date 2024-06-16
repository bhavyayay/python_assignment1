# Write a python program that checks if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    """
    Returns True if str1 and str2 are anagrams of each other, False otherwise.
    """
    return sorted(str1) == sorted(str2)
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  

str1 = "hello"
str2 = "world"
print(are_anagrams(str1, str2)) 