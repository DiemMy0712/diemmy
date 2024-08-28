# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:45:59 2024

@author: MAI THỊ DIỄM MY
"""
a = float(input(" nhập số a: "))
b = float(input(" nhập số b: "))
if a == 0 and b == 0:
    print(" pt có vô số nghiệm")
elif a == 0 and b != 0:
    print(" phương trình vô nghiệm")
else:
    print(" phương trình có 1 nghiệm x=", -b/a)
