# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:47:32 2021

This function is in charge of create the new sheet in the document and send
the information to the cloud (google spreadsheet)

inputs: 
    lista: Is the list of information that the function searcher give us and this
           list is sended to the cloud
    name_sheet: Is the name of the new google sheet
    flag: is the validator if we want to create a new sheet or send the information
    
outputs:
    copy: Is the sheet objet, is necesary to giving format to the new sheet

@author: Sergio Leal
"""

from oauth2client.service_account import ServiceAccountCredentials

import gspread
import pandas as pd

def spreadSheet(lista,name_sheet,flag):
    copy = ''
    print('******************* Cloud IN **************************')
    
    # define the scope
    scope = ["https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]   
    
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('Keys.json',scope)
    
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # get the instance of the Spreadsheet
    sheet = client.open('MarkeBot')
    
    if flag==True:
        # Creating new sheet
        sheet.add_worksheet(rows=1000,cols=10,title=name_sheet)
    else:
        # get the quantity of sheets
        quantity = len(sheet.worksheets())
        
        # get the instance of the sheet to record the information
        sheet_runs = sheet.get_worksheet(quantity-1)

        # convert the json to dataframe
        records_df = pd.DataFrame.from_dict(lista)
        
        sheet_runs.insert_rows(records_df.values.tolist())
        copy = sheet_runs
        print('Sending information')
    return copy    
    print('********************* Cloud OUT ****************************')  
