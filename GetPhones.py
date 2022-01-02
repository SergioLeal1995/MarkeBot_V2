# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:57:38 2021

@author: Sergio Leal
"""
"""
 sheet_selectect: Is the sheet in the spreadsheet that you send as parameter
"""
def PhoneNumbers(sheet_selected):
    import gspread
    import pandas as pd
    import numpy as np
    from oauth2client.service_account import ServiceAccountCredentials
    print('************ Extracting phones *******************')
    # define the scope
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]   
    
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('Keys.json',scope)
    
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # get the instance of the Spreadsheet
    sheet = client.open('MarkeBot')
    
    # get the sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(sheet_selected)
    
    # get all the records of the data
    records_data = sheet_instance.get_all_records()
    
    # convert the json to dataframe
    records_df = pd.DataFrame.from_dict(records_data)
    arr = np.array(records_df)
    
    # Extract phone numbers
    conv = arr[:,2]
    
    # Cast array to list
    phones = list(conv)
    return phones