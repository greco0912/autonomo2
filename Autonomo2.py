import pygame
pygame.init()

pantalla = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("ATARI PONG JOSE FLORES")

ejecutando = True

paleta = pygame.Rect(50, 300, 10, 100)

paleta2 = pygame.Rect(940, 300, 10, 100)

pelota = pygame.Rect(500, 400, 10, 10)
#velocidad de pelota
vel_x = 3
vel_y = 3

clock = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill((255, 255, 255))

    #PALETA IZQUIERDA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta)
    #PALETA DERECHA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta2)
    #PELOTA
    pygame.draw.rect(pantalla, (0, 0, 0,), pelota)
    #Actualiza pantalla
    pygame.display.flip()
    


    #Limitar FPS
    clock.tick(60)

    #Movimiento Paleta Izquierda
    teclas = pygame.key.get_pressed()
    if teclas [pygame.K_w]:
        paleta.y -= 5

    if teclas[pygame.K_s]:
        paleta.y += 5

    #Limitar paleta izquiera
    if paleta.top < 0:
        paleta.top = 0
    
    if paleta.bottom > 800:
        paleta.bottom = 800

    #Movimiento Paleta Derecha
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_o]:
        paleta2.y -= 5

    if teclas[pygame.K_l]:
        paleta2.y += 5

    #Limitar paleta derecha
    if paleta2.top < 0:
        paleta2.top = 0
    
    if paleta2.bottom > 800:
        paleta2.bottom = 800

    #Velocidad de Pelota
    pelota.x += vel_x
    pelota.y += vel_y

    #Limitar Pelota arriba y abajo
    if pelota.top <= 0 or pelota.bottom >= 800:
        vel_y *= -1
        

    #Choque en Paleta o Paleta 2
    if pelota.colliderect(paleta) or pelota.colliderect(paleta2):
        vel_x *= -1


    
    
pygame.quit()
    



