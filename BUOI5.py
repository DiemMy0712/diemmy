# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:29:14 2024

@author: MAI THI DIEM MY
BÀI 1: TRUNG BÌNH CỘNG
a = int(input("nhap a:"))
b = int(input("nhap b:"))
c = int(input("nhap c:"))
d = int(input( " nhap d:"))
trung_binh = ( a + b + c + d)/4
print("tong trung a,b,c,d la ", trung_binh)
BÀI 2: 2 SỐ NGUYÊN a, b
a= int(input("nhap a"))
b= int(input("nhap b"))
tong=(a+b)
hieu=(a - b)
tich=( a*b)
thuong= round((a/b), 2)
chia_lay_phan_du = ( a % b)
chia_lay_phan_nguyen = (a //b)
print(" a + b=", tong)
print(" a - b=", hieu)
print(" a * b=", tich)
print(" a / b=", thuong)
print(" a / b=", round(a / b, 2))
print(" a % b=", chia_lay_phan_du)
print(" a // b =", chia_lay_phan_nguyen)
BÀI 3: TỔNG CÁC CHỮ SỐ CỦA n
n = int(input("nhap so nguyen duong co 2 chu so"))
chu_so_hang_chuc = n//10
chu_so_hang_don_vi = n%10
tong_cac_chu_so_cua_n= chu_so_hang_chuc + chu_so_hang_don_vi
if 10 <= n <= 100:
   print("tong cac chu so cua n", tong_cac_chu_so_cua_n)
BÀI 4: TỔNG GIỜ
gio = int(input("nhap gio"))
phut = int(input("nhap phut"))
giay = int(input("nhap giay"))
tong_giay = gio *3600 + phut *60 + giay
print(" tong so giay la", tong_giay)
BÀI 5: SỐ TUỔI
nam_sinh = int(input("nhap nam sinh"))
nam_hien_tai = 2024
so_tuoi = nam_hien_tai - nam_sinh
print("so tuoi la", so_tuoi)
BÀI 6: TÍNH PHƯƠNG TRÌNH a, b, c
a = int(input("nhap a"))
b = int(input(" nhap b"))
c = int(input("nhap c"))
print(f" {a}X^2 + {b}x + {c} = 0")
BÀI 7: MENU
print("============ MENU ============ ")
print("1. Hu tieu")
print("2.Chao long")
print("3. Bun bo")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================  ")
input(" Moi nhap lua chon: ")
print("============================== ")
print( " su lua chon cua ban la: ")
BÀI 8: CÀI ĐẶT PHÉP TÍNH BIỂU THỨC A
A = (32 ** 0.2) - ((1/64) ** -0.25) + (( 8/27) ** (1/3))
print(" Ket qua cua A =",round(A, 3))
BÀI 9: NHẬP GIÁ TRỊ CHO 2 SỐ THỰC
import math 
a= float(input("nhap a ="))
b= float(input("nhap b="))
A= (math.sqrt(a) - math.sqrt(b)) / ((a** (1/4)) - (b ** (1/4)))
B= (math.sqrt(a) + ((a* b) **(1/4))) / ((a ** (1/4)) +( b ** (1/4)))
print( " Ket qua cua phep tinh la: ", A - B)
"""

