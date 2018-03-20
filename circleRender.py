import turtle
import random

window = turtle.Screen()
jony = turtle.Turtle()
jony.color("red", "black")


circleSize = 1
circleSpeed = 90
circleLimit = 99999
circleDeg = 50
circleSum = 1

###defaultSettings
#circleSize = 250
#circleSpeed = 50
#circleLimit = 99999
#circleDeg = "randomDeg"
#circleSum = 0

if circleDeg=="randomDeg":
    del circleDeg


turtle.tracer(circleSpeed)
for i in range (1,circleLimit):
    randomDeg=random.randint(45, 90)
    if not 'circleDeg' in locals():
        circleDeg=randomDeg
        randomDegEnable=1
    else:
        randomDegEnable=0

    if randomDegEnable==1:
        circleDeg=randomDeg
    
    
    for i in range (1,5):
        jony.circle(circleSize)
        jony.left(90)
        
    jony.left(circleDeg)
    circleSize=circleSize+circleSum

    if jony.color() == ("red", "black"):
        jony.color("orange", "black")
    elif jony.color() == ("orange", "black"):
        jony.color("yellow", "black")
    elif jony.color() == ("yellow", "black"):
        jony.color("green", "black")
    elif jony.color() == ("green", "black"):
        jony.color("blue", "black")
    elif jony.color() == ("blue", "black"):
        jony.color("pink", "black")
    elif jony.color() == ("pink", "black"):
        jony.color("red", "black")

    

window.exitonclick() #exit argument
