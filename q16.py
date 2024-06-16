#Write a program in python that counts the frequency of each character in a string
string = input("Enter a string: ")
for i in set(string):
    frequency = string.count(i)
    print(str(i),":",str(frequency))