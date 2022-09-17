# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:19:31 2022

@author: 20203226
"""

import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util
from IPython.display import display, clear_output

def t2h(T, t):
    # Convert a 2D transformation matrix to homogeneous form.
    # Input:
    # T - 2D transformation matrix
    # t - 2D translation vector
    # Output:
    # Th - homogeneous transformation matrix
    
    #Th = np.array([np.transpose(np.concatenate((T,t),axis=0))])
    #Th = np.transpose(Th)
    
    Th = np.array([[T[0,0],T[0,1],t[0]],[T[1,0],T[1,1],t[1]],[0,0,1]])
    Th
    return Th

X = util.test_object(1)
Xh = util.c2h(X)

# translation vector
t = np.array([10, 20])

# rotation matrix
T_rot = reg.rotate(np.pi/4)

Th = t2h(T_rot, t)
print(Th)



