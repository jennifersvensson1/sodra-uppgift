# -*- coding: utf-8 -*- # Ensures proper handling of non-ASCII characters

def has_unique_chars(string):
    unique_chars = set() # Collection with only unique values

    # Iterates through each character in the string and checks for duplicates
    for char in string:
        if char in unique_chars:
            return False 
        unique_chars.add(char)
    return True

# Example usage of the function with strings containing unique and duplicate characters
print(has_unique_chars("Södra"))
print(has_unique_chars("Södra Skogsägarna"))
print(has_unique_chars("Systemutvecklare"))