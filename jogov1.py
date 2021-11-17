from pygame import *
import pygame

init()
window=display.set_mode((1280,720))
display.set_caption('Taiko no Chi')

game= True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    
    window.fill((255,255,255))
    pygame.display.update()


pygame.quit()