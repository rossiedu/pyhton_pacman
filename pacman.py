# Importando e inicializando a bilbioteca
import pygame
pygame.init()


# Declarando as variaveis
## Variaveis de tela
height = 480
width = 640
## Variaveis do pacman
yellow = (255,255,0)
black = (0,0,0)
radius = 30
x = 10
y = 10
velocity = 0.3
velocity_x = velocity
velocity_y = velocity

## Definindo o tamanho da janela do jogo (largura, altura)
tela = pygame.display.set_mode((width,height),0)

# Criando um looping para que a janela fique aberta até ser fechada
while True:
    # Regras
    x += velocity_x
    y += velocity_y

    if x + radius > width:
        velocity_x = -velocity
    if x - radius < 0:
        velocity_x = velocity
    if y + radius > height:
        velocity_y = -velocity
    if y - radius  < 0:
        velocity_y = velocity

    # Cores
    ## Pintando a tela de preto
    tela.fill(black)
    ## Desenhando o pacman
    pygame.draw.circle(
        surface = tela,
        color = yellow,
        center = (int(x),int(y)),
        radius = radius,
        width = 0
    )
    pygame.display.update()
    # Eventos
    ## Sair do loop quando o usuario clicar no fechar a janela
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()