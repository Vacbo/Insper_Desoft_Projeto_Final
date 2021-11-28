import pygame
import os
from config import *
from assets import * 
from musica1 import *
from sprites import *


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


state = INIT

#Jogo Oficial
while state != QUIT:
        
    if state == INIT:
        ## Variável para o ajuste de velocidade
        clock = pygame.time.Clock()
        #carregar assets
        assets = carrega_assets()

        player = bolinha_cinza(assets)

        #Criando Grupos de Sprites
        all_sprites = pygame.sprite.Group()
        bolinhas_vermelhas = pygame.sprite.Group()
        bolinhas_azuis = pygame.sprite.Group()
        all_bolinhas = pygame.sprite.Group()
        all_players = pygame.sprite.Group()
    
        clock.tick(FPS)
    
    
       
        
        window.fill(0,0,0)
        #window.blit(assets[''imagem de início''], init_rect)
    elif state == PLAY:

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
        #window.blit(assets[''imagem de instruções''], inst_rect)


    # window.fill((255,255,255))
    # bolinha_vermelha1.update()        
    # window.blit(bolinha_vermelha1.image,bolinha_vermelha1.rect)
    #if state == PLAY:
        # ----- Trata eventos
        #for event in pygame.event.get():
            # ----- Verifica consequências
            #if event.type == pygame.QUIT:
                #state = QUIT
            #if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                
            #if event.key == pygame.K_LEFT:

pygame.quit()