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
    tempo_para_criar_bolinha=tempo_de_duracao-14400
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
move_lines = pygame.sprite.Group()

groups = {}
groups['bolinhas_vermelhas'] = bolinhas_vermelhas
groups['bolinhas_azuis'] = bolinhas_azuis
groups['all_bolinhas'] = all_bolinhas
groups['all_players'] = all_players

player1 = bolinha_cinza(assets)
player2 = bolinha_cinza(assets)
inimigo1 = bolinha_azul(assets)
inimigo2 = bolinha_vermelha(assets)
move_line = Move_line(assets)

all_sprites.add(player1)
all_players.add(player1)
all_sprites.add(player2)
all_players.add(player2)
move_lines.add(move_line)

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
        dic_player=timing_player_musica_1()
        score = 0


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

        pygame.mixer.music.play()
        running=True
        while running:
            hitbox1 = False
            hitbox2 = False

            clock.tick(FPS)    
            #Contador de tempo decorrido
            tempo_da_musica = pygame.mixer.music.get_pos()
            for timing in dic_player:
                timing_v=Timing_vermelha(timing)
                if tempo_da_musica >= timing_v:
                    if dic_player[timing] == 'vermelho':
                        bv=bolinha_vermelha(assets)
                        all_bolinhas.add(bv)
                        bolinhas_vermelhas.add(bv)
                        all_sprites.add(bv)
                    
                    elif dic_player[timing] == 'azul':
                        ba=bolinha_azul(assets)
                        all_bolinhas.add(ba)
                        bolinhas_azuis.add(ba)
                        all_sprites.add(ba)
                        # para evitar erros  
                    
                    dic_player[timing]='n repete'
            
            clock.tick(FPS)
            
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    state = QUIT
                    running = False

                if event.type == pygame.KEYDOWN:
                    keys_down[event.key] = True
                    #Verifica o player a ser selecionado, player1 interaje com bolinha azul e player2 com bolinha vermelha
                    if event.key == pygame.K_d or event.key == pygame.K_k:
                        hitbox1 =True

                    if event.key == pygame.K_f or event.key == pygame.K_j:
                        hitbox2 =True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d or event.key == pygame.K_k:
                        hitbox1 =False

                    if event.key == pygame.K_f or event.key == pygame.K_j:
                        hitbox2 =False

            text_surface1 =  assets['score_font'].render("TAIKO NO CHI", True, (0, 255, 255))
            text_rect1 = text_surface1.get_rect()
            text_rect1.midtop = (WIDTH / 2,  10)
            if hitbox1:
                explosion_b = Explosion_b(player1.rect.center, assets)
                all_sprites.add(explosion_b)
                hits = pygame.sprite.spritecollide(player1, bolinhas_azuis, True)
                if len(hits) == 1:
                    score += 10
                if len(hits) > 1:
                    score +=20  
            if hitbox2:
                explosion_r = Explosion_r(player2.rect.center, assets)
                all_sprites.add(explosion_r)
                hits = pygame.sprite.spritecollide(player2, bolinhas_vermelhas, True)
                if len(hits) == 1:
                    score += 10
            if tempo_da_musica > 45600:
                if score > 258:
                    text_surface1 = assets['score_font'].render("VOCE GANHOU", True, (0, 255, 255))
                    text_rect = text_surface1.get_rect()
                    text_rect.midtop = (WIDTH / 2,  10)
                else:
                    text_surface1 = assets['score_font'].render("VOCE PERDEU", True, (0, 255, 255))
                    text_rect = text_surface1.get_rect()
                    text_rect.midtop = (WIDTH / 2,  10)
            if tempo_da_musica > 48500:
                pygame.mixer.music.stop()
                running = False
                state = INIT
                # ----- Gera saídas

            text_surface = assets['score_font'].render("Pontos:{:01d}".format(score), True, (0, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = ((WIDTH-150)+20,  10)

            all_sprites.update(assets)
            window.fill((0, 0, 255))
            window.blit(assets['background'],(0,0))
            window.blit(text_surface, text_rect)
            window.blit(text_surface1, text_rect1)

            move_lines.draw(window)
            all_sprites.draw(window)
            pygame.display.update()  # Mostra o novo frame para o jogador
            clock.tick(FPS)



            # ----- Atualiza estado do jogo


pygame.quit()