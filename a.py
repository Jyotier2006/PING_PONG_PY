import turtle
import random
win = turtle.Screen()
win.title("A PING-PONG Game")
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)
player1_name = win.textinput("Player 1", "Enter the name of Player 1:")
player2_name = win.textinput("Player 2", "Enter the name of Player 2:")
target_score = int(win.textinput("Winning Score", "Enter the winning score:"))
colors = ["red", "blue", "yellow", "green", "purple", "orange", "white", "pink"]
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("green")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("crimson")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
initial_dx = 0.06
initial_dy = 0.06
ball.dx = initial_dx
ball.dy = initial_dy
speed_increase_factor = 1.1
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(player1_name + " : " + str(score_a) + "   " + player2_name + " : " + str(score_b), align="center", font=("Courier", 24, "normal"))
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)
def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)
def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)
win.listen()
win.onkeypress(pad_a_up, "w")
win.onkeypress(pad_a_down, "s")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")
def update_score():
    pen.clear()
    pen.write(player1_name + " : " + str(score_a) + "   " + player2_name + " : " + str(score_b), align="center", font=("Courier", 24, "normal"))
while True:
    win.update()
    if score_a == target_score:
        pen.clear()
        pen.write(player1_name + " won the game!", align="center", font=("Courier", 24, "normal"))
        break
    if score_b == target_score:
        pen.clear()
        pen.write(player2_name + " won the game!", align="center", font=("Courier", 24, "normal"))
        break
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx = initial_dx * -1 
        ball.dy = initial_dy
        update_score()
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx = initial_dx 
        ball.dy = initial_dy
        update_score()
    if (ball.xcor() > 340 and ball.xcor() < 350) and (pad_b.ycor() - 50 < ball.ycor() < pad_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1
        ball.dx *= speed_increase_factor 
        ball.dy *= speed_increase_factor
        pad_b.color(random.choice(colors)) 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (pad_a.ycor() - 50 < ball.ycor() < pad_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= speed_increase_factor 
        ball.dy *= speed_increase_factor
        pad_a.color(random.choice(colors))
win.mainloop()