# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:59:20 2022

@author: jovita amanda putri
"""
def kabisat(tahun):
    if tahun % 4 == 0:
        if tahun % 100 == 0:
            if tahun % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def hari(tahun, bulan):
    if bulan > 12 or bulan < 1:
        return "Bulan tidak valid!"
    if bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    if bulan in (4, 6, 9, 11):
        return 30
    else:
        return 31

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))
days = hari(tahun, bulan)
print("Jumlah hari:",days)