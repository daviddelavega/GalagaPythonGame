class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, galaga_game):
        self.settings = galaga_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit