# Écrire un programme qui permet de créer une fenêtre
# nommée Labyrinthe de largeur 1200 pixels, de hauteur 680 pixels,
# non redimensionnable alignée avec le bord supérieur gauche de l’écran

# ajout d'un canevas 1200 par 680

from tkinter import *
from random import randrange

fenetre = Tk()
fenetre.title("LabyTron")  # Titre de la fenêtre
fenetre.resizable(width="True", height="True")  # Pour ne pas changer la taille de la fenêtre
fenetre.geometry("1350x900")  # Taille de la fenêtre
fond = Canvas(fenetre, width=1200, height=900, background="white")  # Taille du Canevas + couleur du fond
fond.grid(row=0, column=0)
fenetrebackground=fenetre.create_image((450, 360), image=background)
fenetre.pack()

brique = PhotoImage(file="images/brique.gif")  # Importation de l'image du mur
personnage = PhotoImage(file="images/moto1.gif")  # Importation de l'image du personnage
personnageg = PhotoImage(file="images/moto2.gif")
personnageb = PhotoImage(file="images/moto3.gif")
personnageh = PhotoImage(file="images/moto4.gif")
trainee = PhotoImage(file="images/trainee.gif")
arrivee = PhotoImage(file="images/arrivee.gif")
background = PhotoImage(file="images/arriere.gif")

briques = []


def lireniveau(fichier):
    """ affiche le labyrinthe stocké dans le fichier texte
    X correspond à un élément de mur  stocké dans
    "images/brique.gif" 30x30 pixels"""

    fichier = open("niveau0.txt", 'r')  # read, lit fichier texte
    x, y = 0, 0
    cases = []
    for ligne in fichier:
        for colonne in range(len(ligne)):
            case = ligne[colonne]
            if case == 's':
                fond.create_image(x * 30, y * 30, image=arrivee, anchor="nw")
            if case == 'x':
                briques.append([x, y])
                fond.create_image(x * 30, y * 30, image=brique, anchor="nw")
            x += 1
        x = 0
        y += 1
    fichier.close()


def jouer():
    global flag, flag2
    if flag2 != 1 :
        if flag == 0:
            Start.configure(text="Stop")
            flag = 1
            deplacement()
        else:
            flag = 0
            Start.configure(text="Start")

def rejouer():
    global flag2
    
    flag2 = 0

def deplacement():
    """Mouvement du serpent de coordonnées x,y"""
    global x, y, flag, flag2 
    # print(ligne,colonne)

    px = x // 30
    py = y // 30 

    if "Up" == Touches:
        y -= 30
        fond.create_image(x, y, image=personnageh, anchor="nw")
    if "Down" == Touches:
        y += 30
        fond.create_image(x, y, image=personnageb, anchor="nw")
    if "Left" == Touches:
        x -= 30
        fond.create_image(x, y, image=personnageg, anchor="nw")
    if "Right" == Touches:
        x += 30
        fond.create_image(x, y, image=personnage, anchor="nw")

    if flag != 0:
        fenetre.after(200, deplacement)

    for brique in briques:
        if brique[0] == px and brique[1] == py :
            flag2 = 1
            flag = 0
            perdu=fond.create_text(250,150,font=('Fixedsys',52),text="Tu es nul :)")
            break


    

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


lireniveau("niveau0")
x = 30
y = 30
flag = 0
flag2 = 0 
Touches = 'Right'
fenetre.bind('<Up>', up)
fenetre.bind('<Down>', down)
fenetre.bind('<Left>', left)
fenetre.bind('<Right>', right)
Start = Button(fenetre, text='Start', command=jouer)
Start.grid(column=9, row=0)
rejouer = Button(fenetre, text='Rejouer', command=rejouer)
rejouer.grid(column=10, row=0)
personne = fond.create_image(x, y, image=personnage, anchor="nw")
deplacement()
fenetre.mainloop()
