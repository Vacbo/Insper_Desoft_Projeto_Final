import pygame
import os
from config import *
from assets import * 
from musica1 import *
from sprites import *


#Inicia o jogo
pygame.init()
pygame.mixer.init()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Taiko no Chi')
pygame.mixer.music.set_volume(0.4)

#funcão que recebe qual bolinha deve ser pressionada e devolve o tempo que a bolinha tem que ser criada
def Timing_azul(tempo_de_duracao):
    tempo_de_duracao=int(tempo_de_duracao)
    tempo_para_criar_bolinha=tempo_de_duracao-1585
    return tempo_para_criar_bolinha
    
def Timing_vermelha(tempo_de_duracao):
    tempo_de_duracao=int(tempo_de_duracao)
    tempo_para_criar_bolinha=tempo_de_duracao-1585
    return tempo_para_criar_bolinha
# ----- Inicia estruturas de dados
# Definindo os novos tipos

assets = carrega_assets()

#Criando Grupos de Sprites
all_sprites = pygame.sprite.Group()
bolinhas_vermelhas = pygame.sprite.Group()
bolinhas_azuis = pygame.sprite.Group()
all_bolinhas = pygame.sprite.Group()
all_players = pygame.sprite.Group()

groups = {}
groups['bolinhas_vermelhas'] = bolinhas_vermelhas
groups['bolinhas_azuis'] = bolinhas_azuis
groups['all_bolinhas'] = all_bolinhas
groups['all_players'] = all_players

player1 = bolinha_cinza(assets)
player2 = bolinha_cinza(assets)
inimigo1 = bolinha_azul(assets)
inimigo2 = bolinha_vermelha(assets)

all_sprites.add(player1)
all_players.add(player1)
all_sprites.add(player2)
all_players.add(player2)

for i in range(2):
    all_sprites.add(inimigo1)
    bolinhas_azuis.add(inimigo1)

for i in range(2):
    all_sprites.add(inimigo2)
    bolinhas_vermelhas.add(inimigo2)

keys_down = {}

score = 0

game = True


init_rect = assets['menu'].get_rect()
init_count = 0

state = INIT


#Jogo Oficial
while state != QUIT:
        
    if state == INIT:
        ## Variável para o ajuste de velocidade
        clock = pygame.time.Clock()

        clock.tick(FPS)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    state = PLAY
                if event.key == pygame.K_x:
                    state = INSTRUCTIONS
                if event.key == pygame.K_c:
                    state = CREDITS

        window.blit(assets['menu'], init_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    #Tela de instruções
    if state == INSTRUCTIONS:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = INIT
        window.blit(assets['HTP'], init_rect)
        pygame.display.flip()

    if state == CREDITS:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = INIT
        window.blit(assets['credits'], init_rect)
        pygame.display.flip()

    if state == PLAY:
            # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
            if event.type == pygame.KEYDOWN:
                #Verifica o player a ser selecionado, player1 interaje com bolinha azul e player2 com bolinha vermelha
                if event.key == pygame.K_d or event.key == pygame.K_k:
                    all_sprites.add(player1)
                if event.key == pygame.K_f or event.key == pygame.K_j:
                    all_sprites.add(player2)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_k:
                    all_sprites.remove(player1)
                if event.key == pygame.K_f or event.key == pygame.K_j:
                    all_sprites.remove(player2)

        hits = pygame.sprite.spritecollide(player1, bolinhas_azuis, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            score += 10
        hits = pygame.sprite.spritecollide(player2, bolinhas_vermelhas, True, pygame.sprite.collide_mask)
        if len(hits) == 1:
            score += 10
        if clock == 57600:
            if score > 258:
                text_surface1 = assets['score_font'].render("VOCÊ GANHOU", True, (50, 255, 255))
            else:
                text_surface1 = assets['score_font'].render("VOCÊ PERDEU", True, (50, 255, 255))

            # ----- Gera saídas
        window.blit(assets['background'],(0,0))

        text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)

        window.blit(text_surface, text_rect)
        all_sprites.draw(window)
        all_sprites.update()

        # ----- Atualiza estado do jogo
        pygame.display.flip()

pygame.quit()