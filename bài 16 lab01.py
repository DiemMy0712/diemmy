# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:27:34 2024

@author: MAI THỊ DIỄM MY
"""
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
tong_so_giay = gio * 3600 + phut * 60 + giay
print("tổng số giây là", tong_so_giay)