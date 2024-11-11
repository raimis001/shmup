import pygame
import Bullet
from Game import Game
import Helper
import Input
from Sprite import Sprite


class Player(Sprite):

    def __init__(self, game: Game) -> None:
        
        pos = pygame.Vector2(game.size.centerx, game.size.height - 50)

        super().__init__(game, "Ship.png", pos)

        self.game.player_group.add(self)

        self.speed = 300

        self.bullet_position = pygame.Vector2(0, -10)

        self.shot_speed = 0.1
        self.shot_delay = 0

    def update(self) -> None:

        self.position += Input.Axis() * self.speed * self.game.deltaTime

        self.position.x = pygame.math.clamp(self.position.x, 20, self.game.size.width - 20)
        self.position.y = pygame.math.clamp(self.position.y, 20, self.game.size.height - 20)

        super().update()

        if self.shot_delay > 0:
            self.shot_delay -= self.game.deltaTime
            return

        if Input.MousePress():
            self.shot_delay = self.shot_speed
            pos = self.position + self.bullet_position
            Helper.PlaySound("laser.wav")
            Bullet.Create(self.game, pos, 0)

    def damage(self):
        Helper.PlaySound("hit.wav")
        self.game.damage()

    def restart(self):
        self.position = pygame.Vector2(self.game.size.centerx, self.game.size.height - 50)
        self.shot_delay = 1