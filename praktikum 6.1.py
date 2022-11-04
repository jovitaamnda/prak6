# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:31:18 2022

@author: jovita amanda putri
"""

ulang = 0
nilairata = 0.0
a = "wdwd"
def nilai(a):
      p = 0.0
      if a == "A":
        p = 4.00
      elif a == "A-":
        p = 3.75
      elif a == "B+":
        p = 3.50
      elif a == "B":
        p = 3.00
      elif a == "B-":
        p = 2.75
      elif a == "C+":
        p = 2.50
      elif a == "C":
        p = 2.00
      elif a == "C-":
        p = 1.75
      elif a == "D":
        p = 1.50
      elif a == "E":
        p = 1.25
      return p
while a != "":
 a = input("nilai: ")
 if a != "" :
  print("Nilai: {0}".format(nilai(a)))
  ulang = ulang + 1
  nilairata = nilairata + nilai(a)
 if a == "" :
  nilairata = nilairata / ulang 
  print("Rata ratanya adalah: %i"%nilairata)