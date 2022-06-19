# Importando e inicializando a bilbioteca
import pygame
pygame.init()

yellow = (255,255,0)
# Definindo o tamanho da janela do jogo (altura, largura)
tela = pygame.display.set_mode((640,480),0)

# Criando um looping para que a janela fique aberta até ser fechada
while True:
    # Regras
    # Cores
    pygame.draw.circle(
        surface = tela,
        color = yellow,
        center = (320,240),
        radius = 50,
        width = 0
    )
    pygame.display.update()
    # Eventos
    ## Sair do loop quando o usuario clicar no fechar a janela
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
