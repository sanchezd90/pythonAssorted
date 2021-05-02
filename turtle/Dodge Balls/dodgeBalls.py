import turtle
import random
import string

wn = turtle.Screen()
wn.title("Dodge")
wn.bgcolor("white")
wn.setup(width=800, height=800)

#longitud de movimiento de los fireballs
d=35

#longitud de movimiento del player
w=20

#contador de letras comidas
p_1=0
p_2=0
p_3=0
p_4=0
p_5=0
p_6=0

#fin juego
GO = False
FAIL = False
level = 1
xo = False

ran1 = random.randrange(-200,200)
ran2 = random.randrange(-200,200)
ran3 = random.randrange(-200,200)
ran4 = random.randrange(-200,200)
ran5 = random.randrange(-200,200)
ran6 = random.randrange(-200,200)
ran7 = random.randrange(-200,200)
ran8 = random.randrange(-200,200)
ran9 = random.randrange(-200,200)
ran10 = random.randrange(-200,200)
ran11 = random.randrange(-200,200)
ran12 = random.randrange(-200,200)
ran13 = random.randrange(-200,200)
ran14 = random.randrange(-200,200)
ran15 = random.randrange(-200,200)
ran16 = random.randrange(-200,200)

set1 = [ran1,ran2,ran3,ran4,ran5,ran6,ran7,ran8,ran9,ran10,ran11,ran12,ran13,ran14,ran15,ran16]

fire = turtle.Turtle()
fire.speed(0)
fire.color("red")
fire.shape("circle")
fire.shapesize(2)
fire.penup()
fire.goto((ran1,ran2))
fire.dx = 20
fire.dy = 20

f2 = turtle.Turtle()
f2.speed(0)
f2.color("red")
f2.shape("circle")
f2.shapesize(2)
f2.penup()
f2.goto((ran3,ran4))
f2.dx = -20
f2.dy = 20

f3 = turtle.Turtle()
f3.speed(0)
f3.color("red")
f3.shape("circle")
f3.shapesize(2)
f3.penup()
f3.goto((ran5,ran6))
f3.dx = 20
f3.dy = 20

player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("circle")
player.shapesize(2)
player.penup()
player.goto(0,0)

b1 = turtle.Turtle()
b1.hideturtle()
b1.speed(0)
b1.color("black")
b1.shapesize(stretch_wid=0.5, stretch_len=0.5)
b1.penup()
b1.goto(ran1,ran8)
b1.write("A", align="center", font=("Courier", 24, "normal"))

b2 = turtle.Turtle()
b2.hideturtle()
b2.speed(0)
b2.color("black")
b2.shapesize(stretch_wid=0.5, stretch_len=0.5)
b2.penup()
b2.goto(ran2,ran7)
b2.write("B", align="center", font=("Courier", 24, "normal"))

b3 = turtle.Turtle()
b3.hideturtle()
b3.speed(0)
b3.color("black")
b3.shapesize(stretch_wid=0.5, stretch_len=0.5)
b3.penup()
b3.goto(ran3,ran6)
b3.write("C", align="center", font=("Courier", 24, "normal"))

b4 = turtle.Turtle()
b4.hideturtle()
b4.speed(0)
b4.color("black")
b4.shapesize(stretch_wid=0.5, stretch_len=0.5)
b4.penup()
b4.goto(ran4,ran5)
b4.write("D", align="center", font=("Courier", 24, "normal"))

b5 = turtle.Turtle()
b5.hideturtle()
b5.speed(0)
b5.color("black")
b5.shapesize(stretch_wid=0.5, stretch_len=0.5)
b5.penup()
b5.goto(ran1,ran4)
b5.write("E", align="center", font=("Courier", 24, "normal"))

b6 = turtle.Turtle()
b6.hideturtle()
b6.speed(0)
b6.color("black")
b6.shapesize(stretch_wid=0.5, stretch_len=0.5)
b6.penup()
b6.goto(ran7,ran2)
b6.write("F", align="center", font=("Courier", 24, "normal"))

lose = turtle.Turtle()
lose.hideturtle()
lose.speed(0)
lose.color("white")
lose.penup()
lose.goto(0,0)

win = turtle.Turtle()
win.hideturtle()
win.speed(0)
win.color("white")
win.penup()
win.goto(0,0)

cont = turtle.Turtle()
cont.hideturtle()
cont.speed(0)
cont.color("white")
cont.penup()
cont.goto(0,-50)

def player_up():
    y = player.ycor()
    y += w
    player.sety(y)

def player_l():
    x = player.xcor()
    x -= w
    player.setx(x)

def player_down():
    y = player.ycor()
    y -= w
    player.sety(y)

def player_r():
    x = player.xcor()
    x += w
    player.setx(x)

def next():
    GO = False
    player.showturtle()
    fire.showturtle()
    f2.showturtle()
    f3.showturtle()
    win.clear()
    cont.clear()
    p_1=0
    p_2=0
    p_3=0
    p_4=0
    p_5=0
    p_6=0



wn.listen()
wn.onkey(player_up, "Up")
wn.onkey(player_down, "Down")
wn.onkey(player_l, "Left")
wn.onkey(player_r, "Right")
wn.onkey(next,"x")


while True:
    wn.update()

    # move fireballs
    fire.setx(fire.xcor()+ fire.dx)
    fire.sety(fire.ycor()+ fire.dy)
    f2.setx(f2.xcor()+ f2.dx)
    f2.sety(f2.ycor()+ f2.dy)
    f3.setx(f3.xcor()+ f3.dx)
    f3.sety(f3.ycor()+ f3.dy)

    ##border checking
    if fire.ycor() > 380:
        fire.sety(380)
        fire.dy *= -1

    if fire.ycor() < -380:
        fire.sety(-380)
        fire.dy *= -1

    if fire.xcor() > 380:
        fire.setx(380)
        fire.dx *= -1

    if fire.xcor() < -380:
        fire.setx(-380)
        fire.dx *= -1

    if f2.ycor() > 380:
        f2.sety(380)
        f2.dy *= -1

    if f2.ycor() < -380:
        f2.sety(-380)
        f2.dy *= -1

    if f2.xcor() > 380:
        f2.setx(380)
        f2.dx *= -1

    if f2.xcor() < -380:
        f2.setx(-380)
        f2.dx *= -1

    if f3.ycor() > 380:
        f3.sety(380)
        f3.dy *= -1

    if f3.ycor() < -380:
        f3.sety(-380)
        f3.dy *= -1

    if f3.xcor() > 380:
        f3.setx(380)
        f3.dx *= -1

    if f3.xcor() < -380:
        f3.setx(-380)
        f3.dx *= -1

    #comer

    if abs(player.xcor() - b1.xcor()) < 15 and abs(player.ycor() - b1.ycor()) < 15:
        b1.clear()
        p_1 = 1

    if abs(player.xcor() - b2.xcor()) < 15 and abs(player.ycor() - b2.ycor()) < 15 and p_1 == 1:
        b2.clear()
        p_2 = 1

    if abs(player.xcor() - b3.xcor()) < 15 and abs(player.ycor() - b3.ycor()) < 15 and p_1 == 1  and p_2 == 1:
        b3.clear()
        p_3 = 1

    if abs(player.xcor() - b4.xcor()) < 15 and abs(player.ycor() - b4.ycor()) < 15 and p_1 == 1  and p_2 == 1  and p_3 == 1:
        b4.clear()
        p_4 = 1

    if abs(player.xcor() - b5.xcor()) < 15 and abs(player.ycor() - b5.ycor()) < 15 and p_1 == 1  and p_2 == 1  and p_3 == 1 and p_4 == 1:
        b5.clear()
        p_5 = 1

    if abs(player.xcor() - b6.xcor()) < 15 and abs(player.ycor() - b6.ycor()) < 15 and p_1 == 1  and p_2 == 1  and p_3 == 1 and p_4 == 1 and p_5 == 1  :
        b6.clear()
        p_6 = 1

    if abs(player.xcor() - fire.xcor()) < 15 and abs(player.ycor() - fire.ycor()) < 15:
        FAIL = True

    if abs(player.xcor() - f2.xcor()) < 15 and abs(player.ycor() - f2.ycor()) < 15:
        FAIL = True

    if abs(player.xcor() - f3.xcor()) < 15 and abs(player.ycor() - f3.ycor()) < 15:
        FAIL = True

    if p_1 == 1  and p_2 == 1  and p_3 == 1 and p_4 == 1 and p_5 == 1 and p_6 == 1:
        GO = True

    if FAIL == True:
        player.hideturtle()
        fire.hideturtle()
        f2.hideturtle()
        f3.hideturtle()
        b1.clear()
        b2.clear()
        b3.clear()
        b4.clear()
        b5.clear()
        b6.clear()
        lose.color("red")
        lose.write("Perdiste", align="center", font=("Courier", 24, "normal"))

    if GO == True:
        player.hideturtle()
        fire.hideturtle()
        f2.hideturtle()
        f3.hideturtle()
        b1.clear()
        b2.clear()
        b3.clear()
        b4.clear()
        b5.clear()
        b6.clear()
        win.color("red")
        win.write("Nivel {} completado".format(level), align="center", font=("Courier", 24, "normal"))
        cont.color("blue")
        cont.write("Presione X para continuar", align="center", font=("Courier", 24, "normal"))
        p_1=0
        p_2=0
        p_3=0
        p_4=0
        p_5=0
        p_6=0
