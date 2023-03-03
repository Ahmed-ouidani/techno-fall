import pygame

class event():
    def __init__(self, game):
        self.game = game
        self.speed = 1
        self.max_speed = 5
        self.percent = 0
        self.max_percent = 100

    def inc_speed(self):
        if self.speed < self.max_speed:
            self.speed += 1

    def inc_percentage(self):
        if self.percent < self.max_percent :
            self.percent += self.speed
    
    def raz(self):
        if self.percent >= self.max_percent :
            self.game.lunch_cd()
            self.percent = 0