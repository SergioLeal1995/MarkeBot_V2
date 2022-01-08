# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 22:21:58 2021

This code is in charge of scrapt the information of the browser and extract the
main information, name, adress and phone of the market that we want

inputs:
    browser: Browser object to interact with the page
    city: City in which we want to do the seach
    busca: how we search in the browser
    
outputs:
    elements: list of lists with the information of the markets

@author: Sergio Leal
"""

from bs4 import BeautifulSoup
from time import sleep

import random

def searcher(browser,city,busca):
    print('Searcher IN')
    elements = []
    less = 3
    more = 5

    # A implicit wait is neccesary meanwhile the page respond
    browser.implicitly_wait(5)
    # Creation of a limit about the quantity of results (20)
    long = len(browser.find_elements_by_class_name('VkpGBb'))
    sleep(random.uniform(less,more))
    # For cicle to extract each info per page
    for j in range(long):
        #lista = []
        try:
            # Here we catch all 20 results per page
            browser.implicitly_wait(5)
            boxe = browser.find_elements_by_class_name('VkpGBb')
            # Here we use click in each element
            try:
                boxe[j].click()
            except IndexError:
                print(boxe[j])
                continue
            # we extrat all html code of the page to extract the information
            sleep(random.uniform(less,more))
            src = browser.page_source
            soup = BeautifulSoup(src, 'lxml')
            # Here we extract the name of the market
            sleep(random.uniform(less,more))
            try1 = soup.find('div',{'class':'SPZz6b'})
            try2 = try1.find('h2')
            market = try2.find('span').get_text()
            # In this part we use a exception and conditional in the extraction
            # process of the adress and telephone of the market
            try:
                info = soup.find_all('div',{'class':'zloOqf PZPZlf'})
                adress = ((info[0].find_all('span'))[-1]).get_text()
                tel = ((info[-1].find_all('span'))[-1]).get_text()
                if adress == tel:
                    tel = ' '
            except IndexError:
                adress = ''
                tel = ''
                
        except TypeError:
            # if a Exception is found in the process code enter here
            print('Place whiout phone number')
            adress = ((info[0].find_all('span'))[-1]).get_text()

        lista = [market,adress,tel,0,0,' ',' ',city,busca]
        print(lista)
        # info = key words used to the search
        #[market,adress,tel,city,GustavoCheck,MessageSended,dateOfFirstContact,AnswerOfTheClient,info]
    
        elements.append(lista)

    print('Searcher OUT')
    return elements