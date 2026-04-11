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

    #Movimiento Paleta Izquierda
    teclas = pygame.key.get_pressed()
    if teclas [pygame.K_w]:
        paleta.y -= 5

    if teclas[pygame.K_s]:
        paleta.y += 5

    #Movimiento Paleta Derecha
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_o]:
        paleta2.y -= 5

    if teclas[pygame.K_l]:
        paleta2.y += 5



    
    
pygame.quit()
    



