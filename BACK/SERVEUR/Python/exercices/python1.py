# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import *


counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('mrug', 0))

def calcPerimetre(long, larg) :
    return long * larg

longueur = int(input('Entrez la longueur : '))
largeur = int(input('Entrez la largeur : '))
nbPots = 0

perimetre = calcPerimetre(longueur, largeur)
nbPotsEntier = floor(perimetre / 10)
nbPotsReste = perimetre % 10

if nbPotsReste > 0 :
    nbPots = nbPotsEntier + 1
else:
    nbPots = nbPotsEntier
print('Vous avec besoin de ' , nbPots , 'de cirage pour une surface de ', perimetre, ' m²' )
