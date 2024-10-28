import turtle

happy=turtle.Screen()
happy.bgcolor("black")
turtle=turtle.Turtle()
turtle.shape("circle")
turtle.color("yellow")
turtle.width(7)
colors=["peru","ivory","dark orange","coral","cyan","hot pink","gold","ivory","yellow","red","pink","green","blue","light blue","light green",]

import time

time.sleep(10)

def draw_happy(i,x,y):
    turtle.pencolor("linen")
    turtle.color(colors[i%7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()

def ballon(x,y):
    for i in range(5):
        draw_happy(i,x,y)

def f1():
  for i in range(7):
    turtle.pensize(5)
    turtle.pencolor('light blue')
    turtle.color(colors[i%19])
    turtle.begin_fill()
    turtle.left(330)
    turtle.forward(55)
    turtle.begin_fill()
    turtle.rt(110)
    turtle.circle(33)
    turtle.end_fill()
    turtle.rt(11)
    turtle.backward(33)
    turtle.end_fill()

def cake(x,y):
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.rt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)

def heart():
   for i in range(43):
         turtle.pencolor(colors[i%9])
         turtle.rt(5)
         turtle.fd(5)
   turtle.fd(150)
   turtle.penup()
   turtle.rt(140)
   turtle.fd(147)
   turtle.pendown()
   for i in range(43):
         turtle.pencolor(colors[i%9])
         turtle.lt(5)
         turtle.fd(5)
   turtle.lt(7)
   turtle.fd(151)

def move(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.rt(90)
   turtle.fd(x)
   turtle.lt(90)
   turtle.fd(y)
   turtle.pendown()

def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

def A(size):
  turtle.rt(19)
  turtle.forward(size)
  turtle.rt(141)
  turtle.fd(size)
  turtle.backward(size/2)
  turtle.rt(105)
  turtle.fd(int(size/3))

def B(size):
   turtle.forward(size)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(size//20)
   for i in range(18):
      turtle.rt(size//5)
      turtle.backward(size//20)

def D(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//10)
   for i in range(13):
      turtle.rt(13)
      turtle.fd(size//8)

def H(size):
   turtle.fd(size)
   turtle.backward(size//2)
   turtle.rt(90)
   turtle.fd(size//2)
   turtle.lt(90)
   turtle.fd(size//2)
   turtle.backward(size)

def I(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.circle(size//8)

def P(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//8)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(size//9)

def R():
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(3)
   turtle.lt(120)
   turtle.fd(40)

def T(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//2)
   turtle.backward(size//2)

def Y(size):
   turtle.fd(size)
   turtle.left(60)
   turtle.fd(size//2)
   turtle.backward(size//2)
   turtle.rt(90)
   turtle.fd(size//1.5)

turtle.speed(19)

from turtle import *
from random import randint

def Spiral():
    x=1
    turtle.speed(0)
    while x<260:
      turtle.pencolor(colors[x%9])
      turtle.fd(10+x)
      turtle.rt(90.991)
      x=x+1

def triangle(size):
	turtle.color(colors[5%3])
	turtle.begin_fill()
	for i in range(3):
			turtle.pencolor(colors[i%4])
			turtle.left(120)
			turtle.fd(size)
	turtle.end_fill()

def triflow():
    for i in range(12):
        triangle(140)
        turtle.left(30)
        turtle.fd(10)
        triangle(151)

def spiral():
	for i in range(60):
		turtle.pencolor(colors[i%5])
		turtle.circle(2*i)
		turtle.circle(-2*i)
		turtle.left(i)

def draw_leaf(leaf):       #cretes leaf function
      for i in range(0,2):
            leaf.forward(90)
            leaf.right(40+i)
            for j in range(0,21):
                  leaf.right(3)
                  leaf.forward(5)
            leaf.right(145)

def draw_flower(pen):
      for i in range(0,8):
	      pen.color(colors[i%8])
	      pen.begin_fill()
	      draw_leaf(pen)
	      pen.end_fill()
	      pen.right(10)

turtle.width(1)
mov(480,240)
Spiral()
mov(-480,240)
Spiral()

#section of Ballons
move(180,307)
mov(0,0)
ballon(-460, 200)
ballon(490, 200)
ballon(183,-80)
ballon(-133,-80)
turtle.width(5)
mov(-450,-250)
draw_flower(turtle)
mov(450,-250)
draw_flower(turtle)
mov(-30,-120)
turtle.width(13)
heart()
#end Section of ballons


#Cake maker section
turtle.shape('turtle')
mov(120,100)
turtle.color(colors[8%5])
turtle.begin_fill()
cake(40,180)
turtle.end_fill()
mov(110,135)
turtle.color("hot pink")
turtle.begin_fill()
cake(40,160)
turtle.end_fill()
mov(100,170)
turtle.color("blanched almond")
turtle.begin_fill()
cake(40,140)
turtle.end_fill()
mov(30,210)
turtle.width(11)
turtle.pencolor("red")
turtle.circle(7)
# #end Of Cake Section


# #happybithday
turtle.pencolor("cyan")
turtle.width(13)
mov(260,0)
H(100)
turtle.width(7)
mov(190,0)
A(65)
mov(135,0)
P(60)
mov(100,0)
P(60)
mov(52,0)
Y(60)
mov(28,0)
B(60)
move(12,0)
I(60)
move(36,0)
R()
move(80,0)
T(100)
move(102,0)
H(60)
move(150,0)
turtle.pencolor('hotpink')
D(200)
move(160,0)
A(60)
move(220,0)
Y(60)

happy.exitonclick()