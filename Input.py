import pygame

def Axis():
    keys = pygame.key.get_pressed()

    axis = pygame.Vector2(axisX(keys),axisY(keys))

    if axis.x != 0 or axis.y != 0:
        axis = axis.normalize()

    return axis
    

def axisY(keys):
    key = 0
    if keys[pygame.K_w]:
        key -= 1
    if keys[pygame.K_s]:
        key += 1

    return key


def axisX(keys):
    key = 0
    if keys[pygame.K_a]:
        key -= 1
    if keys[pygame.K_d]:
        key += 1

    return key

def MousePress():
    return pygame.mouse.get_pressed()[0]

def MousePosition():
    return pygame.Vector2(pygame.mouse.get_pos())
