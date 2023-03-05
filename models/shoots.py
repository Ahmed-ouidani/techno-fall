import pygame
import random

class shoots(pygame.sprite.Sprite):

    def __init__(self,game,image,type):
        super().__init__()
        self.game = game
        self.velocity = 1
        self.max_velocity = 20
        self.time = 10
        self.min_time = 2
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image , (40,40))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = random.randint(-15 , 445)
        self.type = type

    def remove(self):
        self.game.all_shoots.remove(self)

    def move_down(self):

        if not self.game.check_collettion(self, self.game.all_players):
            self.rect.y += self.velocity
        else : 
            self.remove()
            self.game.sound_manager.play("bonus")
            self.game.player.score_inc(100)

        if self.rect.y > 570:
            self.remove()
            if not self.type == "heart" and not self.type == "virus":
                self.game.player.dec_heart()

    def speedup(self):  
        if self.velocity  > self.max_velocity :
            self.velocity += 1



class cd(shoots):
    def __init__(self,game,):
        super().__init__(game,'assets/cd.png', 'cd')


class keyboard(shoots):
    def __init__(self,game):
        super().__init__(game,'assets/keyboard.png', 'keyboard')

class laptop(shoots):
    def __init__(self, game):
        super().__init__(game, 'assets/laptop.png', 'laptop')

class heart(shoots):
    def __init__(self,game):
        super().__init__(game, 'assets/heart.png', 'heart')

    def catch_heart(self):
        if self.game.check_collettion(self, self.game.all_players) and self.game.player.lifes < 3:
            self.remove()
            self.game.player.inc_heart()

class virus(shoots):
    def __init__(self,game):
        super().__init__(game, 'assets/virus.png', 'virus')

    def catch_virus(self):
        if self.game.check_collettion(self, self.game.all_players):
            self.remove()
            self.game.player.dec_heart()