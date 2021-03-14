# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:09:50 2021

@author: vincent
"""
from tkinter import *
from random import *


# Exercice 3

# fonction qui retourne x1x2y1y2couleur aleatoire

_width=300
_height=300

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

def basquiat(_width,_height):
    def traceDroite():
        # tracé ligne de coordonnées :
        can.create_line(10,190,190,10,width=2,fill="green")
    
    def traceAleat():
        #tupe de couleurs
        tulpCol = ('black','red','green','blue','yellow','violet','orange',
                   'brown','pink','purple','white')
        datas= aleatData(_width,_height,len(tulpCol)-1)
        # print(tulpCol[9])
        can.create_line(datas[0],datas[1],datas[2],datas[3],
                        width=2,fill=tulpCol[datas[4]])

    
        # objet
    fen = Tk()
    # composants (widgets)
    can = Canvas(fen, bg="grey", height=_height, width=_width) 
    can.pack(side = RIGHT)
    btn1 = Button(fen, text= "Quitter", command= fen.quit)
    btn2 = Button(fen, text= "Tracer une ligne", command= traceDroite)
    btn3 = Button(fen, text= "Tracer une ligne aléatoire", command= traceAleat)
    btn1.pack(side =BOTTOM)
    btn2.pack()
    btn3.pack()
    fen.mainloop()
    fen.destroy()
    
basquiat(_width,_height)
