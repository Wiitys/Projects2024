class Board:
    """
    Classe Board
    Possède toutes les fonctionnalités du plateau de jeu pour instancier et jouer les pièces sur le plateau
    """

    def __init__(self):
        self.grid = []
        self.current_turn = "W"  # Définir le joueur actuel ("W" pour blanc, "B" pour noir)

    def initialize_board(self):
        """
        Fonction permettant d'initialiser le plateau de jeu avec les pions.
        """
        self.grid = [["W" if (i + j) % 2 == 0 and i < 5 else "B" if (i + j) % 2 == 0 and i > 5 else 0 for j in range(10)] for i in range(10)]
        for i in range(4, 6):
            self.grid[i] = [0 for j in range(10)]

    def get_intermediate_position(self, start, end):
        """
        Renvoie la position intermédiaire entre le départ et l'arrivée si le mouvement est de deux cases
        """
        mid_row = (start[0] + end[0]) // 2
        mid_col = (start[1] + end[1]) // 2
        return mid_row, mid_col

    def move_piece_handler(self, start, end, piece):
        """
        Gère le déplacement en appelant la bonne méthode en fonction du type de pièce.  
        """
        if piece.isQueen:
            return self.move_piece_queen(start, end, piece)
        else:
            return self.move_piece_pawn(start, end, piece)

    def is_valid_move_pawn(self, start, end, piece):
        """
        Vérifie si un mouvement est valide pour un pion de base.
        """
        if (piece.color != self.current_turn):
            return False
        if self.grid[end[0]][end[1]] != 0 or self.grid[start[0]][start[1]] not in ("W", "B"):
            return False

        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])

        # Mouvement simple pour un pion
        if abs(row_diff) == 1 and col_diff == 1:
            if piece.color == "W" and row_diff <= 0:
                return False
            if piece.color == "B" and row_diff >= 0:
                return False
            return True

        # Capture pour un pion
        if abs(row_diff) == 2 and col_diff == 2:
            intermediate = self.get_intermediate_position(start, end)
            if self.grid[intermediate[0]][intermediate[1]] in ("W", "B") and self.grid[intermediate[0]][intermediate[1]] != piece.color:
                return True

        return False

    def is_valid_move_queen(self, start, end, piece):
        """
        Vérifie si un mouvement est valide pour une dame.
        """
        if (piece.color != self.current_turn + "Q"):
            return False
        if self.grid[end[0]][end[1]] != 0:
            return False

        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])

        if abs(row_diff) == abs(col_diff):
            step_row = 1 if row_diff > 0 else -1
            step_col = 1 if end[1] > start[1] else -1

            current_row, current_col = start[0] + step_row, start[1] + step_col
            found_piece = False

            while current_row != end[0] and current_col != end[1]:
                if self.grid[current_row][current_col] in ("W", "B", "WQ", "BQ"):
                    if found_piece:  # Une pièce a déjà été rencontrée
                        return False
                    found_piece = True  # Première pièce rencontrée
                current_row += step_row
                current_col += step_col

            return True

        return False

    def move_piece_pawn(self, start, end, piece):
        """
        Déplace un pion de base.
        """
        if not self.is_valid_move_pawn(start, end, piece):
            return False, False, piece, -1, -1

        piece.color = self.grid[start[0]][start[1]]
        piece_captured = False
        piece_mange_x, piece_mange_y = -1, -1

        if abs(start[0] - end[0]) == 2:
            intermediate = self.get_intermediate_position(start, end)
            if self.grid[intermediate[0]][intermediate[1]] in ("W", "B"):
                self.grid[intermediate[0]][intermediate[1]] = 0
                piece_captured = True
                piece_mange_x, piece_mange_y = intermediate

        self.grid[start[0]][start[1]] = 0
        self.grid[end[0]][end[1]] = piece.color
        piece.x, piece.y = end[0], end[1]

        if end[0] == 9 and piece.color == "W":
            piece.promote()
            self.grid[end[0]][end[1]] = "WQ"
            piece.color = "WQ"
        if end[0] == 0 and piece.color == "B":
            piece.promote()
            self.grid[end[0]][end[1]] = "BQ"
            piece.color = "BQ"

        return True, piece_captured, piece, piece_mange_x, piece_mange_y

    def move_piece_queen(self, start, end, piece):
        """
        Déplace une dame.
        """
        if not self.is_valid_move_queen(start, end, piece):
            return False, False, piece, -1, -1

        piece.color = self.grid[start[0]][start[1]]
        piece_captured = False
        piece_mange_x, piece_mange_y = -1, -1

        step_row = 1 if end[0] > start[0] else -1
        step_col = 1 if end[1] > start[1] else -1
        current_row, current_col = start[0] + step_row, start[1] + step_col

        while current_row != end[0] and current_col != end[1]:
            if self.grid[current_row][current_col] in ("W", "B", "WQ", "BQ"):
                self.grid[current_row][current_col] = 0
                piece_captured = True
                piece_mange_x, piece_mange_y = current_row, current_col
                break
            current_row += step_row
            current_col += step_col

        self.grid[start[0]][start[1]] = 0
        self.grid[end[0]][end[1]] = piece.color
        piece.x, piece.y = end[0], end[1]

        return True, piece_captured, piece, piece_mange_x, piece_mange_y

    def get_grid(self):
        return self.grid
