import pygame
from models.Game import Game
import math
pygame.init()        
        

pygame.display.set_caption("Techno Fall")
screen = pygame.display.set_mode((550,650))

background = pygame.image.load("assets/bg.png")

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (350, 300))
banner_rect = banner.get_rect()
banner_rect.x = 100
banner_rect.y = 100

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (250,90))
play_button_rect = play_button.get_rect()
play_button_rect.x = 155
play_button_rect.y = 320

game = Game()

run = True

while run :

    screen.blit(background, (-600, -150))

    if game.runing:
        game.update_game(screen)
    else : 
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.runing = True