# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 08:53:20 2021

@author: 59013-38-07
"""
from math import *
import numpy
# import random


# l = [5,4,9,22,1,3]
# def tri_rapide(list):
#     inferieur = []; pivot = []; superieur = []
#     if len(list) < 2:
#         return list
#     pivotNombre = random.choice(list)
#     for i in list:
#         if i < pivotNombre:
#             inferieur.append(i)
#         elif i > pivotNombre:
#             superieur.append(i)
#         else:
#             pivot.append(i)
#     return tri_rapide(inferieur) + pivot + tri_rapide(superieur)

# lt = tri_rapide(l)

# print (l)
# print (lt)

# txt = 'un text'
# ent = 2
# dec = 2.2

# print

# r = float(input('entrez le rayon : '))
# h = float(input('entrez la hauteur : '))
from math import asin

compteur = 0
while compteur<5:
    print(compteur, compteur<5)
    compteur += 1
    print(compteur<5)
# hypot = float(input('saisir l\'hypotenuse du trianle :'))
# oppose = float(input('saisir le côté opposé à l\' hypotenuse du trianle :'))
# angle = degrees(asin((oppose / hypot)))
                     
print('Angle du triangle :' , '%.2f' % angle, ' degrés')

# annee = int(input('Entrez une année : '))

# if annee % 400 == 0 :
#     print('année  bisextile')
# elif annee % 4 == 0:
#     print('année  bisextile')
# else:
#     print(' année non bisextile')

# for compteur in range(1,10):
#     print(compteur, '* 9 =', compteur*9)
# print("Fin de la boucle")

# chaine1 = input('saisir la première chaine de caractère :')
# chaine2 = input('saisir la seconde chaine de caractère :')
# if len(chaine1) > len(chaine2):
#     print('chaine 1 plus grande')
# else:
#     print('chaine 2 plus longue')

devise = input('choisir devise E ou $ :')
prix = float(input('entrez un prix :'))
if devise == 'E':
    print(prix,'euros en dollard donnent: ', prix * 1.21, ' $')
elif devise == '$':
    print(prix,'dollard en euro donnent: ', prix * 0.83, ' €')
else:
    print('erreur')
    
























