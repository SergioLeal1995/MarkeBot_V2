# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:31:53 2021

Este código se encarga de acceder al navegador dirigirse hasta 
google maps y luego escribir lo que deseamos buscar.

@author: seran
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time

def login(info,where):
    
    # Creating the object to open de browser
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Getting the URL and open de browser
    #browser.get('https://www.google.com/maps/@15,-2.970703,3z?hl=es')
    browser.get("""https://www.google.com/search?sxsrf=AOaemvJFlZpUo_x9-cto6m55dikbhPjYEg:
                1640914337240&q=0&rflfq=1&rldoc=1&rllag=4756802,-74199411,6658&tbm=lcl&sa=
                X&ved=2ahUKEwif-rWh8oz1AhWeSTABHZqmCCYQtgN6BAgCEFM&biw=1920&bih=1011&dpr=
                1&fll=0,0&fspn=0.33010749999999955,0.20458689999999535&fz=0&sll=0,0&sspn=
                0.33010749999999955,0.20458689999999535&sz=0&tbs=lrf:!1m4!1u3!2m2!3m1!1e1
                !1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rlst=f#rlfi=hd:;si
                :;mv:[];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3
                sIAE,lf:1,lf_ui:2""")
    # Upper case the city where we want to search
    cp_wh = where.upper()
    # Searching the input box to write the search
    Buscar = browser.find_element_by_id('lst-ib')
    Buscar.send_keys(Keys.BACKSPACE)
    # Concatenating all the message in the browser
    Buscar.send_keys(info + ' en ' + where + ' colombia')
    time.sleep(1)
    # Click on the sarch botton
    browser.find_element_by_id('mKlEF').click()
    
    return browser,cp_wh