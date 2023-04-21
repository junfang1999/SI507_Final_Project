# Data: 中国人大网-代表信息-第十三届全国人大代表

from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote 
from urllib.request import urlopen
import urllib
import csv
import time

path = "/Users/junfang/Dropbox\ \(University\ of\ Michigan\)/Research\ Projects/Project_Toilet/Data/People\'s\ Congress/SI_507_junfang_data_access.py"

driver = "/Users/junfang/Dropbox\ \(University\ of\ Michigan\)/Research\ Projects/Project_Toilet/Data/People\'s\ Congress/chromedriver"

urlhead = "https://zh.m.wikipedia.org"

with open(path+'npc13.csv','w+',encoding='utf-8', newline='') as file:
    writer =csv.writer(file)
    writer.writerow(["id", "name", "party", "gender", "ethnic", "birthday", "position", "note", "birthplace", "repprov"])      

id = ""
name = ""
party = ""
gender = ""
ethnic = ""
birthday = ""
position = ""
note = ""
birthplace = ""
repprov = ""

url = urlhead+"/zh-sg/"+quote("第十三届全国人民代表大会代表名单")
req = urllib.request.urlopen(url)
soup = BeautifulSoup(req.read())
maincontent = soup.find_all('div', attrs = {'class':'mw-parser-output'})

tables = maincontent[0].find_all('table')
para = maincontent[0].find_all('p')

#--------------------------------------------------------
# 北京
tablerows = tables[2].find_all('tr')
tablerows_len = len(tablerows)
for i in range(6,tablerows_len):
    tablecells = tablerows[i].find_all('td')
    output = []
    tablecells_len = len(tablecells)
    for j in range(0, tablecells_len):
        output.append(tablecells[j].get_text().replace("\n",""))
    indurl = urlhead+tablecells[0].find_all('a')[0].get('href')
    indreq = urllib.request.urlopen(indurl)
    indsoup = BeautifulSoup(indreq.read())
    indtable = indsoup.find_all('table', attrs={'class':'infobox biography vcard'})
    if indtable == []:
        indtable = indsoup.find_all('table', attrs={'class':'infobox vcard'})
    if indtable != []:
        indtabrow = indtable[0].find_all('tr')
        indtabrow_len = len(indtabrow)
        for k in range(0, indtabrow_len):
            intabrow_text = indtabrow[k].get_text()
            if '籍贯' in intabrow_text:
                birthplace = intabrow_text.replace("籍贯","")
                break
    else:
        birthplace = ""
    output.append(birthplace)
    output.append("北京市")
    with open(path+'npc13.csv','a',encoding='utf-8', newline='') as file:
        writer =csv.writer(file)
        writer.writerow(output)

#--------------------------------------------------------
# 天津市
tablerows = tables[3].find_all('tr')
tablerows_len = len(tablerows)
for i in range(1,tablerows_len):
    tablecells = tablerows[i].find_all('td')
    output = []
    tablecells_len = len(tablecells)
    for j in range(0, tablecells_len):
        output.append(tablecells[j].get_text().replace("\n",""))
    indurl = urlhead+tablecells[0].find_all('a')[0].get('href')
    indreq = urllib.request.urlopen(indurl)
    indsoup = BeautifulSoup(indreq.read())
    indtable = indsoup.find_all('table', attrs={'class':'infobox biography vcard'})
    if indtable == []:
        indtable = indsoup.find_all('table', attrs={'class':'infobox vcard'})
    if indtable != []:
        indtabrow = indtable[0].find_all('tr')
        indtabrow_len = len(indtabrow)
        for k in range(0, indtabrow_len):
            intabrow_text = indtabrow[k].get_text()
            if '籍贯' in intabrow_text:
                birthplace = intabrow_text.replace("籍贯","")
                break
    else:
        birthplace = ""
    output.append(birthplace)
    output.append("天津市")
    with open(path+'npc13.csv','a',encoding='utf-8', newline='') as file:
        writer =csv.writer(file)
        writer.writerow(output)


csvfile = csv.reader(open(path+'npc13.csv','r',encoding='utf-8'))
npc13info = []
for row in csvfile:
    npc13info.append(row)

print(npc13info)
