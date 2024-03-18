# -*- coding: utf-8 -*- 

def has_unique_chars(string):
    unique_chars = set() 

    for char in string:
        if char in unique_chars:
            return False 
        unique_chars.add(char)
    return True

print(has_unique_chars("Södra"))
print(has_unique_chars("Södra Skogsägarna"))
print(has_unique_chars("Systemutvecklare"))