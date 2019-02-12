# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:21:25 2019

@author: thanusha
"""

# Numpy 1 assignment
#alexandre theophile vandermode matrix
# boolean expression increasing is false

import numpy as np     # importing numpy library  
N=3                    #number of columns required in output
x = np.array([1,2,3,5]) # creating array of 1 dimensional
np.column_stack([x**(N-1-i) for i in range(N)]) #using column stack to display the output in column
                                                #using list comprehension method 
                                                