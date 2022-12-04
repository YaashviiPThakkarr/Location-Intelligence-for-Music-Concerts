#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 01:12:53 2021

@author: Yashvi
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
html = urlopen('https://www.numbeo.com/crime/country_result.jsp?country=United+States')
soup = BeautifulSoup(html.read(),'lxml')
#fout = open('/Users/Yashvi/Desktop/CMU - Spring\'21/DFP/temp2.txt','wt',encoding='utf-8')
#fout.write(str(soup))
#fout.close()


#print(str(bsyc.table))

table = soup.find("table", attrs={"id":"t2"})

table_head = table.thead.find_all("tr")
table_data = table.tbody.find_all("tr")

headings = list()
for h in table_head[0].find_all("th"):
    headings.append(h.text)

data = list()


for i in range(0,len(table_data)):
    row = list()
    row.append(i+1)
    for td in table_data[i].find_all("td"):
        if(td.text == ''):
            continue
        else:
            row.append(td.text)
    data.append(row)
    
df = pd.DataFrame(data,columns=headings)
file = 'CrimeRatings.xlsx'
df.to_excel(file) 
