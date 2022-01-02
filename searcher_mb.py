# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:35:15 2021

Esta función extrae las 20 coincidencias de cada página

@author: Sergio Leal
"""
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import re
import solSoup

def searcher(browser,city):
    elements = []
    
    time.sleep(2)
    # Scrool down 4 times
    for i in range(4):
        browser.find_element_by_css_selector('#pane > div > div.Yr7JMd-pane-content.cYB2Ge-oHo7ed > div > div > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ').send_keys(Keys.END)
        time.sleep(0.5)
    
    # Get all the elements with the class name and calculate the longitude of the elements
    each = browser.find_elements_by_class_name('a4gq8e-aVTXAb-haAclf-jRmmHf-hSRGPd')
    long = len(each)
    
    # for cycle depending on the numbers of elements of long variable
    for j in range(long):
        
        # Scroll down 4 times
        for i in range(4):
            browser.find_element_by_css_selector('#pane > div > div.Yr7JMd-pane-content.cYB2Ge-oHo7ed > div > div > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ > div.siAUzd-neVct.section-scrollbox.cYB2Ge-oHo7ed.cYB2Ge-ti6hGc.siAUzd-neVct-Q3DXx-BvBYQ').send_keys(Keys.END)
            time.sleep(0.5)
        
        
        each[j].click() # click on the coincidence number j
        time.sleep(2)
        #Charge html page source to extract the elements
        src = browser.page_source
        soup = BeautifulSoup(src, 'lxml')
        time.sleep(5)
        
        # Name extraction
        h1 = soup.find('h1',{'class':'x3AX1-LfntMc-header-title-title gm2-headline-5'})
        browser.implicitly_wait(5)
        nombre = h1.find('span').get_text()
        nombre,soup = solSoup.zOup(browser)
        
        # Adress and phone extraction
        data = soup.find_all('div',{'class':'QSFF4-text gm2-body-2'})
        
        # Adress
        adress = data[0].get_text()
        
        # Phone
        for k in range(len(data)):
            phone = data[k].get_text()
            try:
                mt = int(re.search('([0-9])',phone)[1])
            except TypeError:
                print('Se levanto una excepción')
                
            if mt>5:
                tel = data[k].get_text()
        elements.append[nombre, adress,tel,city]
        
        # Return to the 20 result of the first page in the search
        browser.find_element_by_class_name('nhb85d-zuz9Sc-haAclf').click()
        
    return elements