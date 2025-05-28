import turtle
import random

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Árbol de Navidad")

# Función para dibujar el tronco
def draw_trunk(t):
    t.penup()
    t.goto(-15, -200)
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

# Función para dibujar una sección del árbol
def draw_tree_section(t, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.color("forest green")
    t.begin_fill()
    t.pendown()
    t.goto(x + width / 2, y + height)
    t.goto(x + width, y)
    t.goto(x, y)
    t.end_fill()

# Función para dibujar luces
def draw_light(x, y):
    light = turtle.Turtle()
    light.hideturtle()
    light.penup()
    light.goto(x, y)
    light.shape("circle")
    light.shapesize(0.5)
    light.color(random.choice(["red", "yellow", "blue", "white", "pink", "purple"]))
    light.showturtle()

# Función para mostrar frases navideñas
def show_message():
    phrases = [
        "¡Feliz Navidad y Próspero Año Nuevo!",
        "Que la magia de la Navidad ilumine tu hogar.",
        "¡Paz, amor y alegría para todos!",
        "La Navidad es tiempo de compartir.",
        "Deseándote una Navidad llena de amor y felicidad."
    ]
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.color("gold")
    message_turtle.penup()
    message_turtle.goto(0, 250)
    message_turtle.write(random.choice(phrases), align="center", font=("Arial", 18, "bold"))

# Dibujar el árbol y las luces
tree_turtle = turtle.Turtle()
tree_turtle.hideturtle()
tree_turtle.speed(0)

# Dibujar tronco
draw_trunk(tree_turtle)

# Dibujar secciones del árbol
sections = [
    (-100, -140, 200, 100),
    (-85, -80, 170, 90),
    (-70, -20, 140, 80),
    (-55, 30, 110, 70),
]

for x, y, width, height in sections:
    draw_tree_section(tree_turtle, x, y, width, height)

# Dibujar luces en posiciones aleatorias
for _ in range(50):
    x = random.randint(-90, 90)
    y = random.randint(-130, 80)
    draw_light(x, y)

# Mostrar frase navideña
show_message()

# Estrella en la cima
star = turtle.Turtle()
star.hideturtle()
star.color("yellow")
star.penup()
star.goto(0, 90)
star.begin_fill()
for _ in range(5):
    star.forward(40)
    star.right(144)
star.end_fill()

# Mantener ventana abierta
screen.mainloop()
