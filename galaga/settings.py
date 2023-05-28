class Settings:
    """A class to store all settings for Galaga"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.caption = 'Galaga'       
        self.bg_color = (0, 0, 0)
        self.frame_rate = 120
        # Image settings
        self.galaga_logo_image = 'images/galaga_logo.bmp'
        self.ship_image = 'images/ship.bmp'
        self.alien_image = 'images/alien1.bmp'       
        # Sound settings
        self.theme_song = 'sound/Galaga_Theme_Song.wav'
        self.firing_sound = 'sound/Galaga_Firing_Sound_Effect.wav'  
        # Ship settings
        self.ship_speed = 9
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 15
        self.bullets_allowed = 35
        self.bullet_width = 7
        self.bullet_height = 25
        self.bullet_color = (255, 0, 0)
        # Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 7
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1