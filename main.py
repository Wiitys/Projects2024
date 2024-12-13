
import tkinter as tk
import customtkinter as ctk
import sys
import os


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
