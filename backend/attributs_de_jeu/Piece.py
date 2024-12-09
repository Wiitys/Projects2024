from xml.etree.ElementPath import xpath_tokenizer


class Piece:
    """
        Classe Piece
        Possède toutes les fonctionnalités d'une pièce d'un jeu de dame(ses mouvements, sa couleur, son statut)
    """

    def __init__(self, color, isQueen=False ,x=-1, y=-1):
        self.isQueen = isQueen
        self.color = color
        self.x = x
        self.y = y
        self.is_alive = True


    def promote(self):
        """
        Transforme un pion en dame
        """
        self.isQueen = True




