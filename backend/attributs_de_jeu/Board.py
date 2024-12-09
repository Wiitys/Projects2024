class Board:
    """
    Classe Board
    Possède toutes les fonctionnalités du plateau de jeu pour instancier et jouer les pièces sur le plateau
    """

    def __init__(self):
        # Initialisation de la grille
        self.grid = []

    def initialize_board(self):
        """
        Fonction permettant d'initialiser le plateau de jeu avec les pions.
        """
        # Initialisation de la grille avec "W" pour blanc, "B" pour noir et 0 pour vide
        self.grid = [["W" if (i + j) % 2 == 0 and i < 5 else "B" if (i + j) % 2 == 0 and i > 5 else 0 for j in range(10)] for i in range(10)]

        # Modification des deux lignes du milieu pour les remplir de 0 car il n'y a pas de pions ici
        for i in range(4, 6):
            self.grid[i] = [0 for j in range(10)]

    def get_intermediate_position(self, start, end):
        """
        Renvoie la position intermédiaire entre le départ et l'arrivée si le mouvement est de deux cases
        """
        mid_row = (start[0] + end[0]) // 2
        mid_col = (start[1] + end[1]) // 2
        return mid_row, mid_col

    def move_piece(self, start, end, piece):
        """
        Vérifie si la pièce est déplaçable et la déplace si possible. Mange une pièce si elle est sur le chemin.
        :param color_piece: couleur de la pièce deplacée
        :param start: position de base de la pièce
        :param end: position future de la pièce
        :return: Boolean, Boolean -> si la pièce est déplaçable ou non et si une capture a eu lieu
        """
        piece_captured = False  # Variable pour suivre si une pièce a été mangée
        piece_mange_x= -1
        piece_mange_y = -1
        if self.is_valid_move(start, end, piece):
            piece.color = self.grid[start[0]][start[1]]  # Stocke le type de pièce ("W" ou "B")

            # Vérifie s'il y a une pièce intermédiaire pour un mouvement de saut
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 2:
                intermediate = self.get_intermediate_position(start, end)
                piece_mange_x = intermediate[0]
                piece_mange_y = intermediate[1]
                print("case inter", intermediate)


                # Si une pièce ennemie se trouve à la position intermédiaire, elle est mangée
                if self.grid[intermediate[0]][intermediate[1]] in ("W", "B"):
                    self.grid[intermediate[0]][intermediate[1]] = 0  # Retire la pièce mangée
                    piece_captured = True  # Indique qu'une pièce a été capturée



            # Effectue le mouvement
            self.grid[start[0]][start[1]] = 0  # Vide la position de départ
            self.grid[end[0]][end[1]] = piece.color  # Place la pièce dans la position d'arrivée
            piece.x = end[0]
            piece.y = end[1]
            print('nouvelles coordonées =', piece.x, piece.y)

            if end[0] == 9:
                piece.isQueen = True
                # Le pion blanc devient WQ (WHITE QUEEN)
                if self.grid[end[0]][end[1]] == "W":
                    self.grid[end[0]][end[1]] = 'WQ'
                    piece.color = "WQ"

            # Si la ligne sur laquelle je veux aller est la 10 eme (0eme pour les noirs)  alors je vais devenir une reine
            if end[0] == 0:
                piece.isQueen = True
                # Le pion noir devient Black queen
                if self.grid[end[0]][end[1]] == 'B':
                    self.grid[end[0]][end[1]] = 'BQ'
                    piece.color = "BQ"


            return True, piece_captured, piece, piece_mange_x, piece_mange_y # Retourne si le mouvement est valide et si une capture a eu lieu
        return False, False,piece,piece_mange_x, piece_mange_y  # Mouvement invalide, aucune capture




    def is_valid_move(self, start, end, piece):
        """
        Vérifie si un mouvement est valide. Un mouvement de deux cases est valide si une pièce peut être mangée.
        """
        # Vérifie que la case de départ contient une pièce ("W" ou "B") et que la case d'arrivée est vide (0)
        if (piece.color != self.current_turn) and (piece.color != self.current_turn + "Q"):
            return False
        if self.grid[end[0]][end[1]] != 0 or self.grid[start[0]][start[1]] not in ("W", "B","WQ","BQ"):
            return False

        row_diff = end[0] - start[0]  # Différence sur les lignes
        col_diff = abs(start[1] - end[1])  # Différence absolue sur les colonnes

        #Si la piece est une reine ... Sinon
        print("reine is queen ? : " ,piece.isQueen)
        print("row diff col diff : ", abs(row_diff) ,col_diff)
        # Vérifie que le mouvement est dans la direction correcte pour un mouvement simple
        if abs(row_diff) == 1 and col_diff == 1:  # Mouvement simple
            if not piece.isQueen :
                if piece.color == "W" and row_diff <= 0:  # Blancs doivent avancer vers le bas
                    return False
                if piece.color == "B" and row_diff >= 0:  # Noirs doivent avancer vers le haut*
                    return False
                return True
            else:
                return True
        # Vérifie un mouvement de capture (deux cases)
        if abs(row_diff) == 2 and col_diff == 2:

            intermediate = self.get_intermediate_position(start, end)
            # Capture uniquement si la case intermédiaire contient une pièce adverse
            if self.grid[intermediate[0]][intermediate[1]] in ("W", "B") and self.grid[intermediate[0]][intermediate[1]] != piece.color:
                return True
        print("cc")
        return False


    def get_grid(self):
        return self.grid




