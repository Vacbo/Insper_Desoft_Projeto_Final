import pygame
from config import *

#definindo uma classe para cada tipo de bolinha
class bolinha_vermelha(pygame.sprite.Sprite):
    def __init__(self, assets):
        # definindo variavel que registrar o tempo
        self.last_timing = 0
        #registra o timing do presente
        self.timing_atual = pygame.time.get_ticks() 
        self.estado = False
        
        #Classe mãe
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets 
        self.image= assets['vermelho']
        self.rect = self.image.get_rect()
        self.rect.x = -bolinha_width
        self.rect.y = HEIGHT/2
        self.speedx = -3
    
    def update(self, assets):
        #Bolinha movimentando
        self.rect.x +=self.speedx
        
        #quando a bolnha estiver perto da bolinha cinza o jogador ja pode apertar
        if self.rect.centerx >=WIDTH/3-1.15*bolinha_width:
            self.estado = True
        
        #bolinha para quando chegar no centro da bolinha cinza
        if self.rect.centerx  >= WIDTH/2-1.05*bolinha_width:
            self.speedx = 0
            self.last_timing= pygame.time.get_ticks()
        
        #se o jogador demorar muito ele erra
        if self.last_timing-self.timing_atual >1800:
            self.estado = False
            self.kill()
            #sound effect de miss
            #assets['miss'].play()






class Bolinha(sprite.Sprite):
    
    def update(self):
        # Atualizando a posição do bolinha
        self.rect.x += self.speedx
        # Se a bolinha passar do final da tela, some
        ''' if self.rect.left > 1280:
            self.remove()'''

class BolinhaPlayer(sprite.Sprite):
    def __init__(self,img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.imgs=[]
        self.imgs.append(pygame.image.load('sprites/input_judge.png').convert_alpha())
        self.image=pygame.sprites['bolinha3']
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.image.get_rect()
        self.rect.x=350
        self.rect.y=310