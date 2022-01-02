# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:21:58 2021

@author: Sergio Leal
"""

from bs4 import BeautifulSoup
from time import sleep

import random

def searcher(browser,city):
    print('Searcher IN')
    elements = []
    less = 2
    more = 5


    browser.implicitly_wait(5)
    long = len(browser.find_elements_by_class_name('VkpGBb'))
    sleep(random.uniform(less,more))
    
    for j in range(long):
        #lista = []
        try:
                
            boxe = browser.find_elements_by_class_name('VkpGBb')
            boxe[j].click()
            
            sleep(random.uniform(less,more))
            src = browser.page_source
            soup = BeautifulSoup(src, 'lxml')
    
            sleep(random.uniform(less,more))
            try:
                
                try1 = soup.find('div',{'class':'SPZz6b'})
                try2 = try1.find('h2')
                market = try2.find('span').get_text()
            except AttributeError:
                
                print('AttributeError In')
                try1 = soup.find('div',{'class':'SPZz6b'})
                try2 = try1.find('h2')
                market = try2.find('span').get_text()
                

    
            info = soup.find_all('div',{'class':'zloOqf PZPZlf'})
            adress = ((info[0].find_all('span'))[-1]).get_text()
            tel = ((info[-1].find_all('span'))[-1]).get_text()
            if adress == tel:
                tel = ' '
    
        except TypeError:
    
            print('Place whiout phone number')
            adress = ((info[0].find_all('span'))[-1]).get_text()

        lista = [market,adress,tel,city]
    
    
        elements.append(lista)

    print('Searcher OUT')
    return elements