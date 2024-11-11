import pygame
import os

def AssetPath(assetName: str):
    return os.path.join('Assets', assetName)

def LoadImage(imageName: str):
    return pygame.image.load(AssetPath(imageName))

sound_list = {}
def PlaySound(soundName: str):
    if soundName not in sound_list:
        sound_list[soundName] = pygame.mixer.Sound(AssetPath(soundName))

    pygame.mixer.Sound.play(sound_list[soundName])

