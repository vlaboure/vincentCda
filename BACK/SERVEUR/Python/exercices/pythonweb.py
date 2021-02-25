import os, sys

name = input("Entrez votre prénom: ")
try:
    os.mkdir("./"+name)
    os.mkdir("./"+name+"/BACK")
    os.mkdir("./"+name+"/BACK/BDD")
    os.mkdir("./"+name+"/BACK/BDD/SQL")
    os.mkdir("./"+name+"/BACK/SERVEUR")
    os.mkdir("./"+name+"/BACK/SERVEUR/PHP")
    os.mkdir("./"+name+"/FRONT")
    os.mkdir("./"+name+"/FRONT/DYNAMIQUE")
    os.mkdir("./"+name+"/FRONT/DYNAMIQUE/JAVASCRIPT")
    os.mkdir("./"+name+"/FRONT/STATIQUE")
    os.mkdir("./"+name+"/FRONT/STATIQUE/BOOTSTRAP")
    os.mkdir("./"+name+"/FRONT/STATIQUE/CSS")
    os.mkdir("./"+name+"/FRONT/STATIQUE/HTML")
    print("All good in the hood ~ au boulot")
except:
    print('erreur')
