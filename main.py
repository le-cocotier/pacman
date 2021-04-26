# Créé par Nicolas, le 28/09/2017 en Python 3.2
# Amélioré par alpha_quote et lambda_quote

from tkinter import *


def detection(x, y, add_x, add_y):
    global niveau, activate, tableau
    x1, y1, x2, y2 = canvas.coords(perso)  # on récupère les coordonnées du perso
    if tableau[y][x] != '1':
        if tableau[y][x] == '0':
            canvas.coords(perso, x1 + add_x, y1 + add_y, x2 + add_x, y2 + add_y)  # on modifie les coordonnées
        if tableau[y][x] == '2':
            mod(x, y, '3')
            canvas.coords(perso, x1 + add_x, y1 + add_y, x2 + add_x, y2 + add_y)  # on modifie les coordonnées
        if tableau[y][x] == '3':
            canvas.coords(perso, x1 + add_x, y1 + add_y, x2 + add_x, y2 + add_y)  # on modifie les coordonnées
        if tableau[y][x] == '4':
                if niveau != 2:
                    canvas.coords(perso, x1 + add_x, y1 + add_y, x2 + add_x, y2 + add_y)  # on modifie les coordonnées
                    niveau += 1
                    canvas.coords(perso, 1, 1, 19, 19)
                    level()
                    wall(tableau)
                    fen.update()
                else:
                    win(fen)
        fen.update()


def deplace(sens, add_x, add_y):
    global tableau
    x1, y1, x2, y2 = canvas.coords(perso)  # on récupère les coordonnées du perso
    x, y = conv(x1 + add_x), conv(y1 + add_y)
    x, y = int(x), int(y)
    if sens == "d":
        if (x1, y1) == (361, 181):
            canvas.coords(perso, 1, 181, 19, 199)
        if x2 < r_conv(len(tableau[0])) - 20:
            detection(x, y, add_x, add_y)
    if sens == "g":
        if x2 > 20:
            detection(x, y, add_x, add_y)
    if sens == "h":
        if y2 > 20:
            detection(x, y, add_x, add_y)
    if sens == "b":
        if y2 < r_conv(len(tableau)) - 20:
            detection(x, y, add_x, add_y)


def level():
    global tableau
    open_file = open(("level.txt"), "r")
    read_file = open_file.read()
    tableau = list(read_file.split("\n"))
    fen.update()


def win(a):
    reset(fen)
    fen.title("victoire")
    fen.geometry('400x300')
    txt = " Vous avez trouvé la sortie"
    label = Label(fen, text=txt, font=20)
    label.grid()


def rect(a, b, c):
    canvas.create_rectangle(a, b, a + 20, b + 20, fill=c, outline=c)


def cercle(a, b, c):
    canvas.create_oval(r_conv(a)+1, r_conv(b)+1, r_conv(a)+19, r_conv(b)+19, fill=c)  # création du personnage #


def conv(x):
    a = x // 20
    return a


def r_conv(x):
    a = x * 20
    return a


def wall(tab):
    global activate
    activate = 0
    for i_ligne in range(len(tab)):
        ligne = tab[i_ligne]
        for i_colonne in range(len(ligne)):
            if ligne[i_colonne] == '1':
                rect(r_conv(i_colonne), r_conv(i_ligne), '#000')
            if ligne[i_colonne] == '2':
                cercle(i_colonne, i_ligne, 'red')
                activate += 0
            if ligne[i_colonne] == '3':
                cercle(i_colonne, i_ligne, '#5CFF65')
            if ligne[i_colonne] == '4':
                rect(r_conv(i_colonne), r_conv(i_ligne), '#39FF14')


def mod(x, y, chiffre):
    global tableau
    modification = tableau[y][:x] + chiffre + tableau[y][x+1:]
    tableau = tableau[:y] + [modification] + tableau[y+1:]
    wall(tableau)


def reset(fenetre):
    for widget in fenetre.winfo_children():
        widget.destroy()


fen = Tk()
fen.title("Laby")

tableau = []
activate = 0
level()

canvas = Canvas(fen, width=r_conv(len(tableau[0])), height=r_conv(len(tableau)), background='#C7DCF1')  # création de la zone de dessin
canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre

for i in range(len(tableau)):
    canvas.create_line(0, 20*(i+1), r_conv(len(tableau[0])), 20*(i+1), fill='#C7DCF1')  # création des lignes horizontales

for j in range(len(tableau[0])):
    canvas.create_line(20*(j+1), 0, 20*(j+1), r_conv(len(tableau)), fill='#C7DCF1')  # création des lignes verticales

perso = canvas.create_oval(181, 261, 199, 279, fill='yellow')  # création du personnage #

wall(tableau)

fen.bind("<z>", lambda event: deplace('h', 0, -20))
fen.bind("<s>", lambda event: deplace('b', 0, 20))
fen.bind("<q>", lambda event: deplace('g', -20, 0))
fen.bind("<d>", lambda event: deplace('d', 20, 0))
fen.bind("<a>", lambda event: print(canvas.coords(perso)))

fen.mainloop()
