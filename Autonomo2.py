import pygame #Libreria Pygame de Python que me permite crear el juego, manejar gráficos, teclado y animaciones
pygame.init() #Inicializo Pygame para poder usar todas sus funciones como ventana, sonido y controles

pantalla = pygame.display.set_mode((1000, 800)) #Creo la ventana del juego con un tamaño de 1000 por 800 píxeles
pygame.display.set_caption("ATARI PONG JOSE FLORES") #Asigno un título a la ventana para identificar el juego

ejecutando = True #Creo una variable booleana que controla el bucle principal del juego. Mientras sea verdadera, el juego seguirá ejecutándose

paleta = pygame.Rect(50, 300, 10, 100)

paleta2 = pygame.Rect(940, 300, 10, 100) 

aumento_de_velocidad = 0

puntos1 = 0 #Jugador Izquierdo
puntos2 = 0 #Jugador Derecha

#Creo las paleta como un rectángulo, definiendo su posición y tamaño en pantalla. (x posicion horizontal, y posicion vertical, ancho y alto)

pelota = pygame.Rect(500, 400, 10, 10) #Creo la pelota en el centro de la pantalla con un tamaño de 10 por 10
#velocidad de pelota
vel_x = 3
vel_y = 3 #Defino la velocidad de la pelota en los ejes X y Y, lo que permitirá que se mueva en diagonal

clock = pygame.time.Clock() #Creo un objeto clock que me permite controlar la velocidad del juego, es decir, los FPS

fuente = pygame.font.Font(None, 50) #fuente para crea puntaje 

while ejecutando: #Inicio el bucle principal, que se ejecuta continuamente mientras la variable ‘ejecutando’ sea verdadera
    for evento in pygame.event.get(): #Recorro todos los eventos que ocurren en el juego, como presionar teclas o cerrar la ventana
        if evento.type == pygame.QUIT:
            ejecutando = False #Si el usuario cierra la ventana, cambio la variable ejecutando a falso para salir del bucle

    pantalla.fill((255, 255, 255)) #Limpio la pantalla pintándola de blanco para evitar que queden rastros de los objetos

    texto = fuente.render(f"{puntos1}  -  {puntos2}", True, (0, 0, 0)) #fuente

    #PALETA IZQUIERDA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta)
    #PALETA DERECHA
    pygame.draw.rect(pantalla, (0, 0, 0), paleta2)
    #PELOTA
    pygame.draw.rect(pantalla, (0, 0, 0,), pelota) #Dibujo en pantalla las paletas y la pelota usando rectángulos de color negro
    #Actualiza pantalla

    pantalla.blit(texto, (450, 50)) #Dibujar en pantalla

    pygame.display.flip() #Actualizo la pantalla para mostrar los cambios realizados en cada ciclo
    


    #Limitar FPS
    clock.tick(60) #Limito el juego a 60 fotogramas por segundo para que funcione de forma fluida

    #Movimiento Paleta Izquierda
    teclas = pygame.key.get_pressed() #Obtengo el estado del teclado para saber qué teclas están siendo presionadas.
    if teclas [pygame.K_w]:
        paleta.y -= 5 + aumento_de_velocidad

    if teclas[pygame.K_s]: #Muevo la paleta izquierda hacia arriba o abajo dependiendo de las teclas presionadas
        paleta.y += 5 + aumento_de_velocidad

    #Limitar paleta izquiera
    if paleta.top < 0:
        paleta.top = 0
    
    if paleta.bottom > 800:
        paleta.bottom = 800 #Restringo el movimiento para que la paleta no salga de los límites de la pantalla

    #Movimiento Paleta Derecha
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_o]:
        paleta2.y -= 5 + aumento_de_velocidad

    if teclas[pygame.K_l]: #Controlo la paleta derecha con otras teclas para el segundo jugador
        paleta2.y += 5 + aumento_de_velocidad

    #Limitar paleta derecha
    if paleta2.top < 0:
        paleta2.top = 0
    
    if paleta2.bottom > 800:
        paleta2.bottom = 800

    #Velocidad de Pelota #Actualizo la posición de la pelota sumando su velocidad en los ejes X y Y.
    pelota.x += vel_x
    pelota.y += vel_y

    #Limitar Pelota arriba y abajo, Si la pelota toca los bordes superior o inferior, invierto su dirección vertical para simular un rebote
    if pelota.top <= 0 or pelota.bottom >= 800:
        vel_y *= -1
        

    #Choque en Paleta o Paleta 2, Si la pelota colisiona con alguna paleta, invierto su dirección horizontal
    if pelota.colliderect(paleta) or pelota.colliderect(paleta2):
        vel_x *= -1.10
        vel_y *=  1.10
        aumento_de_velocidad += 0.5

    if abs(vel_x) > 10:
        vel_x = 10 if vel_x > 0 else -20
        vel_y = 10 if vel_y > 0 else -20

    if pelota.left <= 0:
        puntos2 += 1
        pelota.x = 500
        pelota.y = 400
        vel_x = 3
        vel_y = 3
        aumento_de_velocidad = 0


    if pelota.right >= 1000:
        puntos1 += 1
        pelota.x = 500
        pelota.y = 400
        vel_x = -3
        vel_y = 3
        aumento_de_velocidad = 0

    if puntos1 == 5:
        print("Jugador 1 gana")

    if puntos2 == 5:
        print("Jugador 2 gana")
     
      


    



    
    
pygame.quit() #Al salir del bucle, cierro correctamente Pygame
    



