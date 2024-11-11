import pygame
from Canvas import UI
import Enemy
from Game import Game
import Items
from Player import Player
from Space import Starfield

clock = pygame.time.Clock()

running = True

game = Game()
player = Player(game)
ui = UI(game)
background = Starfield(game)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.screen.fill("black")

    if game.lives <= 0:
        ui.drawEndPanel()
        pygame.display.flip()
        game.deltaTime = clock.tick(60) / 1000
        continue

    background.update()

    Enemy.Create(game)
    Items.Craate(game)

    game.update()

    ui.update()

    pygame.display.flip()
    game.deltaTime = clock.tick(60) / 1000

pygame.quit()