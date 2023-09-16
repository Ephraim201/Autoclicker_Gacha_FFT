import pygame

# Inicializa pygame
pygame.init()

# Crea una ventana (puede ser invisible)
pygame.display.set_mode((1, 1))

# Carga el sonido
sonido = pygame.mixer.Sound("sound\\LVUp.wav")

# Función para reproducir el sonido en segundo plano
def reproducir_sonido():
    sonido.play()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Puedes cambiar esto a la tecla que quieras
                reproducir_sonido()
