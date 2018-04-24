# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 09:48:50 2018
Dan Bader's pytricks
@author: Sam-Sam
"""

def add_this(a:int, b:int) -> int:
    return a+b

#this just gives you hint, doesn't prevent following
add_this('samir', ' aghayev')

#we can force it by pylint and mypy-lang
# in my opinion the following is better because you don't need any third party 
#library
def add_this(a:int, b:int) -> int:
    assert isinstance(a,int) and isinstance(b,int), ' parameters must be an integer '
    return a+b