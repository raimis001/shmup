from typing import List
import pygame

from Game import Game
from Sprite import Sprite

class Bullet(Sprite):

    #bullet_type = 0 - player bullet
    #bullet_type = 1 - enemy bullet
    def __init__(self, game: Game, position: pygame.Vector2, bullet_type: int) -> None:
        super().__init__(game, "Bullet1.png", position)

        self.bullet_type = bullet_type

        y = -1 
        if bullet_type == 1:
            y = 1

        self.move = pygame.Vector2(0, y)

        self.speed = 430
        self.game.bullet_group.add(self)

        self.active = True

    def update(self) -> None:
        
        self.position += self.move * self.speed * self.game.deltaTime

        if self.position.y < -50 or self.position.y > self.game.size.height + 50:
            self.active = False
            self.remove(self.game.bullet_group)
            return

        super().update()
        
        group = self.game.enemy_group
        if self.bullet_type == 1:
            group = self.game.player_group

        colide = pygame.sprite.spritecollide(self, group, False )
        if colide:
            colide[0].damage()
            self.active = False
            self.remove(self.game.bullet_group)
            return


    def activate(self, position: pygame.Vector2, bullet_type: int):
        
        self.active = True
        self.bullet_type = bullet_type
        self.position = position

        y = -1 
        if bullet_type == 1:
            y = 1

        self.move = pygame.Vector2(0, y)

        self.game.bullet_group.add(self)



bullet_pool: List[Bullet] = []
def Create(game: Game, position: pygame.Vector2, bullet_type: int):
    for bullet in bullet_pool:
        if bullet.active:
            continue
        
        bullet.activate(position, bullet_type)
        return
    
    bullet = Bullet(game, position, bullet_type)
    bullet_pool.append(bullet)
