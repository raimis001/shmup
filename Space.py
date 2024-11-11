import pygame

from Game import Game
import Helper

class Starfield:

    def __init__(self, game: Game) -> None:

        self.game = game

        self.image = Helper.LoadImage("Starfield.png")
        self.image = pygame.transform.scale(self.image, (self.game.size.width / 2, self.game.size.height / 2))

        self.rect = self.image.get_rect()

        self.scrollY = 0
        self.speed = 20

    def update(self):
        for x in range(0, 2):
            for y in range(0, 3):
                self.game.screen.blit(self.image,(x * self.rect.width , self.scrollY + (y - 1) * self.rect.height ))
        
        self.scrollY += self.speed * self.game.deltaTime
        if self.scrollY > self.rect.height:
            self.scrollY = 0

