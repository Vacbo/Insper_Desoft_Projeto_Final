import pygame
import os
from config import *
from assets import * 
from musica1 import *

#Inicia o jogo
pygame.init()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Taiko no Chi')

#funcão que recebe qual bolinha deve ser pressionada e devolve o tempo que a bolinha tem que ser criada
def Timing(tempo_de_duracao):
    tempo_de_duracao=int(tempo_de_duracao)
    tempo_para_criar_bolinha=tempo_de_duracao-1585
    return tempo_para_criar_bolinha

# ----- Inicia estruturas de dados
# Definindo os novos tipos


game= True
## Variável para o ajuste de velocidade
clock = pygame.time.Clock()
#carregar assets
assets = carrega_assets()

#Criando Grupos de Sprites
all_sprites = pygame.sprite.Group()
bolinhas_vermelhas = pygame.sprite.Group()
bolinhas_azuis = pygame.sprite.Group()
all_bolinhas = pygame.sprite.Group()
all_players = pygame.sprite.Group()
#Criando o hitbox do player
for i in range(2):
    player=BolinhaPlayer(sprites['bolinha3'])
    all_sprites.add(player)
    all_players.add(player)
#Criando hitbox dos 'inimigos'
for i in range(2):
    bolinha_vermelha1=Bolinha(sprites['bolinha1'])
    all_sprites.add(bolinha_vermelha1)
    all_bolinhas.add(bolinha_vermelha1)

for i in range(2):
    bolinha_azul1=Bolinha(sprites['bolinha1'])
    all_sprites.add(bolinha_azul1)
    all_bolinhas.add(bolinha_azul1)


state = INIT

#Jogo Oficial
while state != QUIT:
    clock.tick(FPS)

    if state == INIT:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = INSTRUCTIONS
        
        window.fill(0,0,0)
        window.blit(assets[''imagem de início''], init_rect)

    #Tela de instruções
    if state == INSTRUCTIONS:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = PLAY

        window.fill(0,0,0)
        window.blit(assets[''imagem de instruções''], inst_rect)


    # window.fill((255,255,255))
    # bolinha_vermelha1.update()        
    # window.blit(bolinha_vermelha1.image,bolinha_vermelha1.rect)
    if state == PLAY:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                
                if event.key == pygame.K_LEFT:

hits=

                pygame.quit()