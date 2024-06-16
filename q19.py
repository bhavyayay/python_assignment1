#Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
  
    punctuations = string.punctuation
    
   
    cleaned_string = ""
    
   
    for char in input_string:
       
        if char not in punctuations:
           
            cleaned_string += char
    
    return cleaned_string

input_string = input("Enter a string with punctuation: ")
cleaned_string = remove_punctuation(input_string)
print("String without punctuation:")
print(cleaned_string)
