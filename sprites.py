import pygame
from config import *

#definindo uma classe para cada tipo de bolinha
class bolinha_vermelha(pygame.sprite.Sprite):
    def __init__(self, assets):
        #Classe mãe
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets 
        self.image= assets['vermelho']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH+(bolinha_width/2)
        self.rect.centery = HEIGHT/2
        self.speedx = 30
        self.speedy = 3
    
    def update(self,assets):
        #Bolinha movimentando
        self.rect.x -= self.speedx


class bolinha_azul(pygame.sprite.Sprite):
    def __init__(self, assets):
        #Classe mãe
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets 
        self.image= assets['azul']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH+(bolinha_width/2)
        self.rect.centery = HEIGHT/2
        self.speedx = 30
        self.speedy = 3
    
    def update(self,assets):
        #Bolinha movimentando
        self.rect.x -= self.speedx


class bolinha_cinza(pygame.sprite.Sprite):
    def __init__(self,assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets['cinza']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/3+bolinha_width
        self.rect.centery = HEIGHT/2