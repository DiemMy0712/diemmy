# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:51:19 2024

@author: MAI THỊ DIỄM MY
"""
nhap = input("Nhập 1 chữ cái: ")
if len(nhap) == 1:
    if nhap.lower:
        print(nhap.upper())
    elif nhap.upper():
        print(nhap.lower())
    else:
        print("Không nhận diện được")
else:
    print("Không hợp lệ")
