# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 08:46:11 2021

@author: 59013-38-07
"""
from math import * 

# def calcPerimetre(L , l):
#     return L * l


# print (calcPerimetre(2 , 5))

# def fact(n):
#     if n == 0 :
#         return 1
#     return fact(n -1 ) * n

# n = int(input('entrez un nombre dont vous voulez la factorielle : '))
# print(fact(n))

# tab =[2,8,9,4]
# tab.append(15)
# print(tab)
# print(len(tab))

# for el in range(0,5):
#     print(el)

# tabl = [t for t in range(0 , 5)]
# print(tabl)

# m = [1, 2, 3] 
# mm = [m, m, m] 
# m[0] = 100
# print(mm)

# l = [15,2,18,9]
# tab = [t for t in l if t>10]
# print(tab)

#                                   matrices
# t1 = ((1,5,8), (10,1,2),(20,4,3))
# t2 = ((1,2,11), (1,11,2),(2,14,3))

# def sommeMatrice(m1, m2):
#     result = []
#     for i in range(len(m1)):       
#         res=[]
#         for j in range(len(m1)):            
#             res.append(m1[i][j]+m2[i][j])
#         result.append(res)    
#     return result
        
# print(sommeMatrice(t1,t2))

#                   coordonnées
# tabDist = []

# def calcDist(p1, p2):
#     return sqrt((p2[0] - p1[0]) **2 +  (p2[1] - p1[1]) **2)

# def entreCoordonnes():
    
#     for i in range(3):
#         dist = []             
#         dist.append(float(input('entrez une valeur de x : ')))
#         dist.append(float(input('entrez une valeur de y : ')))
#         tabDist.append(dist)
#     return(tabDist)

# entreCoordonnes()

# print('distance AB :',calcDist(tabDist[0] , tabDist[1]))    
# print('distance BC :',calcDist(tabDist[1] , tabDist[2]))   
# print('distance CD :',calcDist(tabDist[0] , tabDist[2]))   

def compCaract(chaine):
    return chaine[0].lower() == chaine[len(chaine)-1].lower()
    

print(compCaract('il pleuti'))

def palindrome(string):
    for i in range(string):
        

print(palindrome('hello'))
















