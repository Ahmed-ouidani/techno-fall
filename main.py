import pygame
from models.Game import Game
pygame.init()    
pygame.mixer.init()    
        
clock = pygame.time.Clock()
FPS = 120

pygame.display.set_caption("Techno Fall")
screen = pygame.display.set_mode((550,650))

background = pygame.image.load('assets/bg.png')

ground = pygame.image.load('assets/ground.jpg')
ground = pygame.transform.scale(ground, (550,250))
ground_rect = ground.get_rect()
ground_rect.y = 600

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (240,130))
play_button_rect = play_button.get_rect()
play_button_rect.x = 155
play_button_rect.y = 250

game = Game()

run = True

while run :

    screen.blit(background, (-600, -150))
    if game.runing:
        screen.blit(ground, ground_rect)
        game.update_game(screen)
    else : 
        screen.blit(play_button, play_button_rect)

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
                game.sound_manager.play('click')
            
    clock.tick(FPS)