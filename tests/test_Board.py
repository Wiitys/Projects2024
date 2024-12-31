import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Backend.Plateau import Plateau
from Frontend.Interface import Piece


class TestPlateau(unittest.TestCase):

    def setUp(self):
        """Initialise un plateau avant chaque test."""
        self.plateau = Plateau()
        self.plateau.InitialiserPlateau()
        self.plateau.grille = [[0] * 10 for _ in range(10)]  # Réinitialisation de la grille

    def TestInitialisationPlateau(self):
        """Teste l'initialisation du plateau."""
        self.plateau.InitialiserPlateau()
        grille = self.plateau.grille
        self.assertEqual(len(grille), 10)
        self.assertEqual(len(grille[0]), 10)
        self.assertEqual(grille[0][0], "W")
        self.assertEqual(grille[9][9], "B")
        self.assertEqual(grille[4][4], 0)

    def test_get_intermediate_position(self):
        """Teste la récupération de la position intermédiaire."""
        start = (2, 2)
        end = (4, 4)
        intermediate = self.plateau.ObtenirPositionIntermediaire(start, end)
        self.assertEqual(intermediate, (3, 3))

    def test_is_valid_move_pawn_simple(self):
        """Teste un mouvement simple valide pour un pion."""
        piece = Piece("W",False,3,3)
        self.plateau.tourCourant = "W"
        start = (3, 3)
        end = (4, 4)
        self.plateau.grille[3][3] = "W"  # Ajout du pion sur la grille
        self.assertTrue(self.plateau.VerifieSiMouvementPionValide(start, end, piece))

    def test_is_valid_move_pawn_invalid(self):
        """Teste un mouvement invalide pour un pion."""
        piece = Piece("W")
        self.plateau.tourCourant = "W"
        start = (2, 2)
        end = (4, 4)  # Mouvement trop long sans capture
        self.plateau.grille[2][2] = "W"  # Ajout du pion sur la grille
        self.assertFalse(self.plateau.VerifieSiMouvementPionValide(start, end, piece))

    def test_is_valid_move_pawn_capture(self):
        """Teste un mouvement de capture valide pour un pion."""
        piece = Piece("W",False,3,3)
        self.plateau.tourCourant = "W"
        start = (2, 2)
        end = (4, 4)
        self.plateau.grille[2][2] = "W"  # Pion blanc
        self.plateau.grille[3][3] = "B"  # Pion noir (cible)
        self.assertTrue(self.plateau.VerifieSiMouvementPionValide(start, end, piece))

    def test_move_piece_pawn_valid(self):
        """Teste le déplacement valide d'un pion."""
        piece = Piece("W",False,3,3)
        self.plateau.tourCourant = "W"
        start = (2, 2)
        end = (3, 3)
        self.plateau.grille[2][2] = "W"  # Position du pion blanc
        valid, captured, moved_piece, x, y = self.plateau.DeplacerPion(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.plateau.grille[2][2], 0)  # L'ancienne case est vide
        self.assertEqual(self.plateau.grille[3][3], "W")  # La nouvelle case contient le pion

    def test_move_piece_pawn_capture(self):
        """Teste un mouvement de capture avec un pion."""
        piece = Piece("W",False,3,3)
        self.plateau.tourCourant = "W"
        start = (2, 2)
        end = (4, 4)
        self.plateau.grille[2][2] = "W"  # Pion blanc
        self.plateau.grille[3][3] = "B"  # Pion noir (cible)

        valid, captured, moved_piece, x, y = self.plateau.DeplacerPion(start, end, piece)

        self.assertTrue(valid)
        self.assertTrue(captured)
        self.assertEqual(self.plateau.grille[2][2], 0)
        self.assertEqual(self.plateau.grille[3][3], 0)
        self.assertEqual(self.plateau.grille[4][4], "W")

    def test_is_valid_move_queen_valid(self):
        """Teste un mouvement valide pour une dame."""
        piece = Piece("WQ")
        self.plateau.tourCourant = "W"
        piece.Promote()  # Promotion en dame
        start = (2, 2)
        end = (4, 4)
        self.plateau.grille[2][2] = "WQ"  # Position initiale de la dame
        self.assertTrue(self.plateau.VerifieSiMouvementReineValide(start, end, piece))

    def test_move_piece_queen_valid(self):
        """Teste le déplacement valide d'une dame."""
        piece = Piece("WQ", isQueen=True)
        self.plateau.tourCourant = "W"
        start = (2, 2)
        end = (4, 4)
        self.plateau.grille[2][2] = "WQ"
        valid, captured, moved_piece, x, y = self.plateau.DeplacerReine(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.plateau.grille[2][2], 0)  # L'ancienne case est vide
        self.assertEqual(self.plateau.grille[4][4], "WQ")  # La nouvelle case contient la dame

    def test_move_piece_pawn_promotion(self):
        """Teste la promotion d'un pion en dame."""
        piece = Piece("W")
        self.plateau.tourCourant = "W"
        start = (8, 2)
        end = (9, 3)
        self.plateau.grille[8][2] = "W"  # Position du pion blanc
        valid, captured, moved_piece, x, y = self.plateau.DeplacerPion(start, end, piece)

        self.assertTrue(valid)
        self.assertFalse(captured)
        self.assertEqual(self.plateau.grille[9][3], "WQ")  # La case contient une dame
        self.assertTrue(moved_piece.isQueen)  # Le pion est promu en dame 




if __name__ == '__main__':
    unittest.main()
