import pygame

class soundman():
    def __init__(self):
        self.sounds = {
            'click' : pygame.mixer.Sound('assets/sounds/click.wav'),
            'bonus' : pygame.mixer.Sound('assets/sounds/bonus.wav'),
            'game_over' : pygame.mixer.Sound('assets/sounds/GameOver.ogg'),
            'bad_bonus' : pygame.mixer.Sound('assets/sounds/hd.flac'),
            'good_bonus' : pygame.mixer.Sound('assets/sounds/hi.flac'),
        }

    def play(self, name):
        self.sounds[name].play()

    def setvol(self,volume,name):
        self.sounds[name].set_volume(volume)