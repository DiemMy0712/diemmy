# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:42:07 2024

@author: MAI THỊ DIỄM MY
"""
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
max_value = a
if max_value < b:
    max_value = b
if a < c:
    max_value = c
print(' SỐ LỚN NHẤT LÀ', max_value)
