# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 18:26:06 2021

Esta función se encarga de extraer los nombres con los repectivos id's de las
worksheets de google, retorna dos diccionarios y una lista los cuales contienen:
    dic_id : diccionario con llaves los nombres de las hojas y valores  el id de las hojas
    dic_in : diccionario con llaves los nombres de las hojas y valores el indice de cada hoja
    names  : lista con los nombres de las hojas de cálculo
    
Ejemplo de uso: 
    import nameAndIndex
    
    opcion = nameAndIndex.dics('MarkeBot')

@author: Sergio Leal
"""

from oauth2client.service_account import ServiceAccountCredentials
import gspread

def dics(doc):
    scope = ["https://spreadsheets.google.com/feeds",
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]   
    
    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('Keys.json',scope)
    
    # authorize the clientsheet 
    client = gspread.authorize(creds)
    
    # get the instance of the Spreadsheet
    sheet = client.open(doc)
    
    hojas = sheet.worksheets()
    dic_id = {} # Dictionary with id's
    dic_in = {} # Dictionary with indexs
    names = []
    for i in range(len(hojas)):
        dic_id.update({hojas[i].title:hojas[i].id})
        dic_in.update({hojas[i].title:i})
        names.append(hojas[i].title)
        
    print('Seleccione la hoja con la cual desea trabajar \n')
    for key,value in dic_in.items():
        print(f'Hoja de nombre {key:.>{20}} se selecciona con {value}')
        
    sel = input('Por favor ingrese su opción: ')
    opt = int(sel)
    print(f'Ha elegido la opción {sel} que corresponde a la hoja de nombre "{names[opt]}"')
 
    return opt
