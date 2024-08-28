# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:28:17 2024

@author: MAI THỊ DIỄM MY
"""
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
bmi = can_nang / (chieu_cao ** 2)
print("bmi là", bmi)
