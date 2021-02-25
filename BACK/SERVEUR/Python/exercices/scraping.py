import urllib3
from bs4 import BeautifulSoup
import requests
li =[]
valListe =[]
requet = requests.get('https://www.afpa.fr/').text


soup = BeautifulSoup(requet,'lxml')
# print(soup)
t = soup.find('select',id ='_rechercheformationhomepageportlet_WAR_rechercheportlet_categorySelector0')
opt = t.find_all('option')

for op in opt:
    li.append(op)

try:
    fil = open('fichiers/options.txt','w')
    for elem in li:
        fil.write(str(elem)+'\n')
    fil.close()
except:
    print('Erreur écriture fichier')
# print(el)

# http = urllib3.PoolManager()
# r = http.request('GET', 'https://www.afpa.fr/')
# soup = BeautifulSoup(r,'html.parser')
# print(soup)
# t = soup.find(class_='logo')
# print(t)
# # print(r.data)

