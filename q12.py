# Write a python program that calculates the sum of the digits of a given number.
num=int(input("enter the number to be calculated"))
sum=0
for i in str(num):
    sum+=int(i)
print(sum)
