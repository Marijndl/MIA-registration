# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 19:27:03 2022

@author: 20203226
"""

def question1(a):
    if a <23:
        answer = 23-a
    else:
        answer = 2 * abs(23-a)
    return answer

print(question1(23),"\n")

import numpy as np
def question2(a):
    all_numbers = range(a,a+17,2)
    print(all_numbers)
    array = np.ones((3,3), dtype=int)
    counter = 0
    print(counter)
    for i in range(len(array)):
        for j in range(len(array[0,:])):
            array[i,j] = all_numbers[counter]
            counter+=1
    return array

A = question2(4)

def question3(array):
    middle = len(array[0,:]) // 2
    array[:,middle] = 0
    return array

print(question3(A))      



from scipy import misc
import scipy.ndimage
import matplotlib.pyplot as plt
face = misc.face(gray=True)

raccoon_blured = scipy.ndimage.gaussian_filter(face, sigma=5)
raccoon_diff = face - raccoon_blured
fig, ax = plt.subplots(1, 2)
ax[0].imshow(raccoon_blured, cmap='gray')
ax[1].imshow(raccoon_diff, cmap='gray')
plt.show()