import pygame
pygame.init()

pantalla = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("ATARI PONG JOSE FLORES")

ejecutando = True

paleta = pygame.Rect(50, 300, 10, 100)

paleta2 = pygame.Rect(940, 300, 10, 100)

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((255, 255, 255))

    #PALETA IZQUIERDA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta)
    #PALETA DERECHA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta2)
    pygame.display.flip()



    
    
pygame.quit()
    



