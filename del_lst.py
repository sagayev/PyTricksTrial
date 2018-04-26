# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

lst=[1,2,3,4,5,]

del lst

#lst is gone completely

lst=[1,2,3,4,5,]

del lst[:]

#lst is now empy list like []

a = lst
lst[:] = [7, 8, 9]
lst
#[7, 8, 9]
a
#[7, 8, 9]
