import tkinter as tk
import customtkinter as ctk

# Configuration de base pour customtkinter (optionnel)
ctk.set_appearance_mode("dark")  # Choix de thème "dark" ou "light"
ctk.set_default_color_theme("blue")  # Thème de couleur pour les widgets

class InterfaceJeuDeDames:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Jeu de Dames")
        self.fenetre.geometry("600x700")  # Taille plus grande pour l'espacement

        # Titre principal
        self.titre = ctk.CTkLabel(fenetre, text="Jeu de Dames", font=("Helvetica", 30, "bold"), text_color="#FFD700")
        self.titre.pack(pady=20)  # Espace autour du titre

        # Configuration du canvas (plateau de jeu)
        self.canvas_frame = ctk.CTkFrame(self.fenetre, width=480, height=480, corner_radius=15, fg_color="#333333")
        self.canvas_frame.pack(pady=10)

        # Création du canvas pour le plateau avec un fond stylisé
        self.canvas = tk.Canvas(self.canvas_frame, width=480, height=480, bg="#444444", bd=0, highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        # Affichage du plateau de jeu avec des cases
        self.afficher_plateau()

        # Création du bouton "JOUER" avec un style moderne et des effets
        self.bouton_jouer = ctk.CTkButton(
            fenetre, text="JOUER", font=("Helvetica", 20), width=200,
            height=50, corner_radius=20, fg_color="#FF5733",
            hover_color="#C70039", text_color="#FFFFFF", command=self.lancer_jeu
        )
        self.bouton_jouer.pack(pady=40)

        # Variable de sélection de pion
        self.selection = None

    def afficher_plateau(self):
        """Affiche le plateau de jeu en dessinant les cases de couleur alternée."""
        taille_case = 60
        for i in range(8):
            for j in range(8):
                x1, y1 = i * taille_case, j * taille_case
                x2, y2 = x1 + taille_case, y1 + taille_case
                couleur = "#FFFFFF" if (i + j) % 2 == 0 else "#333333"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="")

    def lancer_jeu(self):
        """Action pour démarrer le jeu et afficher un message de test."""
        print("Le jeu commence !")  # Cette commande pourrait lancer la logique de jeu


# Création de la fenêtre principale
fenetre = ctk.CTk()
app = InterfaceJeuDeDames(fenetre)

# Lancer l'application
fenetre.mainloop()
