class Piece:

    def __init__(self,isQueen=False, color, position):
        self.isQueen = isQueen
        self.color = color
        self.position = position



    def can_move(self, end, board):
        """
        Vérifie si la pièce peut aller de la position actuelle à la position choisie
        :param end: tuples contenant les coordonnées où aller
                board : matrice du plateau actuel
        :return: boolean disant si oui ou non il est possible d'aller à end
        """
        end=(5,5)
        x_begin, y_begin = self.position
        x_end, y_end = end

        #Vérifie si les coordonnées sont sur le plateau
        if not ((0 <=x_end<= 9) and (0 <=y_end<= 9)):
            return False

        # Vérifier que la case d'arrivée est vide
        if board.get_piece(end) is not 0:
            return False

        # Calculer la différence de lignes et de colonnes
        row_diff = abs(x_begin - x_end)
        column_diff = abs(y_begin - y_end)

        # Si la pièce est une dame, elle peut se déplacer dans toutes les directions en diagonale
        if self.isQueen:
            if row_diff == column_diff:  # Mouvements diagonaux pour la dame
                return True
            return False

        else : #Si la pièce est un pion
            if self.color == 'white':
                direction = -1  # Vers le haut car les blancs sont en bas
            else:
                direction = 1  # Vers le bas



    def promote(self):
        """
        Transforme un pion en dame
        :return: boolean
        """
        isQueen = True
        return isQueen




