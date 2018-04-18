# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:56:59 2018
Replicating Dan Bader's python tricks
@author: Sam-Sam

vals = [expression
        for value in collection
        if condition]

#This equivalent to:
    
vals=[]
for value in  collection:
    if condition:
        vals.append(expression)
"""       
#Example
even_squares =[x * x for x in range(10) if not x%2]
               
even_sq_long=[]
for x in range(10):
    if not x%2:
        even_sq_long.append(x * x)
        
print(even_squares==even_sq_long)