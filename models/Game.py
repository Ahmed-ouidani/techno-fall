from models.Player import Player
import pygame
from models.shoots import cd
from models.shoots import keyboard
from models.shoots import laptop
from models.shoots import heart
from models.shoots import virus
from models.event import event
from models.sounds import soundman
import random

class Game:

    def __init__(self):
        self.runing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_shoots = pygame.sprite.Group()
        self.event = event(self)
        self.sound_manager = soundman()

    def game_over(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_shoots = pygame.sprite.Group()
        self.runing = False

    
    def lunch_cd(self):
        n = random.randint(1, 100)
        if n >= 1 and n < 27:
            self.all_shoots.add(cd(self))
        elif n < 54: 
            self.all_shoots.add(keyboard(self))
        elif n == 55:
            self.all_shoots.add(heart(self))
        elif n < 82 :
            self.all_shoots.add(laptop(self))
        else:
            self.all_shoots.add(virus(self)) 

    def check_collettion(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def update_score(self,screen):
        font = pygame.font.Font(None, 24)
        text_surface = font.render("Score : "+str(self.player.score), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(500, 45))
        screen.blit(text_surface, text_rect)

    def update_game(self, screen):
        screen.blit(self.player.image, self.player.rect)
   
        screen.blit(self.player.heart, self.player.heart_rect)
        self.player.update_lifes(screen)
        self.update_score(screen)

        for shoot in self.all_shoots:
            shoot.move_down()
            if shoot.type == "heart":
                shoot.catch_heart()
            elif shoot.type == "virus":
                shoot.catch_virus()
            
        self.event.raz()

        self.event.inc_percentage()

        self.all_shoots.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 450:
            self.player.move_right()
            self.player.image = pygame.image.load('assets/player_r.png')
            self.player.image = pygame.transform.scale(self.player.image, (120,120))

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -20:
            self.player.move_left()
            self.player.image = pygame.image.load('assets/player.png')
            self.player.image = pygame.transform.scale(self.player.image, (120,120))

    def speed_up(self):
        if (self.player.score % 2000) == 0 :
            self.event.inc_speed()
            self.all_shoots.speedup()
        
