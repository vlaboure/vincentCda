# -*- coding: utf-8 -*-

# Created on Tue Feb 16 09:58:32 2021
# @author: 59013-38-07

import pathlib
import os
import math

# direct = os.getcwd()
# fichier = open(direct+'/fichiers/items.txt','r')
# for lin in fichier:
#     print(lin)
# # print(fichier.read())
# # line= fichier.readline()
# # while line:
# #     print(line)
# #     line= fichier.readline()

# print('***************')

# fichier.close()

# liste = list(range(1,10))
# liste = [l*'^' for l in liste if l%2 ==0]

# fichier = open(direct+'/fichiers/items.txt','w')
# fichier.writelines(liste)
# fichier.close()
# fichier = open(direct+'/fichiers/items.txt','r')
# line = 
# for lin in fichier:
#     print(lin)
import matplotlib.pyplot as plt
import math
from bs4 import BeautifulSoup

    # Parser des textes avec beautifulSoup
html_doc ='''
    <html> 
    <head> 
    <title>Titre de votre site</title> 
    </head> 
    <body> 
    <p>Texte à lire 1</p>
    <p>Texte à lire 2</p>
    </body> 
    </html> 
'''
soup = BeautifulSoup(html_doc,'lxml')
for p in soup.find_all('p'):
    n = BeautifulSoup('<pre>%s</pre>' %p.string,'lxml')
    p.replace_with(n.body.contents[0])
print(soup)
soup.find_parent('p')

raw_html = """
<h1>Vente de véhicule d’occasion</h1>
<ul class="cars-listing">
    <li class="car-listing">
        <div class="car-title">
            Coccinelle Volkswagen
        </div>
        <div class="car-description">
            <span class="car-make">Volkswagen</span>
            <span class="car-model">Coccinelle</span>
            <span class="car-build">1973</span>
        </div>
        <div class="sales-price">
            € <span class="car-price">14 998 €</span>
        </div>
    </li>
</ul>  
 """
# parser le code source HTML enregistré dans raw_html
html = BeautifulSoup(raw_html, 'html.parser')
# extraire le contenu de la balise avec la classe « car-title »
car_title = html.find(class_='car-title').text.strip()
# si cette voiture est une coccinelle Volkswagen
if car_title == 'Coccinelle Volkswagen':
# passer du titre de la voiture à la balise <li></li>
    html.find_parent('li')

# déterminer le prix de la voiture
car_price = html.find(class_ = 'sales-price').text.strip()

# indiquer le prix de la voiture
print(car_price)


def cercle(r,teta):
    t=0
    xa=[]
    ya=[]
    direct=os.getcwd()+'/fichiers'
    fichier =open('fichiers/items.txt','w')
    while t < teta:
        fichier.write(str(r*math.cos(t)) +' '+ str(r*math.sin(t))+'\n')
        t+=0.1
        r+=0.1

    fichier.close()
    x = []
    y = []
    with open('fichiers/items.txt', "r") as f_in:
        for line in f_in:

            coords = line.split()
            x.append(float(coords[0]))
            y.append(float(coords[1]))
    
    plt.figure(figsize=(8,8))
    mini = min(x+y) * 1.2
    maxi = max(x+y) * 1.2
    plt.xlim(mini, maxi)
    plt.ylim(mini, maxi)
    plt.plot(x, y)
    plt.savefig('fichiers/spirale.png')
    
#cercle(0.5, 4*math.pi)

import csv
import pandas

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
csvfile.close()

with open('names.csv','r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        print(row)
csvfile.close()

pr = pandas.read_csv('names.csv')
print(pr)