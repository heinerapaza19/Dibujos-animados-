from turtle import *
import colorsys
import math
import random

# Configuraciones iniciales
speed(0)  # Velocidad máxima para un dibujo rápido

bgcolor("lightblue")  # Fondo azul claro

# Posición inicial para la flor
penup()
goto(0, -150)  # Ajustamos la posición inicial para tener más espacio para la flor
pendown()

# Lista de colores personalizados para los pétalos
colores_petalos = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Número de pétalos y capas por pétalo
n_petalos = 20
n_capas = 12

# Dibujo de pétalos con colores personalizados
for i in range(n_petalos):
    color(random.choice(colores_petalos))  # Escoge un color aleatorio para cada pétalo
    for j in range(n_capas):
        rt(90)
        circle(250 - j * 10, 90)  # Aumentamos el tamaño de los pétalos
        lt(90)
        circle(250 - j * 10, 90)
        rt(180)
    circle(80, 360 / n_petalos)  # Ajustamos el tamaño del círculo entre pétalos

# Dibujo de la parte central (girasol con espiral)
penup()
goto(0, 0)  # Reposiciona al centro de la flor
pendown()

color("black")
shape("turtle")
fillcolor("brown")

# Parámetro para calcular la espiral
phi = 137.508 * (math.pi / 160.0)

# Dibujo del espiral centrado
for i in range(200):  # Aumentamos la cantidad de espiral para que cubra más espacio
    r = 8 * math.sqrt(i)  # Aumentamos el tamaño de la espiral
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    # Coloca la tortuga en la posición calculada
    penup()
    goto(x, y)  # El espiral comienza en el centro (0, 0)
    pendown()
    
    # Sello de la tortuga
    stamp()

# Función para dibujar un corazón
def dibujar_corazon(x, y, color_corazon):
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    color(color_corazon)
    begin_fill()
    left(50)
    forward(40)  # Tamaño del corazón
    circle(20, 200)
    right(140)
    circle(20, 200)
    forward(40)
    end_fill()
    right(50)  # Regresar a la orientación original

# Dibujo de lluvia de corazones
num_corazones = 20
for _ in range(num_corazones):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color_corazon = random.choice(["red", "pink", "purple", "yellow"])
    dibujar_corazon(x, y, color_corazon)

# Escribir texto debajo del dibujo
penup()
goto(0, -750)  # Posición del texto
color("black")
write("Lida", align="center", font=("Arial", 16, "bold"))
penup()
goto(0, -380)  # Ajustar la posición del texto
write("Fue un placer conocerte", align="center", font=("Arial", 16, "bold"))
penup()
goto(0, -610)  # Añadir otro texto más abajo
write("Me gustas mucho", align="center", font=("Arial", 16, "bold"))
penup()
goto(0, 450)  # Ajustar la posición para el texto "DE HEINER"
color("red")
write("DE HEINER", align="center", font=("Arial", 18, "bold"))

# Actualizar la pantalla una vez que se ha terminado el dibujo
tracer(1, 0)

# Esconder la tortuga
hideturtle()

done()