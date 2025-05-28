import pygame
import sys
import math
import random

# Inicializar Pygame
pygame.init()

# Configurar la pantalla en modo de pantalla completa
screen_width, screen_height = 1200, 600  # Cambiar el ancho a 1200
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption('Dedicatoria Motivadora con Girasoles')

# Colores
green_background = (0, 128, 0)  # Fondo verde
black = (0, 0, 0)
red = (255, 0, 0)  # Color para la palabra "ZULMA"
yellow = (255, 255, 0)  # Color de los pétalos de los girasoles
brown = (139, 69, 19)  # Color del centro de los girasoles
purple = (128, 0, 128)  # Color morado para el texto final
blue = (0, 0, 255)  # Color azul para el título "Para ti"
white = (255, 255, 255)  # Color blanco para el texto del botón

# Fuente
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
final_font = pygame.font.Font(None, 50)  # Fuente más grande para el mensaje final
gusto_font = pygame.font.Font(None, 40)  # Fuente para el nuevo mensaje

# Mensajes
title_message = "Para ti"  # Título agregado
main_message = "ZULMA"  # Texto animado
biblical_message1 = "Encomienda al Señor tu camino; confía en él, y él actuará.(Salmo 37:5)"
biblical_message2 = " No se turbe vuestro corazón; creéis en Dios, creed también en mí(juan14,1)"
motivational_message1 = "Sigue adelante, cada esfuerzo vale la pena."
motivational_message2 = "El éxito es la suma de pequeños esfuerzos repetidos día tras día."
friend_message1 = "Un verdadero amigo es como una estrella, siempre está ahí."
friend_message2 = "Eres la razón por la que sonrío todos los días."
romantic_message1 = "Desde que te conocí, mi vida tiene un nuevo sentido."
romantic_message2 = "Tu amistad es el tesoro más valioso que he encontrado."
romantic_message3 = "Cada día a tu lado es una bendición que agradezco."
final_message = "FELIZ SEMANA AMIGA: UN ABRAZO"  # Texto final agregado
gusto_message = "FUE UN GUSTO CONOCERTE"  # Nuevo mensaje agregado

# Función para dibujar un girasol
def draw_sunflower(surface, center, size):
    # Dibujar pétalos
    for angle in range(0, 360, 30):  # Más pétalos para parecer girasol
        petal_x = center[0] + int(size * math.cos(math.radians(angle)))
        petal_y = center[1] + int(size * math.sin(math.radians(angle)))
        pygame.draw.circle(surface, yellow, (petal_x, petal_y), size // 2)

    # Dibujar el centro del girasol
    pygame.draw.circle(surface, brown, center, size // 3)

# Crear una clase para los girasoles en movimiento
class MovingSunflower:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.size = random.randint(20, 40)
        self.speed = random.uniform(1, 3)  # Velocidad flotante para mayor variación

    def move(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = -self.size
            self.x = random.randint(0, screen_width)

    def draw(self, surface):
        draw_sunflower(surface, (self.x, self.y), self.size)

# Crear una lista de girasoles en movimiento
sunflowers = [MovingSunflower() for _ in range(20)]

# Crear un botón para salir del modo de pantalla completa
def draw_exit_button(surface):
    button_rect = pygame.Rect(screen_width - 120, 20, 100, 50)
    pygame.draw.rect(surface, black, button_rect)
    button_text = small_font.render("Salir", True, white)  # Texto del botón en blanco
    surface.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2, button_rect.y + (button_rect.height - button_text.get_height()) // 2))

# Bucle principal
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en el botón de salir
            if event.button == 1:  # Botón izquierdo del ratón
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(screen_width - 120, 20, 100, 50)
                if button_rect.collidepoint(mouse_pos):
                    # Cambiar a modo ventana
                    screen = pygame.display.set_mode((screen_width, screen_height))  # Cambiar a modo ventana
                    pygame.display.set_caption('Dedicatoria Motivadora con Girasoles')  # Cambiar título
                    running = False  # Salir del bucle

    screen.fill(green_background)  # Fondo verde

    # Mover y dibujar los girasoles en movimiento
    for sunflower in sunflowers:
        sunflower.move()
        sunflower.draw(screen)

    # Renderizar los mensajes
    title_text = font.render(title_message, True, blue)  # "Para ti" en azul
    main_text = font.render(main_message, True, red)  # "ZULMA" en rojo
    biblical_text1 = small_font.render(biblical_message1, True, black)
    biblical_text2 = small_font.render(biblical_message2, True, black)
    motivational_text1 = small_font.render(motivational_message1, True, black)
    motivational_text2 = small_font.render(motivational_message2, True, black)
    friend_text1 = small_font.render(friend_message1, True, black)
    friend_text2 = small_font.render(friend_message2, True, black)
    romantic_text1 = small_font.render(romantic_message1, True, black)
    romantic_text2 = small_font.render(romantic_message2, True, black)
    romantic_text3 = small_font.render(romantic_message3, True, black)
    final_text = final_font.render(final_message, True, purple)  # Texto final en morado, ahora más grande
    gusto_text = gusto_font.render(gusto_message, True, blue)  # Nuevo mensaje en azul

    # Posicionar los mensajes
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))  # Título "Para ti"
    screen.blit(biblical_text1, (screen_width // 2 - biblical_text1.get_width() // 2, 150))
    screen.blit(biblical_text2, (screen_width // 2 - biblical_text2.get_width() // 2, 200))
    screen.blit(motivational_text1, (screen_width // 2 - motivational_text1.get_width() // 2, 250))
    screen.blit(motivational_text2, (screen_width // 2 - motivational_text2.get_width() // 2, 300))
    screen.blit(friend_text1, (screen_width // 2 - friend_text1.get_width() // 2, 350))  # Frase de amigo 1
    screen.blit(friend_text2, (screen_width // 2 - friend_text2.get_width() // 2, 400))  # Frase de amigo 2
    screen.blit(romantic_text1, (screen_width // 2 - romantic_text1.get_width() // 2, 450))  # Frase romántica 1
    screen.blit(romantic_text2, (screen_width // 2 - romantic_text2.get_width() // 2, 500))  # Frase romántica 2
    screen.blit(romantic_text3, (screen_width // 2 - romantic_text3.get_width() // 2, 550))  # Frase romántica 3
    screen.blit(final_text, (screen_width // 2 - final_text.get_width() // 2, 620))  # Texto final en morado, más abajo
    screen.blit(gusto_text, (screen_width // 2 - gusto_text.get_width() // 2, 670))  # Nuevo mensaje en azul

    # Dibujar el botón de salir
    draw_exit_button(screen)

    # Animar el texto principal ("ZULMA")
    animated_x = screen_width // 2 + 100 * math.sin(math.radians(angle))
    screen.blit(main_text, (animated_x - main_text.get_width() // 2, screen_height // 2 - main_text.get_height() // 2))
    angle += 5  # Incrementar el ángulo para la animación

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()

