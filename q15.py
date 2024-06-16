#Write a program that reads data from a CSV file and prints it to the console
import csv
readfile=open("/Users/bhavya/Documents/college/python internship/assignment1/cars.csv","r")
reader = csv.reader(readfile)
for row in reader:
    print(row)
