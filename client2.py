# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).


import socket, sys, threading
from tkinter import *
from tkinter.messagebox import *


class Color:
    def __init__(self):
        self.AUCLIENT = 'green' #GREEN
        self.WARNING = '\033[93m' #YELLOW
        self.SERVEUR = '\033[91m' #RED
        self.RESET = '\033[0m' #RESET COLOR


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


class Perso:
    """gestion du perso"""

    def __init__(self, x, y):
        self.pacman = canvas.create_oval(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill='yellow')
        self.x = 0
        self.y = 0
        self.connexion = connexion

    def deplace(self, direction):
        # Déplacement vers la droite
        self.x = int(canvas.coords(self.pacman)[0] // 20)
        self.y = int(canvas.coords(self.pacman)[1] // 20)
        if direction == 'right':
            if (self.x, self.y) == (18, 9):
                self.x, self.y = 0, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.y][self.x + 1] != '1':
                    self.x += 1
                    message = "deplace:right"
                    self.connexion.send(message.encode("Utf8"))

        # Déplacement vers la gauche
        if direction == 'left':
            if (self.x, self.y) == (0, 9):
                self.x, self.y = 18, 9
            elif self.x > 0:
                if tab.tableau[self.y][self.x - 1] != '1':
                    self.x -= 1
                    message = "deplace:left"
                    self.connexion.send(message.encode("Utf8"))

        # Déplacement vers le haut
        if direction == 'up':
            if self.y > 0:
                if tab.tableau[self.y - 1][self.x] != '1':
                    self.y -= 1
                    message = "deplace:up"
                    self.connexion.send(message.encode("Utf8"))

        # Déplacement vers le bas
        if direction == 'down':
            if self.y < len(tab.tableau):
                if tab.tableau[self.y + 1][self.x] != '1':
                    self.y += 1
                    message = "deplace:down"
                    self.connexion.send(message.encode("Utf8"))

        canvas.coords(self.pacman, self.x * 20, self.y * 20, self.x * 20 + 20, self.y * 20 + 20)


class Fantome:
    """gestion du perso"""

    def __init__(self, x, y, z, z_bis):
        self.player = canvas.create_polygon(x * 20, y * 20, z * 20 - 10, z_bis * 20, (x + 1) * 20, y * 20, fill='blue')
        self.x = 0
        self.y = 0
        self.z = 0
        self.z_bis = 0
        self.connexion = connexion

    def deplace(self, direction):
        self.x = int(canvas.coords(self.player)[0] // 20)
        self.y = int(canvas.coords(self.player)[1] // 20)
        self.z = canvas.coords(self.player)[2] / 20
        self.z_bis = int(canvas.coords(self.player)[3] // 20)
        # Déplacement vers la droite
        if direction == 'right':
            print("test")
            if (self.x, self.y, self.z, self.z_bis) == (18, 10, 18.5, 9):
                self.x, self.y, self.z, self.z_bis = 0, 10, 0.5, 9
            elif self.x < len(tab.tableau[0]):
                if tab.tableau[self.z_bis][self.x + 1] != '1':
                    self.x += 1
                    self.z += 1
        # Déplacement vers la gauche
        if direction == 'left':
            if (self.x, self.y, self.z, self.z_bis) == (0, 10, 0.5, 9):
                self.x, self.y, self.z, self.z_bis = 18, 10, 18.5, 9
            elif self.x > 0:
                if tab.tableau[self.z_bis][self.x - 1] != '1':
                    self.x -= 1
                    self.z -= 1
        # Déplacement vers le haut
        if direction == 'up':
            if self.y > 0:
                if tab.tableau[self.z_bis - 1][self.x] != '1':
                    self.y -= 1
                    self.z_bis -= 1
        # Déplacement vers le bas
        if direction == 'down':
            if self.y < len(tab.tableau):
                if tab.tableau[self.z_bis + 1][self.x] != '1':
                    self.y += 1
                    self.z_bis += 1
        canvas.coords(self.player, self.x * 20, self.y * 20, self.z * 20, self.z_bis * 20, self.x * 20 + 20, self.y * 20)


class ThreadReception(threading.Thread):
    """objet thread gérant la réception des messages"""

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn     # réf. du socket de connexion
        self.message_recu = 0
        self.demande = 0
        self.coo = []

    def player_move(self, joueur, sens):
        '''permet de faire bouger les joueurs'''
        if self.coo[1] == sens:
            joueur.deplace(sens)
            print(sens)

    def run(self):
        global player, player2, player3, player4
        while 1:
            self.message_recu = self.connexion.recv(1024).decode("Utf8")
            self.demande = self.message_recu.split()
            print(self.demande)
            self.coo = self.demande[1].split(':')  

            if self.demande[0] == "def" and self.demande[1] == "Thread-1":
                player = Perso(9, 7)
                player2 = Fantome(1, 2, 2, 1)
                player3 = Fantome(1, 18, 2, 17)
                player4 = Fantome(17, 18, 18, 17)

            elif self.demande[0] == "def" and self.demande[1] == "Thread-2":
                player = Fantome(1, 2, 2, 1)
                player2 = Perso(9, 7)
                player3 = Fantome(1, 18, 2, 17)
                player4 = Fantome(17, 18, 18, 17)

            elif self.demande[0] == "def" and self.demande[1] == "Thread-3":
                player = Fantome(1, 2, 2, 1)
                player2 = Fantome(1, 18, 2, 17)
                player3 = Perso(9, 7)
                player4 = Fantome(17, 18, 18, 17)

            elif self.demande[0] == 'def':
                player = Fantome(1, 2, 2, 1)
                player2 = Fantome(1, 18, 2, 17)
                player3 = Fantome(17, 18, 18, 17)
                player4 = Perso(9, 7)

            elif self.demande[0] == "Thread-1>":
                if self.coo[0] == "deplace":
                    print('fantome deplacement 2 {self.coo[1]}'.format())
                    self.player_move(player, 'right')
                    self.player_move(player, 'left')
                    self.player_move(player, 'up')
                    self.player_move(player, 'down')

            elif self.demande[0] == "Thread-2>":
                if self.coo[0] == "deplace":
                    print('fantome deplacement 2 {self.coo[1]}'.format())
                    self.player_move(player2, 'right')
                    self.player_move(player2, 'left')
                    self.player_move(player2, 'up')
                    self.player_move(player2, 'down')

            elif self.demande[0] == "Thread-3>":
                if self.coo[0] == "deplace":
                    print('fantome deplacement 2 {self.coo[1]}'.format())
                    self.player_move(player3, 'right')
                    self.player_move(player3, 'left')
                    self.player_move(player3, 'up')
                    self.player_move(player3, 'down')

            elif self.demande[0] == "Thread-4>":
                if self.coo[0] == "deplace":
                    print('fantome deplacement 2 {self.coo[1]}'.format())
                    self.player_move(player4, 'right')
                    self.player_move(player4, 'left')
                    self.player_move(player4, 'up')
                    self.player_move(player4, 'down')

                print("\n\ncreation d'un personnage ... \n\n")
                #creation = "create"
                #connexion.send(creation.encode())

            #if demande[1] == "lance":
                # lancement()
                #print("lancement en cours ...")


            print("{bcolors.AUCLIENT}* {message_recu} *{bcolors.RESET}".format())
            if not self.message_recu or self.message_recu.upper() == "FIN":
                break

        # Le thread <réception> se termine ici.
        # On force la fermeture du thread <émission> :
        th_E._stop()
        print("Client arrêté. Connexion interrompue.")
        self.connexion.close()

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn	     # réf. du socket de connexion
        self.message_emis = 0

    def run(self):
        while 1:
            self.message_emis = input()
            self.connexion.send(self.message_emis.encode("Utf8"))


def conv(x):
    x *= 20
    return x

host = '192.168.1.16'
port = 40000

bcolors = Color()

fen = Tk()

fen.title("Pacman")
tab = Tableau()
tab.open()

canvas = Canvas(fen, width=len(tab.tableau[0]) * 20, height=len(tab.tableau) * 20, background='#C7DCF1')

canvas.grid(row=1, column=1, columnspan=3)  # méthode qui permet de placer la zone de dessin dans la fenêtre
tab.place()

# Programme principal - Établissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("\n\nConnexion établie avec le serveur.\n\n")

# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()


fen.bind("<z>", lambda event: player.deplace('up'))
fen.bind("<s>", lambda event: player.deplace('down'))
fen.bind("<q>", lambda event: player.deplace('left'))
fen.bind("<d>", lambda event: player.deplace('right'))
fen.bind("<a>", lambda event: print(canvas.coords(player.pacman)))

fen.mainloop()