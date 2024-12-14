import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Projects2024.backend.attributs_de_jeu.Board import Board
from Projects2024.backend.attributs_de_jeu.Piece import Piece


class TestBoard(unittest.TestCase):

    def setUp(self):
        """Initialise un plateau avant chaque test."""
        self.board = Board()
        self.board.initialize_board()
        self.board.grid = [[0] * 10 for _ in range(10)]  # Réinitialisation de la grille

    def test_initialize_board(self):
        """Teste l'initialisation du plateau."""
        self.board.initialize_board()
        grid = self.board.get_grid()
        self.assertEqual(len(grid), 10)
        self.assertEqual(len(grid[0]), 10)
        self.assertEqual(grid[0][0], "W")
        self.assertEqual(grid[9][9], "B")
        self.assertEqual(grid[4][4], 0)

    def test_get_intermediate_position(self):
        """Teste la récupération de la position intermédiaire."""
        start = (2, 2)
        end = (4, 4)
        intermediate = self.board.get_intermediate_position(start, end)
        self.assertEqual(intermediate, (3, 3))

    def test_is_valid_move_pawn_simple(self):
        """Teste un mouvement simple valide pour un pion."""
        piece = Piece("W")
        start = (3, 3)
        end = (4, 4)
        self.board.grid[3][3] = "W"  # Ajout du pion sur la grille
        self.assertTrue(self.board.is_valid_move_pawn(start, end, piece))

    def test_is_valid_move_pawn_invalid(self):
        """Teste un mouvement invalide pour un pion."""
        piece = Piece("W")
        start = (2, 2)
        end = (4, 4)  # Mouvement trop long sans capture
        self.board.grid[2][2] = "W"  # Ajout du pion sur la grille
        self.assertFalse(self.board.is_valid_move_pawn(start, end, piece))

    def test_is_valid_move_pawn_capture(self):
        """Teste un mouvement de capture valide pour un pion."""
        piece = Piece("W")
        start = (2, 2)
        end = (4, 4)
        self.board.grid[2][2] = "W"  # Pion blanc
        self.board.grid[3][3] = "B"  # Pion noir (cible)
        self.assertTrue(self.board.is_valid_move_pawn(start, end, piece))

    def test_move_piece_pawn_valid(self):
        """Teste le déplacement valide d'un pion."""
        piece = Piece("W")
        start = (2, 2)
        end = (3, 3)
        self.board.grid[2][2] = "W"  # Position du pion blanc
        valid, captured, moved_piece, x, y = self.board.move_piece_pawn(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.board.grid[2][2], 0)  # L'ancienne case est vide
        self.assertEqual(self.board.grid[3][3], "W")  # La nouvelle case contient le pion

    def test_move_piece_pawn_capture(self):
        """Teste un mouvement de capture avec un pion."""
        piece = Piece("W")
        start = (2, 2)
        end = (4, 4)
        self.board.grid[2][2] = "W"  # Pion blanc
        self.board.grid[3][3] = "B"  # Pion noir (cible)

        valid, captured, moved_piece, x, y = self.board.move_piece_pawn(start, end, piece)

        self.assertTrue(valid)
        self.assertTrue(captured)
        self.assertEqual(self.board.grid[2][2], 0)
        self.assertEqual(self.board.grid[3][3], 0)
        self.assertEqual(self.board.grid[4][4], "W")

    def test_is_valid_move_queen_valid(self):
        """Teste un mouvement valide pour une dame."""
        piece = Piece("WQ")
        piece.promote()  # Promotion en dame
        start = (2, 2)
        end = (4, 4)
        self.board.grid[2][2] = "WQ"  # Position initiale de la dame
        self.assertTrue(self.board.is_valid_move_queen(start, end, piece))

    def test_move_piece_queen_valid(self):
        """Teste le déplacement valide d'une dame."""
        piece = Piece("WQ", isQueen=True)
        start = (2, 2)
        end = (4, 4)
        self.board.grid[2][2] = "WQ"
        valid, captured, moved_piece, x, y = self.board.move_piece_queen(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.board.grid[2][2], 0)  # L'ancienne case est vide
        self.assertEqual(self.board.grid[4][4], "WQ")  # La nouvelle case contient la dame

    def test_move_piece_pawn_promotion(self):
        """Teste la promotion d'un pion en dame."""
        piece = Piece("W")
        start = (8, 2)
        end = (9, 3)
        self.board.grid[8][2] = "W"  # Position du pion blanc
        valid, captured, moved_piece, x, y = self.board.move_piece_pawn(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.board.grid[9][3], "WQ")  # La case contient une dame
        self.assertTrue(moved_piece.isQueen)  # Le pion est promu en dame


if __name__ == '__main__':
    unittest.main()
