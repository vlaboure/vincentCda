# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 11:11:45 2021

@author: vincent
"""
from tkinter import *
from random import *


def testEnter(sender,name):
    if not sender.get().isdigit():        
        print ('Entrez un nombre')
    if name == 'age':
        print('sender est un age')
    

_width='400'
_height='300'

main = Tk()
main.geometry(_width +'x' + _height)

v= StringVar()

Label(main, text = 'votre age :',font=('arial',12)).grid(sticky='W',row=0,column=0,padx=2,pady=5)
Label(main, text = 'prix du billet (hors réduction) : ' ,font=('arial',12)).grid(sticky='W',row=1,column=0,padx=2,pady=5)
Label(main, text = 'votre réduction est de : ' ,font=('arial',12)).grid(sticky='W',row=2,column=0,padx=2,pady=5)
labelReduc = Label(main, textvariable=v,font=('arial',12))
labelReduc.grid(row=2, column=1, pdx=2, pady=5)

age = Entry(main)
age.grid(row=0,column=1)
age.bind("<FocusOut>",lambda event: testEnter(age,'age'))

prix = Entry(main)
prix.grid(row=1,column=1)
prix.bind("<FocusOut>",lambda event: testEnter(prix,'prix'))

bnValid = Button(main,text='Valider l\'opération',command = '')
bnValid.grid(row=3,column=1)

bnQuit = Button(main, text= "Quitter", command= main.quit)
bnQuit.grid(row=4,column=3)
mainloop()
fen.destroy()
