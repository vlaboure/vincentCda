# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 09:49:22 2021

@author: vincent
"""

#pgcd
import math
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
import platform
import numpy as np
import pandas as pan

# print(math.gcd(15,5))

# #ppcm --> valeur 1 X valeur 2 / pgcd
# def ppcm(a,b) :
#     return (a * b) / math.gcd(a,b)

# print(ppcm(155,5))

# plt.plot([1,5,-2],[22,5,.1])
# x = np.linspace (-5, 5, 100)
# y = np.sin (x)
# plt.plot (x, y)
# plt.show ()

# abscisse = np.linspace (0,7,100)#traçage de l'abscisse
# ordonnee = [2*math.sin(x) + x for x in abscisse]
# plt.plot (abscisse, ordonnee)
# plt.show () 

# x = [1,2,3,4,5]
# y = [7,11,9,3,6]
# largeur = 1
# plt.bar(x, y, largeur)
# plt.show()
# plt.close()




 # print(os.getcwd()) #--> retourne une string
if os.path.exists('c:/users'):
    print('toto est là')
else:
    print('où est passé toto ??')

mydir ='uu'
p = Path(mydir)
if p.is_dir:
    print('répertoire')
elif p.is_file:
    print('repertoire')
else:
    print('Erreur')


p1 = Path(os.getcwd())
# print(p1.absolute())#chemin courrant
print(p1.as_uri())




#**********plateform
infos = ('Plate forme info:', platform.uname())
print (infos[1][3])


m = np.linspace (0, 20, 8)
print(m)

#numpy
my_2darray = np.array([[1,2,3],[4,5,6]])
print(my_2darray,'\n')
t= (my_2darray[:,0])
print(t)


# tableau simple 
data = np.array(['P', 'y', 't', 'h', 'o' , 'n'])
s = pan.Series(data)
print(s)

s = pan.Series (data, index = [4, 7, 8, 9, 13 , 17])
print(s)

dic = {'p':[1,2],'y':[4,66],'t':[88,4],'h':[1,17],'o':[222,3]}
d = pan.Series(dic, index=['p','z','a','n','o'])
print(d)

#DataFrame
dp = pan.DataFrame(dic)
print(dp)

df= pan.DataFrame(d)
print(df, 'data frame')

dictData = {'ID' : [1, 2, 3] , 'Nom': ['Natalie', 'Robert', 'Bernard'], 'Age': [22, 37, 29], 'Taille': [170, 190, 181]}
df = pan.DataFrame(dictData)
print(df)

#***********
s = pan.Series([0, 1, 2, 3],index = ['a','b','c','d']) 
#extraire le deuxième élément 
print(s['b'])
print(s[[1,2]])
print(s[1:4])






 
    
    
    
    
    
