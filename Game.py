import pygame

import Helper

class Game:

    size = pygame.rect.Rect(0,0,800, 800)
    deltaTime = 0

    score = 0
    lives = 5

    @property
    def center(self):
        return pygame.Vector2(self.size.centerx, self.size.centery)

    def __init__(self) -> None:
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.size.bottomright)

        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()

    def update(self):

        self.player_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.explosion_group.update()
        self.items_group.update()

        self.player_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.bullet_group.draw(self.screen)
        self.items_group.draw(self.screen)

        self.explosion_group.draw(self.screen)

    def damage(self, lives = 1):
        if self.lives <= 0:
            return

        self.lives -= lives
        if self.lives <= 0:
            self.dead()

    def dead(self):
        Helper.PlaySound("fail.wav")

    def restart(self):
        self.enemy_group.empty()
        self.bullet_group.empty()
        self.explosion_group.empty()
        self.items_group.empty()


        self.lives = 5
        self.score = 0

        for player in self.player_group:
            player.restart()
     
    
