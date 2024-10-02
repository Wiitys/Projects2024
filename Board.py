
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
        Fonction permettant à l'appel d'initialiser le plateau de jeu ainsi que la présence des pions
        """
        # Initialisation de la grille avec des 1 pour signier la présence des pions
        self.grid = [[1 for _ in range(10)] for _ in range(10)]

        # Modification des deux lignes du milieu pour les remplir de 0 car il n'y a pas de pions ici
        for i in range(4, 6):
            self.grid[i] = [0 for _ in range(10)]

    def move_piece(self,start,end):
        """
        Vérifie si la pièce est déplaçable et la déplace si possible.
        :param start: position de base de la pièce
        :param end: position future de la pièce
        :return: Boolean -> si la pièce est déplaçable ou non
        """
        if(self.is_valid_move(start,end)):
            self.grid[start[0]][start[1]] = 0
            self.grid[end[0]][end[1]] = 1

    def is_valid_move(self,start,end):
        if(self.grid[end[0]][end[1]] == 0 and (start[0] - end[0]) <= 1 and (start[1] - end[1]) <= 1):
            return True
        else :
            return False

def test():
    board = Board()
    board.initialize_board()
    for row in board.grid:
        print(row)
    board.move_piece((4,4),(4,5))
    print("\n")
    for row in board.grid:
        print(row)

test()