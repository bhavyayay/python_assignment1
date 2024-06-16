#Write a program that takes a string input from the user and writes it to a text file.
str=input("Enter the desired string")
txtfile=open("/Users/bhavya/Documents/college/python internship/assignment1/demofile.txt","w")
print(str,file=txtfile)

