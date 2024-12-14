from xml.etree.ElementPath import xpath_tokenizer


class Piece:
    """
        Classe Piece
        Possède toutes les fonctionnalités d'une pièce d'un jeu de dame( ses mouvements, sa couleur, son statut )
    """
    #region CONSTRUCTEUR
    def __init__( self, color, isQueen=False ,p_x=-1, p_y=-1 ):
        self.isQueen = isQueen
        self.color = color
        self.x = p_x
        self.y = p_y
        self.isAlive = True
    #endregion

    #region METHODES
    def Promote( self ):
        """
        Transforme un pion en dame
        """
        self.isQueen = True

    def ObtenirCoordonnees( self ):
        """
        Fourni l'emplacement actuel du pion sur la grille
        """
        return [self.x,self.y]
    #endregion
    


