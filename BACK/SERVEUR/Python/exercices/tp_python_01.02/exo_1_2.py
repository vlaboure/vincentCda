import os
from tkinter import *
from random import *

# exercice1
dictAnglais = {'voiture': 'car', 'assiette': 'plate', 'chat': 'cat', 'chien': 'dog'}
dictAnglais['cheval'] = 'horse'


# fonction pour ajouter une entrée au dico
# paramètres : mot, traduction, dictionnaire
# retour : dictionnaire modifié
def ajouterMot(mot1, mot2, dic):
    if mot1 not in dic:
        dic[mot1] = mot2
    else:
        print('mot déjà existant !')
    return dic


# affichage des mots
def printTraduc(dico):
    for m in dico.values():
        print(m)


# suppression de caractère --> supprime tous les mots commençant par un caractère passé en parametre
# paramètres : caractère, dictionnaire
# retour : dictionnaire modifié
def delCar(car, dico):
    dico2 = {}
    for key, val in dico.items():
        if car not in key:
            dico2[key] = val
    return dico2


# print(dictAnglais)
# print(ajouterMot('vélo','bicycle',dictAnglais))
# print(ajouterMot('vélo','bicycle',dictAnglais))
# printTraduc(dictAnglais)
# dicoFin = delCar('a',dictAnglais)
# print(dicoFin)
# *************************************

        # Exercice 2 - lecture loremipsum.txt
# loremipsum = open('fichiers/loremipsum.txt')
# for lin in loremipsum:
#     if(lin !='\n'):
#         print(lin)
#
# loremipsum.close()
#***************************************
        #Exercice 2 tp météo
#         création de fichier avec "chaud","froid","tempéré","glacial","brûlant".
tabClimat = ["chaud", "froid", "tempéré", "glacial", "brûlant"]
tabClimatEn = ["hot", "cold", "moderate", "icy", "ardent"]

def wrInFile(file,tab):
    try:
        for w in tab:
            file.write(w + '\n')
    except IOError:
        raise RuntimeError from None

def recMeteo():
    try:
        with open('fichiers/climat.txt', 'w') as wrClimat:
            wrInFile(wrClimat, tabClimat)
            wrClimat.write('\nTraduction anglaise : \n')
            wrInFile(wrClimat, tabClimatEn)
    except IOError:
        raise RuntimeError from None
    finally:
        wrClimat.close()
# recMeteo()
#*********************************************
        # Lister rep récursif

# méthode récursive pour test avec algo

# affiche le repertoire courant et la liste des repertoires
# les répertoires du répertoire courant et la liste de leurs répertoires 
lstAllRep = []
def parse():
    rep = []
    curDir = os.getcwd()
    dirs = os.listdir(curDir)
    for f in dirs :        
        if os.path.isdir(f): # si f est un dossier
            rep.append(os.getcwd()+ '/' + f)            
            lstAllRep.append(os.path.split(curDir)[1] + '/' + f)
            os.chdir(f) # On va lister son contenu
            parse()
            os.chdir('../') # On revient au répertoire précédent
    return rep

tabRep = parse()
print('Répertoires et sous repertoires contenus dans ' , os.path.split(os.getcwd())[1])
for el in sorted(lstAllRep):
    print(el)

#*********************************************
# Exercice 3

# fonction qui retourne x1x2y1y2couleur aleatoire

_width=300
_height=300


def basquiat(_width,_height):
    def aleatData(width,height,ncol):
        # liste des coordonnées
        dr = []    
        # en fonction des bornes width on sort x1 x2    
        # en fonction des bornes height on sort y1 y2
        elements = [width,height,ncol]
        # def numAleat(elements):
        # sortie aléatoire avec bornes --> maxim = width/height/color
        for i in range(len(elements)):
            if i< 2:
                for n in range(2):                
                    while True:
                        sort = randint(1,elements[i])
                        if not sort in dr:
                            dr.append(sort)
                            break
            else:
                 dr.append(randint(1,elements[i]))
        return dr

    def traceDroite():
        # tracé ligne de coordonnées :
        can.create_line(10,190,190,10,width=2,fill="green")
    
    def traceAleat():
        #tupe de couleurs
        tulpCol = ('black','red','green','blue','yellow','violet','orange',
                   'brown','pink','purple','white')
        datas= aleatData(_width,_height,len(tulpCol)-1)
        print(datas[3]-1)
        # print(tulpCol[9])
        can.create_line(datas[0],datas[1],datas[2],datas[3],
                        width=2,fill=tulpCol[datas[4]])

    
        # objet
    fen = Tk()
    # composants (widgets)
    can = Canvas(fen, bg="grey", height=_height, width=_width) 
    can.pack(side = LEFT)
    btn1 = Button(fen, text= "Quitter", command= fen.quit)
    btn2 = Button(fen, text= "Tracer une ligne", command= traceDroite)
    btn3 = Button(fen, text= "Tracer une ligne aléatoire", command= traceAleat)
    btn1.pack(side =BOTTOM)
    btn2.pack()
    btn3.pack()
    fen.mainloop()
    fen.destroy()
    
# basquiat(300,300)






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















