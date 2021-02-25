from math import *
from tkinter import*
from PIL import Image,ImageTk

import tkinter.font as tkFont

# def affImage():
#     direct=os.getcwd()+'\\fichiers\\'
#     maFenetre = Tk()
#     maFenetre.title(direct+"/image")
#     maFenetre.geometry('300x200')
#     load = Image.open('watch.png')
#     photo = ImageTk.PhotoImage(load)
#     label_image = Label(maFenetre,image=photo)
#     label_image.place(x=0,y=0)
#     maFenetre.mainloop()
    
# saisie = Tk()
# hei=200 // 5
# left=20
# saisie.geometry('400x200')

# lab1= Label(cadreLab,text = 'Entrez un nombre',font=('courrier',12),width=20)

# entN= Entry(cadreLab,width=30)

# lab2=Label(cadreEnt,text = 'Voici le double',font=('courrier',12))
         
# saisie.mainloop()

from tkinter import *


#exercice 1
# def show_answer():
#     Ans = int(num1.get())*2
#     # blank.insert(0, Ans)
#     num2.insert(0,Ans)
    


# main = Tk()
# main.geometry('300x100')
# Label(main, text = "Enter un chiffre:",font=('courrier',12)).grid(row=0,padx=5)
# Label(main, text = "Voici le double:",font=('courrier',12)).grid(row=1,padx=5)
# # Label(main, text = "The Sum is:").grid(row=2)

# num1 = Entry(main)
# num2 = Entry(main)
# # blank = Entry(main)
# num1.grid(row=0,column=1)
# num2.grid(row=1,column=1)


# Button(main, text='Quitter', command=main.quit).grid(row=4, column=0, sticky=N, pady=5)
# Button(main, text='calculer', command=show_answer).grid(row=4, column=1, sticky=N, pady=5)

# mainloop()

#exercice 2 
# def listeDiviseurs():
#     # l = []
#     n = int(num1.get())
#     s=' '
#     # for i in range(1, n+1):
#     #     if n % i == 0 :
#             # l.append(i)
#             # s+= str(i)
#     v.set(s)


# main = Tk()
# main.geometry('300x100')
# # v= StringVar()

# Label(main, text = 'Entrez la valeur de N',font=('arial',12)).grid(row=0,column=0,padx=5,pady=5)
# Label(main, text = 'diviseurs de N : ' ,font=('arial',12)).grid(row=1,column=0,padx=5,pady=5)
# lblAns = Label(main,textvariable=v, font=('arial',12))
# lblAns.grid(row=1, column=1,padx=5,pady=5)

# num1 = Entry(main)
# num1.grid(row=0,column=1)



# bn = Button(main,text='Valider l\'opération',command = listeDiviseurs())
# bn.grid(row=2,column=1)
# mainloop()
def listeDiviseurs():
    nb = int(num1.get())
    s='  '
    for i in range(1, nb+1):
        if nb % i == 0 :
            # l.append(i)
            s+= ' '+str(i)
    v.set(s)

main = Tk()
main.geometry('300x100')

v= StringVar()

Label(main, text = 'Entrez la valeur de N',font=('arial',12)).grid(row=0,column=0,padx=5,pady=5)
Label(main, text = 'diviseurs de N : ' ,font=('arial',12)).grid(row=1,column=0,padx=5,pady=5)

lblAns = Label(main,textvariable=v, font=('arial',12))
lblAns.grid(row=1, column=1,padx=5,pady=5)

num1 = Entry(main)
num1.grid(row=0,column=1)

bn = Button(main,text='Valider l\'opération',command = listeDiviseurs)
bn.grid(row=2,column=1)
mainloop()

























