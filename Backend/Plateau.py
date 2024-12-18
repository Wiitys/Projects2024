class Plateau:
    """
    Classe Plateau
    Possède toutes les fonctionnalités du plateau de jeu pour instancier et jouer les pièces sur le plateau
    """
    #region CONSTRUCTEUR
    def __init__( self ):
        self.grille = []
        self.tourCourant = "W"  """ Définir le joueur actuel ( "W" pour blanc, "B" pour noir )"""
    #endregion
    
    #region METHODES
    def InitialiserPlateau( self ):
        """Fonction permettant d'initialiser le plateau de jeu avec les pions."""
        self.grille = [
            [
                "W" if ( v_ligne + v_colonne ) % 2 == 0 and v_ligne < 5 else
                "B" if ( v_ligne + v_colonne ) % 2 == 0 and v_ligne > 5 else
                0
                for v_colonne in range( 10 )
            ]
            for v_ligne in range( 10 )
        ]
        for v_ligne in range( 4, 6 ):
            self.grille[v_ligne] = [0 for v_colonne in range( 10 )]

    def ObtenirPositionIntermediaire( self, p_start, p_end ):
        """_summary_
               Renvoie la position intermédiaire entre le départ et l'arrivée si le mouvement est de deux cases
    
        Args:
            p_start ( _type_ ): position de départ du pion ( tab )
            p_end ( _type_ ): position d'arrivée du pion ( tab )

        Returns:
            _type_: int,int
        """        

        midRow = ( p_start[0] + p_end[0] ) // 2
        midCol = ( p_start[1] + p_end[1] ) // 2
        return midRow, midCol

    def GestionnaireDeMouvementPiece( self, p_start, p_end, p_piece ):
        """_summary_
            Gère le déplacement en appelant la bonne méthode en fonction du type de pièce.  
        Args:
            p_start ( _type_ ): position de depart du pion ( tab )
            p_end ( _type_ ): position d'arrivée du pion ( tab )
            p_piece ( _type_ ): piece qui souhaite bouger ( Piece )

        Returns:
            _type_: Bool, Piece, p_piece, int, int
        """        
        if p_piece.isQueen:
            return self.DeplacerReine( p_start, p_end, p_piece )
        else:
            return self.DeplacerPion( p_start, p_end, p_piece )

    def VerifieSiMouvementPionValide( self, p_start, p_end, p_piece ):
        """_summary_
            Vérifie si un mouvement est valide pour un pion de base.
        Args:
            p_start ( _type_ ): position de départ du pion
            p_end ( _type_ ): position d'arrivée du pion
            p_piece ( _type_ ): Piece

        Returns:
            _type_: Boolean
        """
        if ( p_piece.color != self.tourCourant ):
            return False
        if self.grille[p_end[0]][p_end[1]] != 0 or self.grille[p_start[0]][p_start[1]] not in ( "W", "B" ):
            return False

        rowDiff = p_end[0] - p_start[0]
        colDiff = abs( p_end[1] - p_start[1] )

        """ Mouvement simple pour un pion """
        if abs( rowDiff ) == 1 and colDiff == 1:
            if p_piece.color == "W" and rowDiff <= 0:
                return False
            if p_piece.color == "B" and rowDiff >= 0:
                return False
            return True

        """ Capture pour un pion """
        if abs( rowDiff ) == 2 and colDiff == 2:
            intermediate = self.ObtenirPositionIntermediaire( p_start, p_end )
            if self.grille[intermediate[0]][intermediate[1]] in ( "W", "B", "WQ", "BQ" ) and self.grille[intermediate[0]][intermediate[1]] != p_piece.color:
                return True

        return False

    def VerifieSiMouvementReineValide( self, p_start, p_end, p_piece ):
        """_summary_
            Vérifie si un mouvement est valide pour une dame.
        Args:
            p_start ( _type_ ): position depart pion
            p_end ( _type_ ): positon arrive pion
            p_piece ( _type_ ): piece

        Returns:
            _type_: boolean
        """
        if ( p_piece.color != self.tourCourant + "Q" ):
            return False
        if self.grille[p_end[0]][p_end[1]] != 0:
            return False

        v_rowDiff = p_end[0] - p_start[0]
        v_colDiff = abs( p_end[1] - p_start[1] )

        """ Mouvement simple pour une reine"""
        if abs( v_rowDiff ) == abs( v_colDiff ):
            v_stepRow = 1 if v_rowDiff > 0 else -1
            v_stepCol = 1 if p_end[1] > p_start[1] else -1

            currentRow, currentCol = p_start[0] + v_stepRow, p_start[1] + v_stepCol
            foundPiece = False

            """ Capture"""
            while currentRow != p_end[0] and currentCol != p_end[1]:
                if self.grille[currentRow][currentCol] in ( "W", "B", "WQ", "BQ" ):
                    """ Une pièce a déjà été rencontrée"""
                    if foundPiece: 
                        return False
                    foundPiece = True  
                currentRow += v_stepRow
                currentCol += v_stepCol

            return True

        return False
    
    def PromotionReine( self,p_end,p_piece ) :
        """_summary_
             Si un pion atteint la dernière ligne il est promu
        Args:
            p_end ( _type_ ): position d'arrivée
            p_piece ( _type_ ): piece

        Returns:
            _type_:piece
        """        

        if p_end[0] == 9 and p_piece.color == "W":
            p_piece.Promote()
            self.grille[p_end[0]][p_end[1]] = "WQ"
            p_piece.color = "WQ"
            
        if p_end[0] == 0 and p_piece.color == "B":
            p_piece.Promote()
            self.grille[p_end[0]][p_end[1]] = "BQ"
            p_piece.color = "BQ"

        return p_piece

    def DeplacerPion( self, p_start, p_end, p_piece ):
        """_summary_
            Déplace un pion de base.
        Args:
            p_start ( _type_ ): coord de depart pion
            p_end ( _type_ ): coord d'arrivée pion
            p_piece ( _type_ ): piece

        Returns:
            _type_: Bool, Piece, Piece, int, int
        """        

        if not self.VerifieSiMouvementPionValide( p_start, p_end, p_piece ):
            return False, False, p_piece, -1, -1

        p_piece.color = self.grille[p_start[0]][p_start[1]]
        v_pieceCapture = False
        v_pieceCaptureX, v_pieceCaptureY = -1, -1

        """ Si deplacement de 2 cases : On va chercher le pion intermédiaire """
        if abs( p_start[0] - p_end[0] ) == 2:
            intermediate = self.ObtenirPositionIntermediaire( p_start, p_end )
            if self.grille[intermediate[0]][intermediate[1]] in ( "W", "B" , "WQ", "BQ"):
                self.grille[intermediate[0]][intermediate[1]] = 0
                v_pieceCapture = True
                v_pieceCaptureX, v_pieceCaptureY = intermediate

        """ On place le pion à ses nouvelles coordonées sur la grille ( plateau ) """
        self.grille[p_start[0]][p_start[1]] = 0
        self.grille[p_end[0]][p_end[1]] = p_piece.color
        p_piece.x, p_piece.y = p_end[0], p_end[1]

        p_piece = self.PromotionReine( p_end,p_piece )

        return True, v_pieceCapture, p_piece, v_pieceCaptureX, v_pieceCaptureY

    def DeplacerReine( self, p_start, p_end, p_piece ):
        """_summary_
            Déplace une dame.
        Args:
            p_start ( _type_ ): position depart
            p_end ( _type_ ): position d'arrivée
            p_piece ( _type_ ): piece

        Returns:
            _type_: Bool, piece,piece, int, int
        """        
        """ Si invalide on annule """
        if not self.VerifieSiMouvementReineValide( p_start, p_end, p_piece ):
            return False, False, p_piece, -1, -1

        p_piece.color = self.grille[p_start[0]][p_start[1]]
        v_pieceCapture = False
        v_pieceCaptureX, v_pieceCaptureY = -1, -1

        v_stepRow = 1 if p_end[0] > p_start[0] else -1
        v_stepCol = 1 if p_end[1] > p_start[1] else -1
        currentRow, currentCol = p_start[0] + v_stepRow, p_start[1] + v_stepCol

        """ La reine peut se déplacer tout en diagonale """
        while currentRow != p_end[0] and currentCol != p_end[1]:
            if self.grille[currentRow][currentCol] in ( "W", "B", "WQ", "BQ" ):
                self.grille[currentRow][currentCol] = 0
                v_pieceCapture = True
                v_pieceCaptureX, v_pieceCaptureY = currentRow, currentCol
                break
            currentRow += v_stepRow
            currentCol += v_stepCol
        
        """ On ajoute la reine à à sa nouvelle place sur la grille """
        self.grille[p_start[0]][p_start[1]] = 0
        self.grille[p_end[0]][p_end[1]] = p_piece.color
        p_piece.x,p_piece.y = p_end[0], p_end[1]

        return True, v_pieceCapture, p_piece, v_pieceCaptureX, v_pieceCaptureY