# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:50:19 2024

@author: MAI THỊ DIỄM MY
"""
gio1= int(input("Nhập giờ: "))
phut1= int(input("Nhập phút: "))
giay1 = int(input("Nhập giây: "))
tong_gio_1= gio1*3600+phut1*60+giay1
gio2=int(input("Nhập giờ: "))
phut2= int(input("Nhập phút: "))
giay2= int(input("Nhập giây: "))
tong_gio_2=gio2*3600+phut2*60+giay2
tong2gio= tong_gio_1+tong_gio_2
hieu2gio=tong_gio_1-tong_gio_2
print("tong 2 giờ",tong2gio)
print("hiệu 2 giờ", hieu2gio)