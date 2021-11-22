from pygame import *
import pygame

init()
window=display.set_mode((1280,720))
display.set_caption('Taiko no Chi')

sprites = {}
sprites['bolinha1'] = pygame.image.load('sprites/input_b.png')
sprites['bolinha2'] = pygame.image.load('sprites/input_r.png')
sprites['bolinha2']=pygame.transform.scale(sprites['bolinha2'],(82,82))
sprites['bolinha3'] = pygame.image.load('sprites/input_judge.png')
sprites['linha'] = pygame.image.load('sprites/move_line.png')
# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Bolinha(sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        sprite.Sprite.__init__(self)
        self.imgs=[]
        self.imgs.append(image.load('sprites/input_r.png').convert_alpha())
        self.image=sprites['bolinha2']
        self.mask=mask.from_surface(self.image)
        self.rect=self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 310
        self.speedx = -5
    def update(self):
        # Atualizando a posição do bolinha
        self.rect.x += self.speedx
        # Se a bolinha passar do final da tela, some
        ''' if self.rect.left > 1280:
            self.remove()'''

game= True
## Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

#Criando as bolinhas
bolinha_vermelha1=Bolinha(sprites['bolinha2'])

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
    window.fill((255,255,255))
    bolinha_vermelha1.update()        
    window.blit(bolinha_vermelha1.image,bolinha_vermelha1.rect)
    pygame.display.update()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f or event.key == pygame.K_j:
            

        if event.key == pygame.K_d or event.key == pygame.K_k:



pygame.quit()