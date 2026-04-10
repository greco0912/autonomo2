import pygame
pygame.init()

pantalla = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("ATARI PONG JOSE FLORES")

ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((255,255,255))


    
    
pygame.quit()
    



