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
madrab1 = turtle.Turtle() # initalize Tutrle object
madrab1.speed(0) # speed for madrab to move
madrab1.shape("circle") #shape for madrab
madrab1.color("white") #color for madrab
madrab1.penup() # To remove the Point is move there
madrab1.goto(0,0) # start postion


# main game loop
while True:
    win.update()    # to make Screen update
