class Piece:
    """
        Classe Piece
        Possède toutes les fonctionnalités d'une pièce d'un jeu de dame(ses mouvements, sa couleur, son statut)
    """

    def __init__(self, color, position, isQueen=False):
        self.isQueen = isQueen
        self.color = color
        self.position = position

    def promote(self):
        """
        Transforme un pion en dame
        """
        self.isQueen = True




