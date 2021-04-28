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
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#07007e')
                if ligne[i_colonne] == '0':
                    canvas.create_oval(i_colonne * 20 + 7, i_ligne * 20 + 7, i_colonne * 20 + 13, i_ligne * 20 + 13, fill='#fff')
                if ligne[i_colonne] == '2':
                    canvas.create_rectangle(i_colonne * 20, i_ligne * 20, i_colonne * 20 + 20, i_ligne * 20 + 20, fill='#000')

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
                    print(self.score)
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)

    def deplace_l(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if (self.x, self.y) == (18, 9):
            self.x, self.y = 0, 9
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y][self.x - 1] != '1':
                self.x -= 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    print(self.score)
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)

    def deplace_u(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if (self.x, self.y) == (18, 9):
            self.x, self.y = 0, 9
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y - 1][self.x] != '1':
                self.y -= 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    print(self.score)
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)

    def deplace_d(self):
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if (self.x, self.y) == (18, 9):
            self.x, self.y = 0, 9
        elif self.x < len(tab.tableau[0]):
            if tab.tableau[self.y + 1][self.x] != '1':
                self.y += 1
                bille = canvas.find_enclosed(self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)
                if len(bille) != 0:
                    canvas.delete(bille[0])
                    self.score += 1
                    print(self.score)
        canvas.coords(self.pacman, self.x * 20 +2, self.y * 20 + 2, self.x * 20 + 18, self.y * 20 + 18)

fen = Tk()

fen.title("Pacman")
tab = Tableau()
tab.open()

canvas = Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, background='#000')

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()
joueur = Pacman()

fen.bind("<z>", lambda event: joueur.deplace_u())#Joueurj.sendco('u')
fen.bind("<s>", lambda event: joueur.deplace_d())#, Joueurj.sendco('d')
fen.bind("<q>", lambda event: joueur.deplace_l())#, Joueurj.sendco('l')
fen.bind("<d>", lambda event: joueur.deplace_r())#, Joueurj.sendco('r')
fen.bind("<a>", lambda event: print(canvas.coords(player.pacman)))

fen.mainloop()
