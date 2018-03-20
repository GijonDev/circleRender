import random
import turtle

window = turtle.Screen()
jony = turtle.Turtle()
jony.color("red", "black")
limit = 0
totalCircleDeg = 0
fcd = 0

circleSize = 250
circleSpeed = 50
circleLimit = 999
circleDeg = "random"
circleSum = 0
circleIncrease = 0


####defaultSettings
# circleSize = 250 (lower = smaller)
# circleSpeed = 50 (lower = slower)
# circleLimit = "infinite" (amount of circles drawn)
# circleDeg = "random" (amount of degrees between set of circles)
# circleSum = 0 (amount added to circleSize every loop)
# circleIncrease = 0 (amount added to circleSpeed every loop)


def infinity():
    while True:
        yield


if not circleLimit == "infinite":
    forCircle = (range(1, circleLimit+1))
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
    limitGlobal()
    tcgChecker()
    print("Drew set ", limit, " at ", totalCircleDeg, "º. Drawing at ", circleSpeed)


def limitGlobal():
    global limit
    limit = limit + 1


def tcgChecker():
    global totalCircleDeg
    if totalCircleDeg >= 360:
        totalCircleDeg = totalCircleDeg - 360


####start of the rendering loop####
for i in forCircle:

    turtle.tracer(circleSpeed)
    circleSpeed = circleSpeed + circleIncrease

    if circleDeg == "random":
        circleDeg = random.randint(2, 359)
        randomDegEnable = 1
    else:
        randomDegEnable = 0

    if randomDegEnable == 1:
        circleDeg = random.randint(2, 359)

    if not 'circleDeg' in locals():
        circleDeg = random.randint(2, 359)

    for i in range(1, 5):
        jony.circle(circleSize)
        jony.left(90)

    jony.left(circleDeg)
    totalCircleDeg = totalCircleDeg + circleDeg
    fcd = fcd + circleDeg
    circleSize = circleSize + circleSum

    colorChanger()
    debugLocator()

print("Reached loop limit value\n\nTotal deg drawn=", int(fcd), "º")
window.exitonclick()
