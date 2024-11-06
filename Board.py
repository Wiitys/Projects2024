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
        # Initialisation de la grille avec des 1 pour signaler la présence des pions
        self.grid = [["W" if (i + j) % 2 == 0 and i<5 else "B" if (i + j) % 2 == 0 and i>5  else 0 for j in range(10)] for i in range(10)]

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

    def move_piece(self, start, end):
        """
        Vérifie si la pièce est déplaçable et la déplace si possible. Mange une pièce si elle est sur le chemin.
        :param start: position de base de la pièce
        :param end: position future de la pièce
        :return: Boolean -> si la pièce est déplaçable ou non
        """
        if self.is_valid_move(start, end):
            # Vérifie s'il y a une pièce intermédiaire pour un mouvement de saut
            if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 2:
                intermediate = self.get_intermediate_position(start, end)

                # Si une pièce ennemie se trouve à la position intermédiaire, elle est mangée
                if self.grid[intermediate[0]][intermediate[1]] == 1:
                    self.grid[intermediate[0]][intermediate[1]] = 0  # Retire la pièce mangée

            # Effectue le mouvement
            self.grid[start[0]][start[1]] = 0
            self.grid[end[0]][end[1]] = 1

    def is_valid_move(self, start, end):
        """
        Vérifie si un mouvement est valide. Un mouvement de deux cases est valide si une pièce peut être mangée.
        """
        if self.grid[end[0]][end[1]] != 0 or self.grid[start[0]][start[1]] != 1:
            return False

        row_diff = abs(start[0] - end[0])
        col_diff = abs(start[1] - end[1])

        # Mouvement d'une case diagonale sans capture
        if row_diff == 1 and col_diff == 1:
            return True
        # Mouvement de deux cases avec une pièce intermédiaire pour capturer
        elif row_diff == 2 and col_diff == 2:
            intermediate = self.get_intermediate_position(start, end)
            return self.grid[intermediate[0]][intermediate[1]] == 1  # Capture uniquement s'il y a une pièce
        return False


def test():
    board = Board()
    board.initialize_board()

    print("Plateau initial :")
    for row in board.grid:
        print(row)

    # Exemple de mouvement de capture
    board.move_piece((2, 2), (4, 4))  # Ce mouvement doit capturer la pièce en (3, 3)

    print("\nPlateau après capture :")
    for row in board.grid:
        print(row)


test()
