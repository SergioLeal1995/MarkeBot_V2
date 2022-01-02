# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:55:10 2021

@author: seran
"""
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import login_mb
import searcher_mb_V2
import cloud_mb

# Sheet name 
name_sheet = input('Ingrese el nombre de la hoja de cálculo para esta busqueda: ')
info = input('Ingrese que desea buscar: ')
where = input('Ingrese donde lo desea buscar: ')

# Get in to the web browser
browser, city = login_mb.login(info,where)

# Creating a new sheet
cloud_mb.spreadSheet('',name_sheet,True)

# In this cicle we determine the times that the search do
for i in range(25):
    
    # Function in charge to do login and put the search in the browser
    arr = searcher_mb_V2.searcher(browser,city)
    
    # Verifying nonrepeat registers
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    
    # Function in charge to send information to the cloud
    cloud_mb.spreadSheet(result,name_sheet,False)
    
    # CLick on next botton geting the exception when the botton doesn't appear
    sleep(5)
    try:
        browser.find_element_by_id('pnnext').click()
    except ElementClickInterceptedException:
        print('La ejecución ha finalizado sin novedades')
        