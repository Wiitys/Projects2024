import tkinter as tk
import customtkinter as ctk
from Projects2024.backend.attributs_de_jeu.Board import Board

# Configuration de base pour customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class InterfaceJeuDeDames:
    def __init__(self, fenetre, board):
        self.fenetre = fenetre
        self.board = board
        self.fenetre.title("Jeu de Dames")
        self.fenetre.geometry("650x750")
        self.board.current_turn = 'W'

        # Titre principal
        self.titre = ctk.CTkLabel(fenetre, text="Jeu de Dames", font=("Helvetica", 30, "bold"), text_color="#FFD700")
        self.titre.pack(pady=20)

        # Configuration du canvas pour le plateau 10x10
        self.canvas_frame = ctk.CTkFrame(self.fenetre, width=600, height=600, corner_radius=15, fg_color="#333333")
        self.canvas_frame.pack(pady=10)

        # Création du canvas pour une grille 10x10 (600x600 pixels)
        self.canvas = tk.Canvas(self.canvas_frame, width=600, height=600, bg="#444444", bd=0, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        # Affichage du plateau de jeu avec des cases et des pions
        self.afficher_plateau()

        # Création du bouton "JOUER"
        self.bouton_jouer = ctk.CTkButton(
            fenetre, text="JOUER", font=("Helvetica", 20), width=200,
            height=50, corner_radius=20, fg_color="#FF5733",
            hover_color="#C70039", text_color="#FFFFFF", command=self.lancer_jeu
        )
        self.bouton_jouer.pack(pady=40)

        # Variables pour le drag and drop
        self.pion_selectionne = None
        self.position_initiale = None

        # Affichage du tour du joueur
        self.tour_label = ctk.CTkLabel(fenetre, text="Au tour de : Blanc", font=("Helvetica", 20), text_color="#FFD700")
        self.tour_label.pack(pady=20)

    def afficher_plateau(self):
        """Affiche le plateau de jeu en dessinant les cases pour une grille 10x10."""
        taille_case = 60
        for i in range(10):
            for j in range(10):
                x1, y1 = i * taille_case, j * taille_case
                x2, y2 = x1 + taille_case, y1 + taille_case
                couleur = "#FFFFFF" if (i + j) % 2 == 0 else "#333333"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")

    def afficher_pieces(self):
        """Affiche les pions noirs et blancs selon les positions du board pour une grille 10x10."""
        taille_case = 60
        rayon_pion = taille_case // 2 - 10

        for i in range(10):
            for j in range(10):
                couleur_pion = None
                if self.board.grid[i][j] == "B":
                    couleur_pion = "#000000"
                elif self.board.grid[i][j] == "W":
                    couleur_pion = "#FF0000"

                if couleur_pion:
                    x1, y1 = j * taille_case + 10, i * taille_case + 10
                    x2, y2 = (j + 1) * taille_case - 10, (i + 1) * taille_case - 10
                    pion_id = self.canvas.create_oval(x1, y1, x2, y2, fill=couleur_pion, outline="")
                    self.canvas.tag_bind(pion_id, "<ButtonPress-1>", self.start_drag)
                    self.canvas.tag_bind(pion_id, "<B1-Motion>", self.drag)
                    self.canvas.tag_bind(pion_id, "<ButtonRelease-1>", self.drop)

    def start_drag(self, event):
        """Démarre le drag d'un pion."""
        # Enregistre l'ID du pion sélectionné et la position initiale
        self.pion_selectionne = event.widget.find_withtag("current")[0]
        self.position_initiale = (event.y // 60, event.x // 60)

    def drag(self, event):
        """Déplace le pion sélectionné avec la souris."""
        if self.pion_selectionne:
            # Calcule les nouvelles coordonnées du pion
            x, y = event.x, event.y
            self.canvas.coords(self.pion_selectionne, x - 25, y - 25, x + 25, y + 25)

    def drop(self, event):
        """Dépose le pion et tente de le déplacer sur le plateau."""
        if self.pion_selectionne and self.position_initiale:
            # Position finale du pion
            position_finale = (event.y // 60, event.x // 60)

            # Appelle `move_piece` pour mettre à jour la logique du plateau
            if self.board.move_piece(self.position_initiale, position_finale):
                print(f"Pion déplacé de {self.position_initiale} à {position_finale}")
                # Met à jour la position sur le canevas pour la position finale
                x1, y1 = position_finale[1] * 60 + 10, position_finale[0] * 60 + 10
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.coords(self.pion_selectionne, x1, y1, x2, y2)

                if self.board.current_turn == 'B':
                    self.board.current_turn = 'W'
                else :
                    self.board.current_turn = 'B'

                # Mettre à jour le tour du joueur
                self.mettre_a_jour_tour()

            else:
                print(f"Déplacement invalide de {self.position_initiale} à {position_finale}")
                # Retour à la position initiale si mouvement invalide
                x1, y1 = self.position_initiale[1] * 60 + 10, self.position_initiale[0] * 60 + 10
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.coords(self.pion_selectionne, x1, y1, x2, y2)

            # Réinitialise les variables
            self.pion_selectionne = None
            self.position_initiale = None

    def mettre_a_jour_tour(self):
        """Met à jour le texte affichant le tour du joueur."""
        if self.board.current_turn == "B":
            self.tour_label.configure(text="Au tour de : Noir")
        else:
            self.tour_label.configure(text="Au tour de : Blanc")

    def lancer_jeu(self):
        """Action pour démarrer le jeu."""
        print("Le jeu commence !")
        self.afficher_pieces()
        self.bouton_jouer.pack_forget()


# Initialisation du plateau avec des pions
board = Board()
board.initialize_board()

# Création de la fenêtre principale
fenetre = ctk.CTk()
app = InterfaceJeuDeDames(fenetre, board)
# Lancer l'application
fenetre.mainloop()
