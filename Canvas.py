import pygame

from Game import Game
import Helper
import Input

class UI:

    def __init__(self, game: Game) -> None:
        self.game = game

        self.heart = Helper.LoadImage("Heart.png")
        self.heart = pygame.transform.scale(self.heart, (32,32))
        self.heart_r = self.heart.get_rect()

        self.fonts = []
        self.fonts.append(pygame.font.Font(Helper.AssetPath("Pixel.ttf"), 60)) #0 Game font
        self.fonts.append(pygame.font.Font(Helper.AssetPath("Pixel.ttf"), 40)) #1 Game font

        self.colors = [
            (200,200,200),   #0 game font color
            (251,225,187),   #1 panel color
            (83,68,56),      #2 panel fame color
            (50,50,50),      #3 panel font color
            (206,165,136),   #4 button color
            (120,82,55),     #5 button ower color
        ]

        self.botton_ower1 = False
        self.button_ower2 = False

    def drawText(self, text: str, font: pygame.font.Font, color, position: pygame.Vector2, align: int = 0, valig: int = 0):
        img = font.render(text, True, color)

        pos = position * 1
        if align == 1:
            w = img.get_width()
            pos.x -= w / 2
        elif align == 2:
            w = img.get_width()
            pos.x -= w

        if valig == 1:
            h = img.get_height()
            pos.y -= h / 2
        elif valig == 2:
            h = img.get_height()
            pos.y -= h

        self.game.screen.blit(img, pos)

    def update(self):
        #todo: draw lives

        text = str(self.game.score)
        pos = pygame.Vector2(self.game.size.centerx, 20)
        self.drawText(text, self.fonts[0], self.colors[0], pos, 1)

        pos = pygame.Vector2(10,20)
        for i in range(0, self.game.lives):
            self.game.screen.blit(self.heart,(pos.x + i * self.heart_r.width + 5, pos.y))

    def drawPanel(self, color, color_fame, rect, radius, width):
        pygame.draw.rect(self.game.screen, color, rect, border_radius = radius)
        pygame.draw.rect(self.game.screen, color_fame, rect, border_radius = radius, width=width)

    def drawEndPanel(self):

        rect = pygame.rect.Rect(100, 200, self.game.size.width - 200, self.game.size.height - 400)
        self.drawPanel(self.colors[1], self.colors[2], rect, 20, 4)

        pos = self.game.center
        pos.y -= 70
        self.drawText(" GAME OWER ", self.fonts[0], self.colors[3], pos, 1, 1)

        pos.y += 70
        text = str(self.game.score)
        self.drawText(" YOUR SCORE: " + text + " ", self.fonts[0], self.colors[3], pos, 1, 1)

        button_1 = pygame.rect.Rect(rect.left + 50, rect.bottom - 100, 200, 50)
        button_2 = pygame.rect.Rect(rect.right - 250, rect.bottom - 100, 200, 50)

        mouse = Input.MousePosition()

        color = self.colors[4]
        if pygame.Rect.collidepoint(button_1, mouse):
            color = self.colors[5]
            if not self.botton_ower1:
                self.botton_ower1 = True
                Helper.PlaySound("click.wav")
            if Input.MousePress():
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        else:
            if self.botton_ower1:
                self.botton_ower1 = False
                

        self.drawPanel(color, self.colors[2], button_1, 10, 2)
        text = " EXIT GAME "
        self.drawText(text, self.fonts[1],self.colors[3],pygame.Vector2(button_1.centerx, button_1.centery) ,1,1)

        color = self.colors[4]
        if pygame.Rect.collidepoint(button_2, mouse):
            color = self.colors[5]
            if not self.button_ower2:
                self.button_ower2 = True
                Helper.PlaySound("click.wav")
            if Input.MousePress():
                self.game.restart()
        else:
            if self.button_ower2:
                self.button_ower2 = False


        self.drawPanel(color, self.colors[2], button_2, 10, 2)
        text = " RESTART GAME "
        self.drawText(text, self.fonts[1],self.colors[3],pygame.Vector2(button_2.centerx, button_2.centery) ,1,1)

        