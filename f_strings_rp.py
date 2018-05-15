# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:20:35 2018

@author: Samir_Agayev
"""

name ="Samir"
age = 40
message = f"Hello, {name}. You are {age}."
print(message)

#CAPITAL F is also OK
message=F"Hello, {name}. You are {age}."
print(message)
## EXPRESSION INSIDE F STRINGS

message = F"{2*20}"
print(message)

#You can call functions as well
def to_lowercase(input):
    return input.lower()

name = "Samir Aghayev"
message = f"{to_lowercase(name)} is funny"
print (message)