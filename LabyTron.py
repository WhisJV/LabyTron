  #Écrire un programme qui permet de créer une fenêtre
 #nommée Labyrinthe de largeur 1200 pixels, de hauteur 680 pixels,
 #non redimensionnable alignée avec le bord supérieur gauche de l’écran

# ajout d'un canevas 1200 par 680

from tkinter import *
from random import randrange

fenetre=Tk()
fenetre.title("LabyTron") #Titre de la fenêtre
fenetre.resizable(width="True", height="True") #Pour ne pas changer la taille de la fenêtre
fenetre.geometry("1350x900")  #Taille de la fenêtre
fond = Canvas(fenetre, width=1200, height=900, background="white") #Taille du Canevas + couleur du fond
fond.grid(row=0, column=0)

brique=PhotoImage(file="images/brique.gif") #Importation de l'image du mur
personnage=PhotoImage(file="images/moto.gif") #Importation de l'image du personnage
trainee=PhotoImage(file="images/trainee.gif")

def lireniveau(fichier):
    """ affiche le labyrinthe stocké dans le fichier texte
    X correspond à un élément de mur  stocké dans
    "images/brique.gif" 40x40 pixels"""

    fichier = open("D:\LabyTron\iveau0.txt", 'r')  # read, lit fichier texte
    x, y = 0,0
    cases=[]
    for ligne in fichier:
        for colonne in range(len(ligne)):
            case = ligne[colonne]
            liste = case[:-1]
            print (case)
            #print(liste)
            cases.append(liste)
            if case == 'x':
                fond.create_image(x, y, image=brique, anchor="nw")
            if case == 's' :
                fond.create_image(x, y, image=brique, anchor="nw")
            x = x + 30
        x = 0
        y = y + 30
        
    fichier.close()
    return cases

def jouer():
    global flag
    if flag == 0:
        flag = 1
    deplacement()

def deplacement():
    """Mouvement du serpent de coordonnées x,y"""

    global x, y
    ligne,colonne=y//30,x//30
    toast = lireniveau("iveau0")
    #print(ligne,colonne)
    if "Up" == Touches :
        if toast[ligne-1][colonne] == ' ':
         y = y - 30
         fond.create_image(x, y, image=trainee, anchor="nw")
        else :
         perdu = fond.create_text(250, 150, font=('Fixedsys', 18), text="perdu", fill="#FF358B")
    if "Down" == Touches:
      y += 30
      fond.create_image(x, y, image=trainee, anchor="nw")
    if "Left" == Touches:
      x -= 30
      fond.create_image(x, y, image=trainee, anchor="nw")
    if "Right" == Touches:
      x += 30
      fond.create_image(x, y, image=personnage, anchor="nw")
    if flag != 0:
        fenetre.after(80, deplacement)

def up(event):
    global Touches
    Touches = 'Up'

def down(event):
    global Touches
    Touches = 'Down'

def left(event):
    global Touches
    Touches = 'Left'

def right(event):
    global Touches
    Touches = 'Right'

cases=lireniveau("niveau0")
y, x = 30, 30
obstacle = 0
flag = 0
Touches = 'Right'
fenetre.bind('<Up>', up)
fenetre.bind('<Down>', down)
fenetre.bind('<Left>', left)
fenetre.bind('<Right>', right)
Start = Button(fenetre, text='New Game', command=jouer)
Start.grid(column=9,row=0)
personne=fond.create_image(x, y, image=personnage, anchor="nw")
deplacement()
fenetre.mainloop()
