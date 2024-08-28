# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:09:35 2024

@author:MAI THỊ DIỄM MY
"""
import math
a= int(input("nhập số a"))
b = int(input("nhập số b"))
N= (((a + b)/(a**(1/3)+b**(1/3)) - (a*b)**(1/3))) / ((a**(1/3))-b**(1/3))**2
print("N là", N)