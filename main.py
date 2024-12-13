
import tkinter as tk
import customtkinter as ctk
import sys
import os

# Ajouter le chemin du répertoire racine
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.Board import Board
from frontend.Interface import InterfaceJeuDeDames

# Initialisation du plateau avec des pions
board = Board()
board.initialize_board()


# Création de la fenêtre principale
fenetre = ctk.CTk()
app = InterfaceJeuDeDames(fenetre, board)

# Lancer l'application
fenetre.mainloop()
