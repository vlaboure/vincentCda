# exercice1
dictAnglais = {'voiture':'car','assiette':'plate','chat':'cat','chien':'dog'}
dictAnglais['cheval']= 'horse'
def ajouterMot(mot1, mot2, dic):
    if mot1 not in dic:
        dic[mot1]=mot2
    else:
        print('mot déjà existant !')
    return dic
def printTraduc(dico):
    for m in dico.values():
        print(m)
def delCar(car, dico):
    dico2={}
    for key, val in dico.items():
        if car not in key:
            dico2[key] = val
    return dico2

# print(dictAnglais)
# print(ajouterMot('vélo','bicycle',dictAnglais))
# print(ajouterMot('vélo','bicycle',dictAnglais))
# printTraduc(dictAnglais)
dicoFin = delCar('a',dictAnglais)
print(dicoFin)
# *************************************


