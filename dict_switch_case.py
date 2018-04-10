# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:20:31 2018

@author: Sam-Sam
"""

def dispatch_if(operator, x,y):
    if operator=='add':
        return x+y
    elif operator =='sub':
        return x-y
    elif operator =='mul':
        return x*y
    elif operator=='div':
        return x/y
    else:
        return None
        
print(dispatch_if('div', 6,3))
print(dispatch_if('mul', 6,3))
print(dispatch_if('sub', 6,3))
print(dispatch_if('add', 6,3))

def dispatch_dict(operator, x,y):
    """
    Without last paranthesis it will return lamda function.
    We have to call this function to get the result.
    """
    return {
            'add': lambda:x+y,
            'sub': lambda:x-y,
            'mul': lambda:x*y,
            'div': lambda:x/y,}.get(operator, lambda:None)()
            
print(dispatch_dict('div', 6,3))
print(dispatch_dict('mul', 6,3))
print(dispatch_dict('sub', 6,3))
print(dispatch_dict('add', 6,3))