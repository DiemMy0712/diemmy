# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:17:29 2024

@author: MAI THỊ DIỄM MY
"""
N = int(input("Nhập số nguyên dương N có 2 chữ số: "))
chu_so_hang_don_vi = N % 10
chu_so_hang_chuc = N // 10
tong = chu_so_hang_don_vi + chu_so_hang_chuc
print("tong la", tong)
