from typing import Any
import pygame

from Game import Game
import Helper

class Explosion(pygame.sprite.Sprite):

    def __init__(self, game: Game, position: pygame.Vector2) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.game = game
        self.position = position

        self.images = []

        self.anim_count = 5
        for i in range(1, self.anim_count + 1):
            file = f"exp{i}.png"
            self.images.append(Helper.LoadImage(file))

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.anim_speed = 0.2
        self.anim_delta = self.anim_speed
        self.anim_index = 0

        self.game.explosion_group.add(self)

        Helper.PlaySound("explosion.wav")


    def update(self) -> None:
        if self.anim_delta > 0:
            self.anim_delta -= self.game.deltaTime
            return
        
        self.anim_delta = self.anim_speed
        self.anim_index += 1
        if self.anim_index >= self.anim_count:
            self.kill()
            return

        self.image = self.images[self.anim_index]

        super().update()

