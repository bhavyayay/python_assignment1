#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
string = input("Enter a string: ")
prefix = input("Enter a prefix: ")
suffix = input("Enter a suffix: ")

if string.startswith(prefix):
    print(f"The string starts with the prefix '{prefix}'")
else:
    print(f"The string does not start with the prefix '{prefix}'")

if string.endswith(suffix):
    print(f"The string ends with the suffix '{suffix}'")
else:
    print(f"The string does not end with the suffix '{suffix}'")