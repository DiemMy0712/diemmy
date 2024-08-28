# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:20:04 2024

@author: MAI THỊ DIỄM MY
"""
thoi_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")
gio, phut, giay = map(int, thoi_gian.split(":"))
tong_giay = gio * 3600 + phut * 60 + giay
print("tong giay la", tong_giay)
