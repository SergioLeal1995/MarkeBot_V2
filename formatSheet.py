# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:36:29 2022

@author: Sergio Leal
"""

def formating(sheet):
    sheet.format("A1:I1", {
        
        "backgroundColor": {
          "red": 0.0,
          "green": 120,
          "blue": 50
        },
        "horizontalAlignment": "CENTER",
        "textFormat": {
          "foregroundColor": {
            "red": 1.0,
            "green": 1.0,
            "blue": 1.0
          },
          "fontSize": 10,
          "bold": True
        }
    })