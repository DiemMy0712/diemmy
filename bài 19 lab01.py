# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:30:57 2024

@author: Acer
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
min_value = a
if b < a:
    min_value = b
if c < a:
    min_value = c
if d < a:
    min_value = d
print("số nhỏ nhất là", min_value)
