import unittest
from Backend.Piece import Piece

class TestPiece(unittest.TestCase):

    def setUp(self):
        """Initialiser une pièce avant chaque test."""
        self.piece_pawn = Piece(color="W")
        self.piece_queen = Piece(color="B", isQueen=True, p_x=5, p_y=5)

    def test_initialization_pawn(self):
        """Tester l'initialisation d'un pion."""
        self.assertEqual(self.piece_pawn.color, "W")
        self.assertFalse(self.piece_pawn.isQueen)
        self.assertTrue(self.piece_pawn.isAlive)
        self.assertEqual(self.piece_pawn.x, -1)
        self.assertEqual(self.piece_pawn.y, -1)

    def test_initialization_queen(self):
        """Tester l'initialisation d'une dame."""
        self.assertEqual(self.piece_queen.color, "B")
        self.assertTrue(self.piece_queen.isQueen)
        self.assertEqual(self.piece_queen.x, 5)
        self.assertEqual(self.piece_queen.y, 5)

    def test_promotion(self):
        """Tester la promotion d'un pion en dame."""
        self.assertFalse(self.piece_pawn.isQueen)
        self.piece_pawn.Promote()
        self.assertTrue(self.piece_pawn.isQueen)

    def test_get_coordinates(self):
        """Tester la récupération des coordonnées d'une pièce."""
        # Pour un pion
        self.assertEqual(self.piece_pawn.ObtenirCoordonnees(), [-1, -1])

        # Pour une dame
        self.assertEqual(self.piece_queen.ObtenirCoordonnees(), [5, 5])

if __name__ == "__main__":
    unittest.main()
