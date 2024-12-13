class Player:
    """
        Classe Player
        Possède toutes les fonctionnalités d'un joueur dans un jeu de dame
    """

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces_count = 12       
        self.captures_count = 0      

    def lose_piece(self):
        """Réduit le nombre de pièces restantes du joueur lorsqu'il en perd une."""
        if self.pieces_count > 0:
            self.pieces_count -= 1

    def capture_opponent_piece(self):
        """Incrémente le nombre de pièces adverses capturées par le joueur."""
        self.captures_count += 1

    def has_pieces_left(self):
        """Retourne True si le joueur a encore des pièces sur le plateau, sinon False."""
        return self.pieces_count > 0

    def __str__(self):
        return f"{self.name} ({self.color}) - Pièces restantes: {self.pieces_count}, Pièces capturées: {self.captures_count}"
