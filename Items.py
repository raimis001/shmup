import random
import pygame

import Helper
from Sprite import Sprite
from Game import Game

class Heart(Sprite):

    def __init__(self, game: Game) -> None:

        x = random.randrange(50, game.size.width - 50)
        pos = pygame.Vector2(x, -50)

        super().__init__(game, "Heart.png" , pos)

        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

        x = random.uniform(-1, 1)
        self.move = pygame.Vector2(x, 1).normalize()

        self.speed = 50

        self.game.items_group.add(self)

        

    def update(self) -> None:
        
        self.position += self.move * self.speed * self.game.deltaTime
        if self.position.x < 50 or self.position.x > self.game.size.width - 50:
            self.move.x *= -1

        super().update()

        if pygame.sprite.spritecollide(self, self.game.player_group, False ):
            Helper.PlaySound("collect.wav")
            self.game.score += 50
            if self.game.lives <= 7:
                self.game.lives += 1
            self.kill()

class Skull(Sprite):

    def __init__(self, game: Game,) -> None:
        x = random.randrange(50, game.size.width - 50)
        pos = pygame.Vector2(x, -50)

        super().__init__(game, "Skull.png", pos)

        x = random.uniform(-1, 1)
        self.move = pygame.Vector2(x, 1).normalize()

        self.speed = 50

        self.game.items_group.add(self)

        
    def update(self) -> None:
        
        self.position += self.move * self.speed * self.game.deltaTime
        if self.position.x < 50 or self.position.x > self.game.size.width - 50:
            self.move.x *= -1

        super().update()

        if pygame.sprite.spritecollide(self, self.game.player_group, False ):
            Helper.PlaySound("collect.wav")
            self.game.damage(10)  
        self.kill


delay_time = 10
def Craate(game: Game):
    global delay_time

    if delay_time > 0:
        delay_time -= game.deltaTime
        return
    
    delay_time = random.uniform(10, 20)
    rnd = random.randrange(0,100)

    if rnd < 40:
        Heart(game)
    else:
        Skull(game)

