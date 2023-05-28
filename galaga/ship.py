import pygame
from settings import Settings

class Ship:
    """A class to manage the ship"""

    def __init__(self, galaga_game):
        """Initialize the ship and set its starting position"""
        self.screen = galaga_game.screen
        self.screen_rect = galaga_game.screen.get_rect()
        self.settings = galaga_game.settings
        self.galaga_game = galaga_game

        # Load ths ship image and get its rect
        self.image = pygame.image.load(self.settings.ship_image) 
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Move right flag; start with a ship that's not moving.
        self.moving_right = False  
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right:
            if self.rect.x <= self.galaga_game.screen_width - self.rect.width:
                self.rect.x += self.settings.ship_speed
        elif self.moving_left:
             if self.rect.x >= 0:
                self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    