# Shawn Jones
# A02248994
# This program draws a really cool Snowman bro dude. It will be super awsome and we are going to do some crazy crap!
# PS EVERY snowflake is diffrent if you dont belive me change teh scaleFactor. Try setting it to 1.
#Sudo code
#Begin
# draw the snow man
# generate the snow flakes
#End

#import used pakages
import turtle
import random

turtle.speed(100)

scaleFactor = 100

#This function draws a circle
def drawCircle(r, ex, color1, color2):
    turtle.color(color1)
    turtle.fillcolor(color2)
    turtle.begin_fill()
    turtle.circle(r, ex)
    turtle.end_fill()

#This fucntion draws the arms, but will also be used to draw the snow flakes
#This fuction takes a lot of paramaters, main,b1,b2, and b3 are all the lengths you would like. main being the arm and
# the b's being finger lengths. Width_i sets the width you would like and  the heading's will set the direction of the
# arms
def drawArms(main, b1, b2, b3, width_i, color, heading_i):
    turtle.setheading(heading_i)
    turtle.color(color)
    turtle.width(width_i)
    turtle.forward(main)
    turtle.width(width_i / 2.5)
    turtle.setheading(heading_i - 30)
    turtle.forward(b1)
    turtle.backward(b1)
    turtle.setheading(heading_i)
    turtle.forward(b2)
    turtle.backward(b2)
    turtle.setheading(heading_i + 30)
    turtle.forward(b3)

#this fucntion will randomly genirate snow flakes
#it will take an imput heading and then geriate one of the snow flakes arms.
def drawSnowFlakes(heading_p):
    main_i = random.randint(1, 100)
    b_1 = random.randint(1, 50)
    b_2 = random.randint(1, 50)
    b_3 = random.randint(1, 50)
    main_i = main_i / scaleFactor
    b_1 = b_1 / scaleFactor
    b_2 = b_2 / scaleFactor
    b_3 = b_3 / scaleFactor

    drawArms(main_i, b_1, b_2, b_3, 3, "white", heading_p)



#set the background color.
turtle.bgcolor("black")

#set the turtle to starting zone
turtle.penup()
turtle.goto(0, -160)
turtle.penup()

#this part of the code draws the body of our snowman
drawCircle(75, 360, "white", "white")
turtle.goto(0, -18)
drawCircle(50, 360, "white", "white")
turtle.goto(0, 75)
drawCircle(35, 360, "white", "white")

#This will draw his face
#This is his eyes
turtle.goto(10, 115)
drawCircle(5, 360, "black", "black")
turtle.penup()
turtle.goto(-10, 115)
drawCircle(5, 360, "black", "black")

#this will draw his mouth
turtle.goto(-15, 95)
turtle.setheading(-42)
turtle.width(5)
turtle.pendown()
drawCircle(25, 90, "black", "white")

#This code will draw his arms
turtle.penup()
turtle.goto(-45, 40)
turtle.pendown()
drawArms(40, 20, 20, 20, 8, "brown", 160)
turtle.penup()
turtle.goto(45, 40)
turtle.pendown()
drawArms(40, 20, 20, 20, 8, "brown", 30)

#Now we draw the buttons
turtle.penup()
turtle.goto(5, 15)
drawCircle(5, 360, "blue", "blue")
turtle.goto(5, 30)
drawCircle(5, 360, "blue", "blue")
turtle.goto(5, 45)
drawCircle(5, 360, "blue", "blue")

#Draw the hat
turtle.goto(-35, 145)
turtle.color("blue")
turtle.pendown()
turtle.setheading(0)
turtle.forward(70)
turtle.goto(-17.5, 145)
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(30)
turtle.setheading(0)
turtle.forward(35)
turtle.setheading(-90)
turtle.forward(30)
turtle.end_fill()

#Draw the ground
turtle.penup()
turtle.color("white")
turtle.begin_fill()
turtle.goto(-400, -150)
turtle.pendown()
turtle.goto(400, -150)
turtle.goto(400, -400)
turtle.goto(-400, -400)
turtle.goto(-400, -150)
turtle.end_fill()


#we need to pen up so the next fuction works properly
turtle.penup()

#draw the snow flakes
#this loop will fun of the number of snow flakes
#it will first randomly genirate the possition of the snow flakes then it will us the drawnSnowFlakes funtions to build
#the snowflakes
for i in range(900):
    x = random.randint(-400, 400)
    y = random.randint(-150, 400)
    turtle.goto(x, y)
    heading_c = random.randint(-360, 360)
    #this will randomly genirate a number between 3 and 6, this will how many arms are on the snow flakes. Between one
    #and 6.
    numOfArms = random.randint(3, 6)
    heading_increasing = 360 / numOfArms

    # hide the turtle
    turtle.hideturtle()

    #this loop will call draw snow flakes acroding to the number of arms and ran gen headings
    for b in range(numOfArms):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        drawSnowFlakes(heading_c)
        heading_c = heading_c + heading_increasing
    turtle.penup()


#Wait for the user to end the program
turtle.done()
