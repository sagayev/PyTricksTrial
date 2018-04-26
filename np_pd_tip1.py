# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
frame=pd.DataFrame(np.random.randn(4,3), columns=list('bde'), index=[
        'Utah', 'Ohio','Texas', 'Oregon'])
f=lambda x: x.max() - x.min()
frame.apply(f, axis=1)
frame.apply(f, axis=0)
#Out[8]: 
#b    0.513681
#d    3.271031
#e    0.469249
#dtype: float64
#
#frame.apply(f, axis=1)
#Out[9]: 
#Utah      1.255902
#Ohio      1.171964
#Texas     0.861112
#Oregon    3.001437
#dtype: float64

format = lambda x: '%.2f' % x
frame.applymap(format)
#frame.apply(format) won't work.
#            b      d      e
#Utah     0.38  -0.85  -1.96
#Ohio    -0.57   0.21   0.24
#Texas   -0.13   0.93   0.49
#Oregon   0.35  -0.94   0.10

frame['e'].map(format)
#Out[17]: 
#Utah      -1.96
#Ohio       0.24
#Texas      0.49
#Oregon     0.10
#Name: e, dtype: object