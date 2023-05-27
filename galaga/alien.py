import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, galaga_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = galaga_game.screen
        self.settings = galaga_game.settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(self.settings.alien_image)
        self.rect = self.image.get_rect()

        # Start each new alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if an alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

