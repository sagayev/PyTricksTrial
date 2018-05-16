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


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
    
new_comedian = Comedian("Samir", "Aghayev", "40")

message=f"{new_comedian}"  #default way of referring to __str__ method
print(message)
#>>>Samir Aghayev is 40

message=f"{new_comedian!r}"  #How to refer to __repr__ method
print(message)
#>>>Samir Aghayev is 40. Surprise!


"""
Multiline f-strings

"""
name = "Samir"
profession = "comedian"
affiliation = "Monty Python"
message = (
        f"Hi {name}. "
        f"You are a {profession}. "
        f"You were in {affiliation}."
        )
print(message)
#Hi Samir. You are a comedian. You were in Monty Python.


message =f"""
    Hi {name}.
    You are a {profession}.
    You were in {affiliation}.
    
    """
print (message)
#    Hi Samir.
#    You are a comedian.
#    You were in Monty Python.

#>>>message
#'\n    Hi Samir.\n    You are a comedian.\n    You were in Monty Python.\n    \n


comedian = {'name': 'Samir Aghayev', 'age': 40}
message=f"The comedian is {comedian['name']}, aged {comedian['age']}."
print("Dictionary in f string: ", message)


print(f"{{40}}")        #>>{40}
print(f"{{{40}}}")      #>>{40}
print(f"{{{{40}}}}")    #>>{{40}}





















