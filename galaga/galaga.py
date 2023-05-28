import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

class Galaga:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()      
        self.theme_song_played = False    
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.sound = pygame.mixer.Sound(self.settings.theme_song)
        self.firing_sound = pygame.mixer.Sound(self.settings.firing_sound)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.stats = GameStats(self)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()               
        self._create_alien_fleet()
        pygame.display.set_caption(self.settings.caption)           

        # Start Galaga in an active state.
        self.game_active = True

    def run_game(self):
        """Start the main loop for the game."""        
        while True:          
            self._check_events()                     
            
            if self.game_active:
                self.ship.update()       
                self.bullets.update()
                self._delete_bullets()
                self._detect_alien_bullet_collisions()
                self._update_aliens()
                self._detect_alien_ship_collisions()
                self._repopulate_alien_fleet()

            self._update_screen()                   
            self.clock.tick(self.settings.frame_rate)   
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()            
       
        self.ship.blitme()
        self.aliens.draw(self.screen)           

        pygame.display.flip()

        if self.theme_song_played == False: 
            self.theme_song_played = self.play_theme_song()    

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)                    
                
    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group and play sound"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.play_firing_sound()  

    def _delete_bullets(self):
        """Get rid of bullets that have disappeared."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)     

    def _create_alien_fleet(self):
        """Create the fleet of aliens"""
        # Create an alient and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y <(self.screen_height - 12 * alien_height):
            while current_x < (self.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height       

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position          
        new_alien.rect.y = y_position  
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _detect_alien_bullet_collisions(self):
        """Check for any bullets that have hit aliens
        If so, get rid of the bullet and the alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
    def _repopulate_alien_fleet(self):
        """Check if all aliens are destroyed and empty bullets if true"""
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            
    def _detect_alien_ship_collisions(self):
        """Check for any aliens hitting the ship
        If so, game over."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship
            self._create_alien_fleet()
            self.ship.center_ship()
            #Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def play_theme_song(self):
        self.sound.play()
        # Wait until the sound finishes playing
        pygame.time.wait(int(self.sound.get_length() * 1000))
        return True
    
    def play_firing_sound(self):
        self.firing_sound.play()
  
if __name__ == '__main__':
    # Make a game instance, and run the game.
    galaga_game = Galaga()
    galaga_game.run_game()

        

