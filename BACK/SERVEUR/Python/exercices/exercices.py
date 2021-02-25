import math
from random import *

def premiers(n):    
    # prem=[]
    k=2
    prem= list(range(2,n))
    prem=[i for i in prem if i%k!=0 or i==2]
    nRacine=math.sqrt(n)    
    while k<nRacine:
        [p for p in prem if p<k]
        k=prem[prem.index(k)+1]
    return prem


def premierSup(n):
    i = 2
    n+=1
    divisible = True
    while divisible:
        if i < n and n % i != 0:
        i = i + 1
    if i == n :
        print('Le nombre', n, 'est premier ! Fantastique !')
    
    return i    

print(premierSup(53))


# def inverserMot(stri):
#     # return ''.join(reversed(stri))
#     # return stri[::-1]
# print(inverserMot('test'))

# phrase = input('entrez une phrase\n')
# mots = phrase.split(' ')
# liste = []
# max = 0
# motMax = ''
# for mot in mots:
#     if len(mot) > max:
#         max = len(mot)
#         motMax = mot
#     if mot.startswith('a'):
#         liste.append(mot);
# for motA in liste:
#     print('liste de mot(s) débutant par a  : ', motA)
# print('le mot le plus long est : ', motMax)
# liste = list(range(2, 10, 3)) # [2, 5, 8]
# print(liste)
# st = ''
# j=1
# n=0
# while n < 4:
#     n = int(input('Entrez une taille pour votre sapin (minimum 4) : '))

# for i in range(1,n * 2,2):    
#     print(i*'^')


# def listAnimaux(liste_animaux):    
#     liste = (liste_animaux[::-1])
#     print(liste)
#     for animal in reversed(liste_animaux):
#         print(animal)
#     liste = sorted(liste_animaux)
#     print('triée : ',)
#     liste_animaux.append('troll')
#     for animal in (liste_animaux):
#         print(animal)
#     print('**************animaux domestiques')
#     liste_domestiques = liste_animaux[slice(0,3)]
#     for animal in (liste_domestiques):
#         print(animal)
#     print('***************animaux sauvages')
#     for el in liste_domestiques:
#         liste_animaux.remove(el)
#     for animal in liste_animaux:
#         print(animal)

#         # création d'un tableau avec l'association de chaque sauvage avec les domestiques
#     listedb = [[[a, d] for a in (liste_animaux)] for d in (liste_domestiques)]
#     for listAnimaux in listedb:
#         print(listAnimaux)

# listAnimaux(["lapin","chat", "chien", "chiot", "dragon"])
# #**************************
#       #tri recursif
# def quicksort(t):
    
#    # pivot = []
#     t1 = []
#     t2 = []
#     if len(t) < 2 :
#         return t
#     else:
#         pivotn = t[randint(0,len(t)-1)]
#         for x in t:
#             # if x == pivotn:
#             #     pivot.append(x)
#             # else:
#                 if x<pivotn:
#                     t1.append(x)
#                 else: 
#                     t2.append(x)            
                
#         return quicksort(t1)+quicksort(t2)

# print(quicksort([2588,5,22,8,1,255,0,80]))        

def tri(l):
    

# def pgcd(a,b):
#     if b == 0:
#         return a
#     else:
#         res = a%b    
#     return(pgcd(b,res))

# print('le pgcd est : ',pgcd(22,8))

# def pgcd2(x,y):
#     while x - y:
#         if x < y:
#            x += y
#            y =x - y
#            x -=y
          
#         x -= y
#     return abs(x)

# print('pgcd sans recursif',pgcd2(22,8))

# def test(n):
#     t=[]
#     n1 = 10 **n -1    
#     u = 0
#     def calcn(n1,u):
#         print('coucou',n1)
    
#     calcn(n1,u)

# test(3)    
