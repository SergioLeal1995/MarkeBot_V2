# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:47:32 2021

@author: seran
"""

from oauth2client.service_account import ServiceAccountCredentials

import gspread
import pandas as pd

def spreadSheet(lista,name_sheet,flag):

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
    sheet = client.open('Empresas')
    
    if flag==True:
        # Creating new sheet
        sheet.add_worksheet(rows=1000,cols=9,title=name_sheet)
    else:
        # get the quantity of sheets
        quantity = len(sheet.worksheets())
        
        # get the instance of the sheet to record the information
        sheet_runs = sheet.get_worksheet(quantity-1)

        # convert the json to dataframe
        records_df = pd.DataFrame.from_dict(lista)
        
        sheet_runs.insert_rows(records_df.values.tolist())
        print('Sending information')
        
    print('********************* Cloud OUT ****************************')  
