import tkinter as tk
import customtkinter as ctk
import sys
import os

from backend.Plateau import Plateau
from backend.Piece import Piece


# Configuration de base pour customtkinter
ctk.set_appearance_mode( "dark" )
ctk.set_default_color_theme( "blue" )


class InterfaceJeuDeDames:
    """ Classe qui gère l'interface de jeu et intéragit avec les éléments ( Plateau et Pièce )"""
  
    #region CONSTRUCTEUR
    def __init__( self, p_fenetre, p_plateau ):
        self.fenetre = p_fenetre
        self.Plateau = p_plateau
        self.fenetre.title( "Jeu de Dames" )
        self.fenetre.geometry( "650x750" )
        self.Plateau.tourCourant = 'W'
        self.pions ={}
        self.partieTerminee = False

        """ Titre principal"""
        self.titre = ctk.CTkLabel( p_fenetre, text="Jeu de Dames", font=("Helvetica", 30, "bold" ), text_color="#FFD700")
        self.titre.pack( pady=20 )

        self.GestionCanvas()
       
        """ Affichage du plateau de jeu avec des cases et des pions"""
        self.AfficherPlateau()

        """ Création du bouton "JOUER" """
        self.bouton_jouer = ctk.CTkButton(
            p_fenetre, text="JOUER", font=( "Helvetica", 20 ), width=200,
            height=50, corner_radius=20, fg_color="#FF5733",
            hover_color="#C70039", text_color="#FFFFFF", command=self.LancerJeu
        )
        self.bouton_jouer.pack( pady=40 )

        """Variables pour le Drag and Drop"""
        self.pionSelectionne = None
        self.positionInitiale = None

        """ Affichage du tour du joueur"""
        self.tour_label = ctk.CTkLabel( p_fenetre, text="Au tour de : Blanc", font=("Helvetica", 20 ), text_color="#FFD700")
        self.tour_label.pack( pady=20 )


        """Affichage du nombre de pions restants"""
        self.pionsRestantEtiquette = ctk.CTkLabel(
            p_fenetre, text="Pions restants - Blanc: 20 | Noir: 20",
            font=( "Helvetica", 18 ), text_color="#FFFFFF"
        )
        self.pionsRestantEtiquette.pack( pady=10 )
    #endregion
    
    #region METHODES
    def GestionCanvas( self ):
        """S'occupe de la configuration du canvas"""
        self.canvas_frame = ctk.CTkFrame( self.fenetre, width=600, height=600, corner_radius=15, fg_color="#333333" )
        self.canvas_frame.pack( pady=10 )

        """ Création du canvas pour une grille 10x10 ( 600x600 pixels )"""
        self.canvas = tk.Canvas( self.canvas_frame, width=600, height=600, bg="#444444", bd=0, highlightthickness=0 )
        self.canvas.pack( padx=10, pady=10 )

    def AfficherPlateau( self ):
        """Affiche le plateau de jeu en dessinant les cases pour une grille 10x10."""
        v_taille_case = 60 

        """Parcourt la grille et y créee les cases sur le canva"""
        for v_ligne in range( 10 ):
            for v_colonne in range( 10 ):
                x1, y1 = v_ligne * v_taille_case, v_colonne * v_taille_case
                x2, y2 = x1 + v_taille_case, y1 + v_taille_case
                couleur = "#FFFFFF" if ( v_ligne + v_colonne ) % 2 == 0 else "#333333"
                self.canvas.create_rectangle( x1, y1, x2, y2, fill=couleur, outline="" )

    def MajPionsRestants( self ):
        """
        Met à jour l'affichage du nombre de pions restants pour chaque joueur et vérifie si un joueur a gagné.
        """
        v_NombrePionsBlancs = sum( 1 for i in range(10 ) for j in range( 10 ) if self.Plateau.grille[i][j] == "W")
        v_NombrePionsNoirs = sum( 1 for i in range(10 ) for j in range( 10 ) if self.Plateau.grille[i][j] == "B")
        self.pionsRestantEtiquette.configure( text=f"Pions restants - Blanc: {v_NombrePionsBlancs} | Noir: {v_NombrePionsNoirs}" )

        # Vérification de la condition de victoire, seulement si la partie n'est pas terminée
        if not self.partieTerminee and ( v_NombrePionsBlancs == 0 or v_NombrePionsNoirs == 0 ):
            self.partieTerminee = True  # Marquer la partie comme terminée
            gagnant = "Noir" if v_NombrePionsNoirs > 0 else "Rouge"
            v_couleurPopUp = "#000000" if gagnant == "Noir" else "#FF0000"
            self.AfficherPopUpVictoire( gagnant, v_couleurPopUp )


    def AfficherPopUpVictoire( self, p_gagnant, p_couleurPopUp ):
        """_summary_
            Affiche un popup annonçant le gagnant et réinitialise le jeu à la fermeture.
        Args:
            p_gagnant ( _type_ ): pseudo du joueur gagnant
            p_couleurPopUp ( _type_ ): couleur du popUp qui sera affiché
        """       
        popup = tk.Toplevel( self.fenetre )
        popup.title( "Partie terminée" )
        popup.geometry( "300x150" )
        popup.configure( bg="#333333" )
        popup.transient( self.fenetre )
        popup.grab_set()

        label_message = tk.Label(
            popup,
            text=f"Le joueur {p_gagnant} a gagné !",
            font=( "Helvetica", 16, "bold" ),
            fg=p_couleurPopUp,
            bg="#333333"
        )
        label_message.pack( pady=30 )

        p_boutonValider = ctk.CTkButton(
            popup,
            text="OK",
            command=lambda: [popup.destroy(), self.ReinitialiserJeu()],
            font=( "Helvetica", 14 ),
            fg_color="#FF5733",
            hover_color="#C70039"
        )
        p_boutonValider.pack( pady=10 )

    def ReinitialiserJeu( self ):
        """Réinitialise le jeu à son état initial."""
        """ Réinitialise le plateau"""
        self.Plateau.InitialiserPlateau()

        """ Réinitialise les variables internes"""
        self.Plateau.tourCourant = 'W'
        self.partieTerminee = False

        """ Réinitialise l'affichage"""
        self.canvas.delete( "all" ) 
        self.AfficherPlateau()  
        self.AfficherPieces()
        self.MajPionsRestants()
        self.MajTour()
     self.bouton_jouer.pack( pady=40 )

    def ColoriserPion( self,p_color ):
        """_summary_
            Méthode qui colorise le pion en fonction de son role ( Blanc, noir et dorés pour reines )
        Args:
            p_color ( _type_ ): Couleur du pion

        Returns:
            _type_: string
        """
        if p_color == "B":
            p_color = "#000000"
        elif p_color == "W":
            p_color = "#FFFFFF"
        elif p_color == "BQ":
            p_color= "#393939"
        elif p_color == "WQ":
            p_color = "#e3e3e3"
        return p_color

    def ReafficherPieces( self ):
        """Réaffiche la nouvelle position des pions en fonction de leurs nouvelles coordonnées ( si elles ont changées )."""
        v_tailleCase = 60
        
        """On parcourt tous les pions de la grille et on change les pions sur le canva si nécessaire"""
        for pion in self.pions.items() :
        
            if pion[1].isAlive:
                couleur = self.ColoriserPion( pion[1].color )
                """ Coordonnées de l'ovale"""
                x1, y1 = pion[1].y * v_tailleCase + 10, pion[1].x * v_tailleCase + 10
                x2, y2 = ( pion[1].y + 1 ) * v_tailleCase - 10, ( pion[1].x + 1 ) * v_tailleCase - 10
                """ Bouger le pion avec ses nouvelles coordonnées"""
                self.canvas.coords( pion[0], x1, y1,x2, y2 )
                self.ChangementCouleur( pion )
            else :
                self.canvas.delete( pion[0] )

        self.MajPionsRestants()


    def ChangementCouleur( self, pion ):
        """_summary_
            Change la couleur quand une dame passe reine
        Args:
            pion ( _type_ ): pion à analyser
        """        
    
        """ On change la couleur du pion si c'est une reine"""
        if pion[1].color == "WQ":
            self.canvas.itemconfigure( pion[0], fill="#FFD700" )  
        elif pion[1].color == "BQ":
            self.canvas.itemconfigure( pion[0], fill="#B8860B" )  


    def AfficherPieces( self ):
        """Affiche les pions noirs et blancs selon les positions du Plateau pour une grille 10x10."""
        v_tailleCase = 60

        """Parcourt de toute la tableau"""
        for v_ligne in range( 10 ):
            for v_colonne in range( 10 ):
                piece = Piece( self.Plateau.grille[v_ligne][v_colonne],False,v_ligne,v_colonne )

                v_code_hexa_pion = self.ColoriserPion( self.Plateau.grille[v_ligne][v_colonne] )
                
                """On dessine les pions et les lies aux événements """
                if v_code_hexa_pion:
                    x1, y1 = v_colonne * v_tailleCase + 10, v_ligne * v_tailleCase + 10
                    x2, y2 = ( v_colonne + 1 ) * v_tailleCase - 10, ( v_ligne + 1 ) * v_tailleCase - 10
                    pionId = self.canvas.create_oval( x1, y1, x2, y2, fill=v_code_hexa_pion, outline="black", width="3" )
                    self.pions[pionId] = piece
                    self.canvas.tag_bind( pionId, "<ButtonPress-1>", self.startDrag )
                    self.canvas.tag_bind( pionId, "<B1-Motion>", self.Drag )
                    self.canvas.tag_bind( pionId, "<ButtonRelease-1>", self.Drop )

        """ Mettre à jour les pions restants après affichage initial"""
        self.MajPionsRestants()

    def startDrag( self, p_event ):
        """_summary_
            Démarre le Drag d'un pion.
        Args:
            p_event ( _type_ ):Evénement déclenché
        """        

        """ Enregistre l'ID du pion sélectionné et la position initiale"""
        self.pionSelectionne = p_event.widget.find_withtag( "current" )[0]
        self.positionInitiale = ( p_event.y // 60, p_event.x // 60 )


    def Drag( self, p_event ):
        """_summary_
            Déplace le pion sélectionné avec la souris
        Args:
            p_event ( _type_ ): événement déclenché
        """        

        if self.pionSelectionne :
            """ Calcule les nouvelles coordonnées du pion"""
            x, y = p_event.x, p_event.y
            self.canvas.coords( self.pionSelectionne, x - 25, y - 25, x + 25, y + 25 )

    def Drop( self, p_event ):
        """_summary_
            Lache le pion
        Args:
            p_event ( _type_ ): événement déclenché
        """     
        if self.pionSelectionne and self.positionInitiale:
            """ Position finale du pion"""
            v_positionFinale = ( p_event.y // 60, p_event.x // 60 )

            """ Appelle `move_piece` pour mettre à jour la logique du plateau"""
            v_mouvementValide, v_pieceMangee,piece, v_pieceMangeeX, v_pieceMangeeY = self.Plateau.GestionnaireDeMouvementPiece(
                self.positionInitiale, v_positionFinale, self.pions[self.pionSelectionne]
            )

            if v_pieceMangeeX != -1 and v_pieceMangeeY !=-1 :
                self.MajPionApresCapture( v_pieceMangeeX,v_pieceMangeeY )

            if v_mouvementValide:
                if v_pieceMangee:
                    print( f"Une pièce a été mangée en se déplaçant de {self.positionInitiale} à {v_positionFinale}" )

                """ Met à jour la position sur le canevas pour la position finale"""
                x1, y1 = v_positionFinale[1] * 60 + 10, v_positionFinale[0] * 60 + 10
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.coords( self.pionSelectionne, x1, y1, x2, y2 )

                """ Alterne le tour des joueurs si aucun mouvement supplémentaire n'est possible"""
                if not v_pieceMangee: 
                    self.Plateau.tourCourant = 'W' if self.Plateau.tourCourant == 'B' else 'B'

                """ Mettre à jour le tour du joueur"""
                self.ReafficherPieces()
                self.MajTour()

            else:
                if self.pions[self.pionSelectionne].color != self.Plateau.tourCourant or self.pions[self.pionSelectionne].color != self.Plateau.tourCourant + "Q":
                    print(
                        f"Déplacement invalide de {self.positionInitiale} à {v_positionFinale}, ce n'est pas votre tour")
                else:
                    print( f"Déplacement invalide de {self.positionInitiale} à {v_positionFinale}" )

                """ Retour à la position initiale si mouvement invalide """
                x1, y1 = self.positionInitiale[1] * 60 + 10, self.positionInitiale[0] * 60 + 10
                x2, y2 = x1 + 40, y1 + 40
                self.canvas.coords( self.pionSelectionne, x1, y1, x2, y2 )

            """ Réinitialise les variables"""
            self.pionSelectionne = None
            self.positionInitiale = None



    def MajPionApresCapture( self, v_pieceMangeeX, v_pieceMangeeY ):
        """_summary_
            Change l'attribut isAlive à false si le pion vient d'être mangé
        Args:
            v_pieceMangeeX ( _type_ ): coordonées X de la piece capturée
            v_pieceMangeeY ( _type_ ): coordonées Y de la piece capturée
        """        

        for pionId, pion in self.pions.items():
            if pion.x == v_pieceMangeeX and pion.y == v_pieceMangeeY:
                pion.isAlive = False
                print( f"Pion {pionId} a été mangé" )


    def MajTour( self ):
        """Met à jour le texte affichant le tour du joueur."""
        if self.Plateau.tourCourant == "B":
            self.tour_label.configure( text="Au tour de : Noir" )
        else:
            self.tour_label.configure( text="Au tour de : Blanc" )

    def LancerJeu( self ):
        """Action pour démarrer le jeu."""
        print( "Le jeu commence !" )
        self.AfficherPieces()
        self.bouton_jouer.pack_forget()


    #endregion
    