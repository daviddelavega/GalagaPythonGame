class Settings:
    """A class to store all settings for Galaga"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.caption = 'Galaga'       
        self.bg_color = (0, 0, 0)
        self.frame_rate = 120
        self.ship_image = 'images/ship.bmp'
        self.alien_image = 'images/alien1.bmp'
        self.ship_speed = 9 
        # Bullet settings
        self.bullet_speed = 10
        self.bullets_allowed = 10
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (255, 255, 255)
        # Alien settings
        self.alien_speed = 3.0
        self.fleet_drop_speed = 5
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1