#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input
print("Temperature Conversion")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")

else:
    print("Invalid choice. Please enter 1 or 2.")
