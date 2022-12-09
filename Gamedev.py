import turtle

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Scoring variables/system
score_a = 0
score_b = 0



#platform a 
platform_a = turtle.Turtle()
platform_a.speed(0)
platform_a.shape("square")
platform_a.color("white")
platform_a.shapesize(stretch_wid=5, stretch_len=1)
platform_a.penup()
platform_a.goto(-350, 0)

#platform b

platform_b = turtle.Turtle()
platform_b.speed(0)
platform_b.shape("square")
platform_b.color("white")
platform_b.shapesize(stretch_wid=5, stretch_len=1)
platform_b.penup()
platform_b.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#we use the (dx, dy) to tell the ball object to move on given value of pixel and for this one we use 2 pixels becaue that works well on my pc 
ball.dx = 0.2
ball.dy = -0.2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player I: 0  Player II: 0", align="center", font=("Minecraft", 24, "normal"))





# Function for the movement of the platforms #(ycor) use to define the coordinates of the object
def platform_a_up(): 
    coor_y = platform_a.ycor()
    coor_y += 40
    platform_a.sety(coor_y)

def platform_a_down(): 
    coor_y = platform_a.ycor()
    coor_y -= 40
    platform_a.sety(coor_y)

def platform_b_up(): 
    coor_y = platform_b.ycor()
    coor_y += 40
    platform_b.sety(coor_y)

def platform_b_down(): 
    coor_y = platform_b.ycor()
    coor_y -= 40
    platform_b.sety(coor_y)

#now we need to create a keyboard binding so we can move around a platform
#we use (.listen) to tell the program to listen for the keyboard input from the user
#we also use (.onkeypress) to define what key on our keyboard we need to use on the function that we created
window.listen()
window.onkeypress(platform_a_up, "w")
window.onkeypress(platform_a_down, "s")


window.onkeypress(platform_b_up, "Up")
window.onkeypress(platform_b_down, "Down")

#main game loop

while True:
    window.update()
    

    #We move the ball here <we use the same thing on the platforms but on diferent coordinates so we can move it vertically 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border cheacking (if we dont put a border checker the ball will end up on other univers so we need to create a border in order to not bounce it off the screem)
    #if the balls went to a certain point we need it to bounce off
    #this loops makes the ball reverse its direction if it hits a hieght of 290 pixel of the window we use the coordinates y to define where it shoul go
    #it reverse the direction of the ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() <  -290:
        ball.sety(-290)
        ball.dy *= -1

    #we use the (.goto) to reset the coordinate to center 
    #add the variable score_a so we can iterate the score everytime that the player bounces off the ball
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player I: {}  Player II: {}".format(score_a, score_b), align="center", font=("Minecraft", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1 
        pen.clear()
        pen.write("Player I: {}  Player II: {}".format(score_a, score_b), align="center", font=("Minecraft", 24, "normal"))
        

    #collisions
    #platform and ball collisions for platfor a and b 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < platform_b.ycor() + 50 and ball.ycor() > platform_b.ycor() - 50 ):
        ball.setx(340)
        ball.dx *= -1 
    #We basically iterating the coordinates to create a collision process
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < platform_a.ycor() + 50 and ball.ycor() > platform_a.ycor() - 50 ):
        ball.setx(-340)
        ball.dx *= -1 

    