import random
import turtle
import os

os.system('title circleRender debug info')

window = turtle.Screen()
jony = turtle.Turtle()
jony.color("red", "black")

limit = 0
totalCircleDeg = 0
finalCircleDeg = 0
randomize = "random"
infinite = "infinite"


circleSize = 1
circleSizeIncrease = 1
circleSizeLimit = 300
circleSpeed = 250
circleSpeedIncrease = circleSpeed
circleLimit = infinite
circleDeg = randomize
circleCPS = 2
circleCPSIncrease = 2


if circleCPS < 2:
    print("Invalid CPS count. (<2) ")
    os.system('pause')
    window.bye()


def infinity():
    while True:
        yield


# circleSize = window.numinput("circleRender.py", "Size:", minval=0, maxval=x)


####defaultSettings
# circleSize = 250 (lower = smaller)
# circleSpeed = 50 (lower = slower)
# circleLimit = infinite (amount of sets drawn)
# circleDeg = randomize (amount of degrees between sets)
# circleSizeIncrease = 0 (amount added to circleSize every loop)
# circleSpeedIncrease = 0 (amount added to circleSpeed every loop)
# circleSizeLimit = 0 (amount before the circle stops circleSizeIncrease)
# circleCPS = 4 (circles per set)
# circleCPSIncrease = 0 (pretty basic)


if not circleLimit == 'infinite':
    forCircle = (range(1, circleLimit + 1))
else:
    forCircle = (infinity())


def colorChanger():  # change turtle color function
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

def debugLocator():
    global limit
    limit = limit + 1

    global totalCircleDeg
    if totalCircleDeg >= 360:
        totalCircleDeg = totalCircleDeg - 360

    print("Drew set ",limit,"/",circleLimit," at ",totalCircleDeg,"º. Drawing at ",circleSpeed," (", circleSize,")")

def circleSizeCalc():
    global circleSize
    global circleSizeLimit
    global circleSizeIncrease

    if circleSizeLimit <= circleSize:
        if not circleSizeLimit == 0:
            circleSizeIncrease = 0
    circleSize = circleSize + circleSizeIncrease


# start of the rendering loop
for i in forCircle:

    if circleSpeed == "random":
        csRandomToggle = 1
    else:
        csRandomToggle = 0

    if csRandomToggle == "1":
        circleSpeed = random.randint(1, 999999)

    turtle.tracer(circleSpeed)
    circleSpeed = circleSpeed + circleSpeedIncrease

    if circleDeg == "random":
        circleDeg = random.randint(2, 359)
        randomDegEnable = 1
    else:
        randomDegEnable = 0

    if randomDegEnable == 1:
        circleDeg = random.randint(2, 359)

    if not 'circleDeg' in locals():
        circleDeg = random.randint(2, 359)

    for i in range(1, circleCPS+1):
        jony.circle(circleSize)
        jony.left(90)

    jony.left(circleDeg)
    totalCircleDeg = totalCircleDeg + circleDeg
    finalCircleDeg = finalCircleDeg + circleDeg


    if circleCPSIncrease != 0:
        circleCPS=circleCPS+circleCPSIncrease

    circleSizeCalc()
    colorChanger()
    debugLocator()



print("Reached loop limit value\n\nTotal deg drawn=", int(finalCircleDeg), "º")
window.exitonclick()
