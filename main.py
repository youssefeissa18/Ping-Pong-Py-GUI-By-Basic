import turtle

# Initialize the screen
win = turtle.Screen()
win.title("Ping Pong Game By Youssef")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle (madrab) 1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=6, stretch_len=1)
madrab1.penup()
madrab1.goto(-350, 0)

# Paddle (madrab) 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=6, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

#Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player1 :0 ""Player2 :0 ", align="center",font=("Courier",24,"normal"))

# Function to move paddle 1 up
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

# Function to move paddle 1 down
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

# Function to move paddle 2 up
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

# Function to move paddle 2 down
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

# Keyboard bindings
win.listen()
win.onkeypress(madrab1_up, "w")
win.onkeypress(madrab1_down, "s")
win.onkeypress(madrab2_up, "Up")
win.onkeypress(madrab2_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write(f"Player1 :{score1} "f"Player2 :{score2} ", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player1 :{score1} "f"Player2 :{score2} ", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (madrab2.ycor() + 50 > ball.ycor() > madrab2.ycor() - 50):
        ball.color("red")
        ball.setx(340)
        ball.dx *= -1

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (madrab1.ycor() + 50 > ball.ycor() > madrab1.ycor() - 50):
        ball.color("blue")
        ball.setx(-340)
        ball.dx *= -1