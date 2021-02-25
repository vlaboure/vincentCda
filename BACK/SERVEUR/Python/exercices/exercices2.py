# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 19:46:26 2021

@author: vincent
"""
import math
import string

#♦tp révisions python
#exercice 1
# L = ["Python", "Java", "C++", "Javascript"]
# L[0],L[-1] = L[-1],L[0]
# print(L)

#exercice 2

# def paireImpaire(s):
#     l_even = ()
#     l_odd = ()
#     for i, el in enumerate(s):
#         if i%2 == 0:
#             l_even += (el,)
#         else:
#             l_odd += (el,)
#     # print(i_even)
#     # print(i_odd)
#     tupple3=(tuple(l_even),tuple(l_odd))
#     print (tupple3)

            
# paireImpaire(L)

#exercice 3
# def listeDiviseurs(n):
#     l = []
#     for i in range(1, n+1):
#         if n % i == 0 :
#             l.append(i)
#     return l

# n= int(input('entrez un nombre : '))
# ld = listeDiviseurs(n)
# print('liste des diviseurs de ',n,ld)

#exercice 4
#j'utilise la liste L 
# def isInList(_list, name):
#     return name in _list

# o = input('suis je dans la liste : ')
# o = o[0].upper()+o[1:].lower()
# print(isInList(L , o))

#exercice 5
# def createDico(li):
#     array = li.split(' ')
#     dico = {}
#     # ajout des mots dans le dico
#     for d in array:
#         dico[d]=len(d)
#     return dico

# phrase = input('entrez une phrase, je vous en dit plus..\n')
# print('nous allons compter les mots: ',createDico(phrase))

#exercice 6
def tridico(d):
    dico={}
    for key, val in d.items():
        val = sorted(val)
        dico[key]= val
    return dico

dico = {'a1': [21, 17, 22, 3], 'a2': [11, 15, 8, 13],
          'a3': [7, 13, 2, 11] , 'a4':[22,14,7,9]}
dico2 = tridico(dico)

for key, val in dico2.items():
    print('clé ',key,'valeur ', val)

#     return pgcd(b, r)
# #♥exercice 7
def pgcd(a, b):
    if b == 0 :
        return a
    else:
        r = a % b
    return pgcd(b,r)

# a = int(input('entrez le premier nombre : '))
# b = int(input('entrez le deuxième nombre : '))
# print('le pgcd de ',a , 'et ',b,' est ',pgcd(a,b))

# exercice 8
def ppcm(a,b):
    return a * b / pgcd(a,b)
# a = int(input('entrez le premier nombre : '))
# b = int(input('entrez le deuxième nombre : '))
# print('le ppcm de ',a , 'et ',b,' est ',ppcm(a,b))


#exercice 9
# ******************************************
# x=int(input("Please enter a number: "))
# for n in range (x,x+10):
#     if n>1 and n>=x:
#         for i in range(2,n):
#             if(n%i)==0:
#                 break
#         else:
#             print(n)
#             break

def premiers(n):
  prem=list(range(2,n+1))
  k=2
  nRacine=math.sqrt(n)
  # limite pour le controle de la divisibilité le diviseur donnant 0 en résultat
  # de la division doit être inférieur à la racine carré du nombre testé
  while k<nRacine:
    # on modifie la liste en veririant si p non divisible par k
    # ou p <= k
    prem=[p for p in prem if p<=k or p%k!=0]
    # on met dans k les premier nombre premiers
    k=prem[prem.index(k)+1]  # nouveau nombre premier
  return prem


def premierSup(n):
    i = n
    divisible = True      
    # if n == 3:
    #     return 3
    # elif n<3:
    #     return 2
    # else:
    #     nRacine = int(math.sqrt(n))  
    #     prem = premiers(n)
    #     # if n == 1: return 2
    #     # if n > 3:
    #     #     prem = premiers(nRacine)
    #     # else:
            
      
    while divisible :
        for p in range(2,n):
            if i % p == 0:
                divisible = True
                # evite la boucle infinie avec n<4
                if n != 3:
                    # si 3 ne pas incrémenter
                    i+=1
                else:
                    # pour sortir de la boucle si 3 
                    divisible = False
                break            
            else:
                divisible = False          
    return i
# n=-1    
# while n<0: 
#     n = int(input('Entrez un nombre je donne le premier nombre premier suivant : '))
# print('Le premier nombre indivisible après ',n,' est ',premierSup(n))



#exercice 10
# def pgds(n):
#     max = 0
#     for i in range(1, n-1):
#         # print(i)
#         if n % i == 0 and i > max :
#             max = i
#     return max

# n= int(input('Entrez un nombre :'))
# print('le plus grand diviseur de ',n,' est ',pgds(n))


#exercice 11
def toUp(s):
    chaine=[]
    for el in s:
        chaine.append(el.upper())
    return chaine

L = ["Python", "est", "un", "langage", "de", "programmation"]

# majuscule = [toUp(L)]
# print(majuscule)
# print(L)
    
#exercice 12
def countUpLow(s):
    maj=minus =0
    for i in range(len(s)):
        if s[i].isspace() == False:
            if s[i].isupper(): 
                maj+=1
            elif s[i].islower:
                minus+=1
    return minus, maj
 
print(countUpLow('Je suis un Beau Gars'))

#exercice 13
def charstr(s):
    sortie =[]
    for e in range(len(s)):
        sortie.append(s[e])
    return sortie

print(charstr('Je suis un Beau Gars'))

#exercice 14

def supMoyenne(l):
    ret = []
    for el in l :
        if el >= 10:
            ret.append(el)
            del el
    return (ret, l)

# notes = [12 , 4 , 14 , 11 , 18 , 13 ,7, 10 , 5 , 9 , 15 , 8 , 14 , 16]
# moy, tt = supMoyenne(notes)

#exercice 15

def hypertexte(chaine):
    toto='toto'
    return('<a href="%s.com"></a>' %chaine)

print(hypertexte('test_de_chaine'))


#exercie 16
def listeCommuns(s1,s2):
    sortie = []
    l1 = s1.split(' ')
    l2 = s2.split(' ')
    for el in l1:
        for el2 in l2:
            if el == el2:
                sortie.append(el)
    return sortie

# print(listeCommuns('test de chaine', 'test autre mots chaine'))

#exercice 17
def compter(s):
    out = ''.join([i for i in s if i not in string.punctuation])
    tabChaine = out.split(' ')
    return len(tabChaine)

print('la chaine comporte %d caractèress'%(compter('test de chaine.')))












