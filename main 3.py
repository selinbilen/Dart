import turtle
import random 
import math
t=turtle.Turtle()
wn=turtle.Screen()
t.speed(10)
t.hideturtle()

t.setposition(0,-300)
t.begin_fill()
t.color("black")
t.circle(300)
t.end_fill()
t.penup()
t.setposition(0,0)
t.left(9)
for i in range(10)  :
  t.pendown()
  t.forward(240)
  t.left(90)
  t.color("red")
  t.begin_fill()
  t.circle(240,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)
  t.forward(240)
  t.left(90)
  t.color("green")
  t.begin_fill()
  t.circle(240,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)

t.penup()
t.setposition(0,0)
for i in range(10)  :
  t.pendown()
  t.forward(220)
  t.left(90)
  t.color("black")
  t.begin_fill()
  t.circle(220,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)
  t.forward(220)
  t.left(90)
  t.color("white")
  t.begin_fill()
  t.circle(220,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)

t.penup()
t.setposition(0,0)
for i in range(10)  :
  t.pendown()
  t.forward(130)
  t.left(90)
  t.color("red")
  t.begin_fill()
  t.circle(130,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)
  t.forward(130)
  t.left(90)
  t.color("green")
  t.begin_fill()
  t.circle(130,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)

t.penup()
t.setposition(0,0)
for i in range(10)  :
  t.pendown()
  t.forward(110)
  t.left(90)
  t.color("black")
  t.begin_fill()
  t.circle(110,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)
  t.forward(110)
  t.left(90)
  t.color("white")
  t.begin_fill()
  t.circle(110,18)
  t.setposition(0,0)
  t.end_fill()
  t.left(18)



t.penup()
t.setposition(0,0)
t.right(18)
t.pendown()
for i in range(20):
  t.color("white")
  t.forward(240)
  t.backward(240)
  t.right(18)
t.penup()

t.left(9)
t.setposition(0,-25)
t.pendown()
t.begin_fill()
t.color("green")
t.circle(25)
t.end_fill()
t.penup()
t.color("white")
t.setposition(0,-25)
t.pendown()
t.circle(25)
t.penup()


t.setposition(0,-12)
t.begin_fill()
t.color("red")
t.pendown()
t.circle(12)
t.end_fill()
t.color("white")
t.penup()
t.setposition(0,-12)
t.pendown()
t.circle(12)

t.penup()
t.setposition(0,-240)
t.pendown()
t.circle(240)
t.penup()
t.setposition(0,-220)
t.pendown()
t.circle(220)
t.penup()
t.setposition(0,-130)
t.pendown()
t.circle(130)
t.penup()
t.setposition(0,-110)
t.pendown()
t.circle(110)


FONT_SIZE = 30
FONT = ("Arial", FONT_SIZE, "bold")
t.penup()
t.setposition(-25,260)
t.pendown()
t.color("white")
t.write("20", font=FONT)
t.penup()
t.setposition(-5,-280)
t.pendown()
t.color("white")
t.write("3", font=FONT)
t.penup()
t.setposition(-290,-10)
t.pendown()
t.color("white")
t.write("11", font=FONT)
t.penup()
t.setposition(260,-10)
t.pendown()
t.color("white")
t.write("6", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(235,70)
t.pendown()
t.color("white")
t.write("13", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(235,-90)
t.pendown()
t.color("white")
t.write("10", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-280,80)
t.pendown()
t.color("white")
t.write("14", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-265,-85)
t.pendown()
t.color("white")
t.write("8", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-230,140)
t.pendown()
t.color("white")
t.write("9", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-180,205)
t.pendown()
t.color("white")
t.write("12", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-90,245)
t.pendown()
t.color("white")
t.write("5", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(65,245)
t.pendown()
t.color("white")
t.write("1", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(140,195)
t.pendown()
t.color("white")
t.write("18", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(210,140)
t.pendown()
t.color("white")
t.write("4", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(200,-170)
t.pendown()
t.color("white")
t.write("15", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(150,-230)
t.pendown()
t.color("white")
t.write("2", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(60,-265)
t.pendown()
t.color("white")
t.write("17", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-110,-265)
t.pendown()
t.color("white")
t.write("19", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-175,-235)
t.pendown()
t.color("white")
t.write("7", font=FONT)
#-------------------------------------------------------------------
t.penup()
t.setposition(-250,-165)
t.pendown()
t.color("white")
t.write("16", font=FONT)

#--------------------------------------------------------------
#sırasıyla çizilen daire parçalarının puanları:
#1. parça = 13 puan   6 = 17 puan      11 = 8 puan      16 = 5 puan 
#2 = 9 puan           7 = 18 puan      12 = 15 puan     17 = 7 puan 
#3 = 3 puan           8 = 11 puan      13 = 20 puan     18 = 6 puan
#4 = 4 puan           9 = 2 puan       14 = 16 puan     19 = 12 puan 
#5 = 14 puan          10 = 1 puan      15 = 10 puan     20 = 19 puan
#--------------------------------------------------------------

#"T":3,  130 ile 110 arası
#"D":2,   240 ile 220 arası
#"S": 1,  300 den 20 ye kadar ama t ve d yok
#"I": 50,   12 den 0 a kadar
# "O": 25   25 ile 10 arası

total=int(input("please write a total value: "))
# radius of the circle
circle_r = 240
# center of the circle (x, y)
circle_x =0
circle_y =0
# random angle
pi=3,14
score=0

while total>score : 
  alpha = 2 * math.pi * random.random()
  # random radius
  r = circle_r * random.random()
# calculating coordinates
  x = int(r * math.cos(alpha) + circle_x)
  y = int(r * math.sin(alpha) + circle_y)
  print("Random point", (x, y))
  a=random.randint(1,20)
  area= math.sqrt((x**2)+(y**2))
  
  if area<12  :
    score += 50
    print("your throw: ", "I", a)
    print ("your points: ", 50)
    print("your total score: ",score)
  
  elif area<25 and area>15:
    score += 25
    print("your throw: ", "O", a)
    print ("your points: ", 25)
    print("your total score: ",score)
  
  elif area<(130) and area>(110):
    score += a*3
    print("your throw: ", "T", a)
    print ("your points: ", a*3)
    print("your total score: ",score)
  
  elif area<(240) and area>(220):
    score += a*2
    print("your throw: ", "D", a)
    print ("your points: ", a*2)
    print("your total score: ",score)
  
  else  :
    score += a
    print("your throw: ", "S", a)
    print ("your points: ", a)
    print("your total score: ",score)
  
  t.penup()
  t.shape("circle")
  t.color("navy")
  t.goto(x,y)
  t.pendown()
  t.stamp()

