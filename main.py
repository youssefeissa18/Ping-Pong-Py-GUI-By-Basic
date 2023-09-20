# call library turtle for Gui
import turtle

# Features of Game Screen and intialize screen
win = turtle.Screen()
win.title("Ping Pong Game By Youssef") # Title for Window
win.bgcolor("black") # Color for Screen
win.setup(width= 800, height= 600) # width and height for Window
win.tracer(0) # to Stop Update for screen


#madrab1
madrab1 = turtle.Turtle() # initalize Tutrle object
madrab1.speed(0) # speed for madrab to move
madrab1.shape("square")#shape for madrab
madrab1.color("blue")#color for madrab
madrab1.penup()# To remove the Point is move there
madrab1.goto(-350,0)# start postion
madrab1.shapesize(6,1,1.5) # size of madrab

#madrab2
madrab2 = turtle.Turtle() # initalize Tutrle object
madrab2.speed(0) # speed for madrab to move
madrab2.shape("square") #shape for madrab
madrab2.color("red") #color for madrab
madrab2.penup() # To remove the Point is move there
madrab2.goto(350,0) # start postion
madrab2.shapesize(6,1,1.5) # size of madrab

#ball
ball = turtle.Turtle() # initalize Tutrle object
ball.speed(0) # speed for madrab to move
ball.shape("circle") #shape for madrab
ball.color("white") #color for madrab
ball.penup() # To remove the Point is move there
ball.goto(0,0) # start postion
ball.dx = 2.5
ball.dy = 2.5


# Move Up For Two madrab
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

# Move Down For Two madrab
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


# keyboard button will use
win.listen()
win.onkeypress(madrab1_up(), "w") # make the move up using W
win.onkeypress(madrab1_down(), "s") # make the move up using S

win.onkeypress(madrab2_up(), "Up") # make the move up using up button
win.onkeypress(madrab2_down(), "Down") # make the move up using down button

# main game loop
while True:
    win.update()    # to make Screen update
    # move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)