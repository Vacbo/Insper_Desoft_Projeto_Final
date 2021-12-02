from os import path

#Determinando o path (diretorio) de cada elemento 
SPRITES_PATH = path.join(path.dirname(__file__), 'assets', 'sprites')
SOUND_PATH = path.join(path.dirname(__file__), 'assets', 'sounds')
FONT_PATH = path.join(path.dirname(__file__), 'assets', 'fonts')
ANIMATIONS_PATH = path.join(path.dirname(__file__),'assets', 'animations')

#Variaveis Gerais
WIDTH=1280
HEIGHT=720
FPS=60

#Tamanho dos circulos
bolinha_width=82
bolinha_height=82

#Tamanho da score line
score_line_height=116

INIT=0
INSTRUCTIONS=1
PLAY=2
QUIT=3
CREDITS=4
