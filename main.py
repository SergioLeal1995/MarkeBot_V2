# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:55:10 2021

@author: Sergio Leal
"""
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import login_mb
import searcher_mb_V2
import cloud_mb


# Sheet name 
print("""Como usuario puede hacer la búsqueda a su gusto, sin embargo le
      recomendamos hacer uso de operadores avanzados para hacer una busqueda
      mucho más precisa y obtener mejor filtrado de resultados, los operadores
      avanzados más comunes son los siguientes.
      
      () : Hace que la búsqueda de aquellos que esté dentro de los parentesis
           sea mucho más estricta.
      - : Si por algún motivo hay algo que desee excluir de su búsqueda este
          operador es útil para dicho uso.
      AND : Este operador lógico le permite hacer una búsqueda donde si o si
            las palabras relacionadas al mismo serán certeras, también puede usar
            el símbolo '&'.
      OR : Da la opción de que si o no aparezca las palabras relacionadas al
           mismo, también puede usar el símbolo '|'.
      Ejemplo: (fabricas AND (Hielo OR Plastico) AND Cundinamarca)-Bogotá""")
      

      
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
    arr = searcher_mb_V2.searcher(browser,city,info)
    
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
    except NoSuchElementException:
        print('La ejecución ha finalizado sin novedades')
        break

# Retornar sheet_runs se reemplaza en worksheet

# worksheet.format("A2:B2", {
#     "backgroundColor": {
#       "red": 0.0,
#       "green": 120,
#       "blue": 50
#     },
#     "horizontalAlignment": "CENTER",
#     "textFormat": {
#       "foregroundColor": {
#         "red": 1.0,
#         "green": 1.0,
#         "blue": 1.0
#       },
#       "fontSize": 10,
#       "bold": True
#     }
# })