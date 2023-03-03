import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.lifes = 3
        self.max_lifes = 3
        self.velocity = 2
        self.max_velocity = 7
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (120,120))
        self.rect = self.image.get_rect()
        self.rect.y = 500
        self.rect.x = 200
        self.score = 0
        self.heart = pygame.image.load('assets/heart.png')
        self.heart = pygame.transform.scale(self.heart, (40, 40))
        self.heart_rect = self.heart.get_rect()
        self.heart_rect.y = 30
        self.heart_rect.x = 30

    def score_inc(self, score):
        self.score += score

    def update_lifes(self,screen):
        font = pygame.font.Font(None, 24)
        text_surface = font.render("X"+str(self.lifes), True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(90, 45))
        screen.blit(text_surface, text_rect)

    def move_left(self):
        self.rect.x -= self.velocity
        # self.image = pygame.image.load('assets/player.png')
        # self.image = pygame.transform.scale(self.image, (120,120))

    def move_right(self):
        self.rect.x += self.velocity
        # self.image = pygame.image.load('assets/player_r.png')
        # self.image = pygame.transform.scale(self.image, (120,120))

    def dec_heart(self):
        self.lifes -= 1
        if self.lifes == 0:
            self.game.game_over()
    
    def inc_heart(self):
        self.lifes += 1

    def inc_speed(self):
        self.velocity += 1