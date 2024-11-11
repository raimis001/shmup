from typing import Any
import pygame

from Game import Game
import Helper

class Sprite(pygame.sprite.Sprite):

    def __init__(self, game: Game, imageName: str, position: pygame.Vector2 ) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.game = game

        self.image = Helper.LoadImage(imageName)
        self.rect = self.image.get_rect()

        self.position = position

    def update(self) -> None:
        
        self.rect.center = self.position

        super().update()
    


