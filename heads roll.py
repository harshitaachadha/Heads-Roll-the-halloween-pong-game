import turtle
import os
wn=turtle.Screen()
wn.title("Heads Roll")
wn.bgcolor("lightblue")
wn.setup(width=800,height=600)
wn.tracer(0)
#score
score_a=0
score_b=0
#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("gold")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("gold")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350,0)

#ball
b=turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("yellowgreen")
b.shapesize(stretch_wid=1.5, stretch_len=1.5)
b.penup()
b.goto(0,0)
b.dx=2
b.dy=-2
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("magenta")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))
#functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
#Keyboard bindingw
wn.listen()
wn.onkey(paddle_a_up,"w")
wn.onkey(paddle_a_down,"s")
wn.onkey(paddle_b_up,"Up")
wn.onkey(paddle_b_down,"Down")
#Main Game loop
while True:
    wn.update()

    #move the ball:
    b.setx(b.xcor()+b.dx)
    b.sety(b.ycor()+b.dy)

    #border check
    if b.ycor()>290:
        b.sety(290)
        b.dy *=-1
        os.system("afplay bounce.wav&")

    if b.ycor()<-290:
        b.sety(-290)
        b.dy *=-1
        os.system("afplay bounce.wav&")

    if b.xcor()>390:
        b.goto(0,0)
        b.dx *=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
        os.system("afplay bounce.wav&")

    if b.xcor()<-390:
        b.goto(0,0)
        b.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))
        os.system("afplay bounce.wav&")

    #paddle and ball collisions
    if (b.xcor()>340 and b.xcor()<350) and (b.ycor()<paddle_b.ycor()+50 and b.ycor()>paddle_b.ycor()-50):
        b.setx(340)
        b.dx *= -1
        score_a+=1
        os.system("afplay bounce.wav&")
    if (b.xcor()<-340 and b.xcor()>-350) and (b.ycor()<paddle_a.ycor()+50 and b.ycor()>paddle_a.ycor()-50):
        b.setx(-340)
        b.dx *= -1
        os.system("afplay bounce.wav&")
