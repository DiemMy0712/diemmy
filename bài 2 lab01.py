# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:09:22 2024

@author: MAI THỊ DIỄM MY
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
if b == 0:
    print("Không thể chia cho 0")
else:
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = round(a / b, 3)
    print("Tổng:", tong)
    print("Hiệu:", hieu)
    print("Tích:", tich)
    print("Thương:", thuong)

