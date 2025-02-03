import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# Configurações da janela
largura = 960
altura = 540

#x e y vao controlar o movimento do objeto na tela (retangulo)
#x = 0
x = largura/2 #para ficar no meio da tela
#y = 0
y = altura/2

#Recebe uma tupla para largura e altura da tela
tela = pygame.display.set_mode((largura, altura))

#Colocando o nome da Janela do Jogo
pygame.display.set_caption('Jogo')

#Melhor jeito de controlar a velocidade de movimentos
clock = pygame.time.Clock()

#Loop principal do jogo, o jogo atualiza a cada segundo jogando
while True:
    
    #Usando o clock   +frame + rapido, - frame - rapido
    clock.tick(60) #60 frames por segundo
    
    #Faremos algo para "limpar a tela a cada atualização do jogo"
    tela.fill((0,0,0)) #RGB, preto
    
    #o proximo loop captura os eventos (ações do jogador) a cada momento do jogo
    for event in pygame.event.get():
        
        #Aqui esta capturando o evento de sair do jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        '''
        #Movimentar o objeto
        if event.type == KEYDOWN:
            
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_s:
                y += 20
            if event.key == K_w:
                y -= 20
        '''
        
    #Movimentar segurando a tecla    
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_s]:
        y += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    
    
    #Para colocar em movimento vamos substiruir por x e y que podem variar
    pygame.draw.rect(tela,(255,0,0), (x, y,40,50))
    
    ''' Fazer mexer sozinho
    if y >= altura:
        y = 0
    y += 1
    '''
    #y += 0.5 -> faz o objeto se mover em uma determinada velocidade, >1 mais rapido, <1 mais lento.
    
    
    
    #A cada interação do jogo ela atualiza a tela do jogo, para rodar sempre, ate fechar o jogo.
    pygame.display.update()
    
    

    '''
    usamos o plano cartesiano para definir os desenhos. No pygame o eixo y cresce para baixo, o x se mantem normal.
    #colocar objeto na tela pega o RGB de cor, de 0 a 250, e a posição do objeto na tela, x e y.
    #Dentro de uma tupla, que é um conjunto de dados, que não pode ser alterado.
    '''
    
    '''
    #recebe a tela. a cor do objeto, e a posição do objeto na tela, (x, y, largura altura).     
    
    pygame.draw.rect(tela,(255,0,0), (200, 300,40,50))
    
    #fazer um circulo agr, com o 40 representando o raio do circulo (ultimo parametro da tupla)
    
    pygame.draw.circle(tela, (0,255,0), (300, 260), 40)
    
    #fazer uma linha, com a cor, e a posição inicial e final da linha
    
    pygame.draw.line(tela, (0,0,255), (390, 0), (360, 600), 5) #5 é a espessura da reta
    '''