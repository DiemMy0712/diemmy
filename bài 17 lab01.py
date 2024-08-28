# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:30:37 2024

@author: MAI THỊ DIỄM MY
"""
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
max = a
if b > max : 
    max = b
if c > max :
    max = c
print("giá trị lớn nhất là :", max)
min = a
if b<min:
    min = b
if c< min:
    min = c
print("giá trị nhỏ nhất là :", min)
    