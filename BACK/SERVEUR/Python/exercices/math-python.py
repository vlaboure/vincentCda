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

def pgcd(a,b):
    if b == 0:
        return a
    else:
        res = a%b    
    return(pgcd(b,res))

print(pgcd(3,15))





















 
    
    
    
    
    
