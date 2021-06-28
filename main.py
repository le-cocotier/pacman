# Changement des déplacement:fonction deplace(self, direction) changer en: -deplace_d
#                                                                         -deplace_l
#                                                                         -deplace_u
#                                                                         -deplace_r
# mise en place des pièce comtabilisée dans la variable self.score de Pacman
# mise en place du compteur de point
# mise en place de la condition de victiore et de la fenetre de victoire

import tkinter
from tkinter import messagebox
from tkinter.constants import FALSE
from typing import FrozenSet

class Tableau:
    """gestion du level"""

    def __init__(self):
        self.level = 'level.txt'
        self.tableau = []

    def open(self):
        """ouverte d'un fichier"""

        file = open(self.level, "r")
        read = file.read()
        self.tableau = list(read.split("\n"))
        self.tableau.remove(self.tableau[-1])
        print(self.tableau)

    def place(self):
        for i_ligne in range(len(self.tableau)):
            ligne = self.tableau[i_ligne]
            for i_colonne in range(len(ligne)):
                if ligne[i_colonne] == '1':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#07007e')
                if ligne[i_colonne] == '0':
                    canvas.create_oval(i_colonne * 20 + 7, i_ligne * 20 + 7, i_colonne * 20 + 13, i_ligne * 20 + 13, fill='#fff')
                if ligne[i_colonne] == '3':
                    canvas.create_oval(i_colonne * 20 + 5, i_ligne * 20 + 5, i_colonne * 20 + 15, i_ligne * 20 + 15, fill='#07007e')

    def mod(self, y, x, chiffre):
        modification = self.tableau[y][:x] + chiffre + self.tableau[y][x+1:]
        self.tableau = self.tableau[:y] + [modification] + self.tableau[y+1:]


class Pacman:
    """gestion du perso"""

    def __init__(self):
        self.pacman = canvas.create_oval(182, 182, 198, 198, fill='yellow')
        self.x = 0
        self.y = 0
        self.score = 0
        self.compteur = tkinter.Label(text='Score = 0', bg='black', fg='white')
        self.compteur.grid(row=0, column=1, columnspan=3)

    def win(self):
        if self.score == 176:
            messagebox.showinfo("Pacman", "Vous avez gagné!")
            fen.destroy()

    def deplace_r(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if (self.x, self.y) == (18, 9):
            self.x, self.y = 0, 9
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y][self.x + 1] != '1':
                self.x += 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    self.compteur.configure(text='score = ' + str(self.score))
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
        self.win()

    def deplace_l(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if (self.x, self.y) == (0, 9):
            self.x, self.y = 18, 9
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y][self.x - 1] != '1':
                self.x -= 1
                bille = canvas.find_enclosed(self.x * 20 + 4, self.y * 20 + 4, self.x * 20 + 16, self.y * 20 + 16)
                if len(bille) != 0:
                    bille = canvas.find_enclosed(self.x * 20 + 6, self.y * 20 + 6, self.x * 20 + 14, self.y * 20 + 14)
                    if len(bille) != 0:
                        canvas.delete(bille[0])
                        self.score += 1
                        self.compteur.configure(text='score = ' + str(self.score))
                    len
            canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
        self.win()

    def deplace_u(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if self.x < len(tab.tableau[0]):
            if tab.tableau[self.y - 1][self.x] != '1':
                self.y -= 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    self.compteur.configure(text='score = ' + str(self.score))
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
        self.win()

    def deplace_d(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if self.x < len(tab.tableau[0]):
            if tab.tableau[self.y + 1][self.x] != '1':
                self.y += 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    self.compteur.configure(text='score = ' + str(self.score))
                can_eat = True
                print(can_eat)
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)
        self.win()


class Ghost:
    """gestion du perso"""

    def __init__(self, x, y, color):
        self.ghost = canvas.create_polygon(x, y, x + 10, y -20, x + 20, y, fill=color)
        self.x = x
        self.y = y

    def deplace_r(self):
        self.x = int(canvas.coords(self.ghost)[0] // 20)
        self.y = int(canvas.coords(self.ghost)[1] // 20)
        if (self.x, self.y) == (18, 10):
            self.x, self.y = 0, 10
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y - 1][self.x + 1] != '1':
                self.x += 1
        canvas.coords(self.ghost, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_l(self):
        self.x = int(canvas.coords(self.ghost)[0] // 20)
        self.y = int(canvas.coords(self.ghost)[1] // 20)
        if (self.x, self.y) == (0, 10):
            self.x, self.y = 18, 10
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y - 1][self.x - 1] != '1':
                self.x -= 1
        canvas.coords(self.ghost, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_u(self):
        self.x = int(canvas.coords(self.ghost)[0] // 20)
        self.y = int(canvas.coords(self.ghost)[1] // 20)
        if self.x < len(tab.tableau[0]):
            if tab.tableau[self.y - 2][self.x] != '1':
                self.y -= 1
        canvas.coords(self.ghost, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)

    def deplace_d(self):
        self.x = int(canvas.coords(self.ghost)[0] // 20)
        self.y = int(canvas.coords(self.ghost)[1] // 20)
        if self.x < len(tab.tableau[0]):
            if tab.tableau[self.y][self.x] != '1':
                self.y += 1
        canvas.coords(self.ghost, self.x * 20, self.y * 20, self.x * 20 + 10, self.y * 20 - 20, self.x * 20 + 20, self.y * 20)


fen = tkinter.Tk()

fen.title("Pacman")
fen.configure(bg='black')
tab = Tableau()
tab.open()

canvas = tkinter.Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, bg='#000')
can_eat = False

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()

joueur = Pacman()

fen.bind("<z>", lambda event: joueur.deplace_u())#Joueurj.sendco('u')
fen.bind("<s>", lambda event: joueur.deplace_d())#, Joueurj.sendco('d')
fen.bind("<q>", lambda event: joueur.deplace_l())#, Joueurj.sendco('l')
fen.bind("<d>", lambda event: joueur.deplace_r())#, Joueurj.sendco('r')
fen.bind("<a>", lambda event: print(canvas.coords(player.pacman)))

fen.mainloop()
