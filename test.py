from tkinter import *

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

    def place(self):
        for i_ligne in range(len(self.tableau)):
            ligne = self.tableau[i_ligne]
            for i_colonne in range(len(ligne)):
                if ligne[i_colonne] == '1':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#000', outline='#000')
                if ligne[i_colonne] == '2':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='orange', outline=None)


class Pacman:
    """gestion du perso"""

    def __init__(self):
        self.pacman = canvas.create_oval(181, 181, 199, 199, fill='yellow')
        self.x = 0
        self.y = 0

    def deplace(self, direction):
        # Déplacement vers la droite
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if direction == 'r':
            if (self.x, self.y) == (18, 9):
                self.x, self.y = 0, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x + 1] != '1':
                    self.x += 1
        # Déplacement vers la gauche
        if direction == 'l':
            if (self.x, self.y) == (0, 9):
                self.x, self.y = 18, 9
            elif self.x > 0:
                if tab.tableau[self.y][self.x - 1] != '1':
                    self.x -= 1
        # Déplacement vers le haut
        if direction == 'u':
            if self.y > 0:
                if tab.tableau[self.y - 1][self.x] != '1':
                    self.y -= 1
        # Déplacement vers le bas
        if direction == 'd':
            if self.y < len(tab.tableau):
                if tab.tableau[self.y + 1][self.x] != '1':
                    self.y += 1
        canvas.coords(self.pacman, self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)

fen = Tk()

fen.title("Pacman")
tab = Tableau()
tab.open()

canvas = Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, background='#C7DCF1')

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()
joueur = Pacman()

fen.bind("<z>", lambda event: joueur.deplace('u'))#Joueurj.sendco('u')
fen.bind("<s>", lambda event: joueur.deplace('d'))#, Joueurj.sendco('d')
fen.bind("<q>", lambda event: joueur.deplace('l'))#, Joueurj.sendco('l')
fen.bind("<d>", lambda event: joueur.deplace('r'))#, Joueurj.sendco('r')
fen.bind("<a>", lambda event: print(canvas.coords(player.pacman)))

fen.mainloop()
