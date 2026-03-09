import pygame
from time import sleep

pygame.mixer.init()

pygame.mixer.music.load('C:/Users/Cleyton/Documents/Github/Python/Estudos/Guanabara/python-exercises/Mundo1/fourth class/Stardew Valley OST - Stardew Valley Overture - Lewie G (youtube).mp3')

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    sleep(1)
    