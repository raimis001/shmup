import random
import pygame

import Bullet
from Explosion import Explosion
from Game import Game
import Helper
from Sprite import Sprite

class Enemy(Sprite):

    def __init__(self, game: Game) -> None:

        x = random.randrange(50, game.size.width - 50)
        pos = pygame.Vector2(x, -50)

        super().__init__(game, "ShipE1.png" , pos)

        x = random.uniform(-1,1)
        self.move = pygame.Vector2(x, 1).normalize()

        self.speed = 70

        self.bullet_position = pygame.Vector2(0, 10)

        self.lives = 3
        self.shot_speed = 0.2
        self.shot_delay = 0
        self.shot_count = 0
        self.shot_max = 3
        self.shot_wait = 2

        self.game.enemy_group.add(self)

    def update(self) -> None:
        
        self.position += self.move * self.speed * self.game.deltaTime

        if self.position.y > self.game.size.height + 50:
            self.game.score -= 5
            self.kill()
            return
        
        if self.position.x < 50 or self.position.x > self.game.size.width - 50:
            self.move.x *= -1

        super().update()

        if pygame.sprite.spritecollide(self, self.game.player_group, False):
            self.game.score += 20
            self.game.damage()
            self.kill()
            Explosion(self.game, self.position)
            return
        
        if self.shot_delay > 0:
            self.shot_delay -= self.game.deltaTime
            return

        self.shot_count += 1

        if self.shot_count >= self.shot_max:
            self.shot_delay = self.shot_wait
            self.shot_count = 0
        else:
            self.shot_delay = self.shot_speed

        pos = self.position + self.bullet_position
        Helper.PlaySound("laser1.wav")
        Bullet.Create(self.game, pos, 1)


    def damage(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game.score += 10
            Explosion(self.game, self.position)
            self.kill()



delay_time = 3
def Create(game: Game):
    global delay_time

    if delay_time > 0:
        delay_time -= game.deltaTime
        return

    
    delay_time = random.uniform(2,4)
    Enemy(game)

