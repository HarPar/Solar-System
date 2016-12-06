#####################################                
# Harshil Parikh                    #                                         
# 22/04/15                          #
#####################################

#BEGIN

#Imports
from tkinter import *
from random import *
from time import *
from math import *
from calendarTools import *
from datetime import *
from threading import Thread

try:
    import winsound

    #Playing sound file via a thread
    class MyBackgroundMusic (Thread):
        def run(self):
            while True:
                #Playing sound file
                winsound.PlaySound("Ambient_Piano_Space_Instrumental_Music.wav",winsound.SND_FILENAME)

    music = MyBackgroundMusic()
    music.start()
except:
    print("Importing winsound or playing music file gave a fatal erorr")

years = int(input("How many earth years would you like to observe? "))

#Calculating Days between 2 dates
currentDate = strftime("%b") + " " + strftime("%d") + ", " + strftime("%Y")
endDate = strftime("%b") + " " + strftime("%d") + ", " + str(int(strftime("%Y"))+years)
daysBetween = calculateDaysBetween(currentDate,endDate)

#Creating Tk and setting properties
root = Tk()
root.title("Solar System")
root.attributes("-fullscreen", True)

#Width and Height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#Creating Screen
screen = Canvas(root, height=height, width=width, background="black", cursor="star")
screen.pack()

#Drawing Black Hole, Quasar and Nebula in random positions
blackhole = PhotoImage(file="black_holes.gif")
quasar = PhotoImage(file="quasar.gif")
nebula = PhotoImage(file="nebula.gif")

bhX = randint(0,300)
bhY = randint(0,height-100)

qX = randint(500,800)
qY = randint(100,height-100)

nX = randint(1000,width)
nY = randint(0,height-100)

screen.create_image(bhX,bhY, image=blackhole)
screen.create_image(qX,qY, image=quasar)
screen.create_image(nX,nY, image=nebula)

#-----Parameters-----
#Planet
planets = [["Sun"], ["Mercury", 88], ["Venus", 224], ["Earth", 365], ["Mars", 687], ["Jupiter", 4332], ["Saturn", 10759], ["Uranus", 30685], ["Neptune", 60189]]
planetObj = []
planetImg = []
planetOrbit = []

#Stars
numStars = 200
numShiningStars = 15
stars = []
starsObj = []
starColours = ["orange", "yellow"]

#Miscellaneous
startTime = datetime.now()
fileExtension = ".gif"
targetFPS = 60
i = 15000
initialI = i
#-------------------

#Create initial star properties
for starRange in range(numStars):
    #Finding random starX/Y, starSize, starX/Y speed and outline colour
    starX, starY = randint(0, width), randint(0, height)
    starSize = randint(1, 3)
    #The larger the star the faster its speed######
    starXSpeed, starYSpeed = starSize*-1, starSize#
    ###############################################
    starOutline = choice(starColours)

    #Adding all those values to stars array
    stars.append([starX, starY, starXSpeed, starYSpeed, starSize, starOutline])

#Drawing shining stars randomly on screen
for shiningStars in range(numShiningStars):
    #Random shootingStarX/Y
    shootingStarX, shootingStarY = randint(0,width), randint(0, height)

    #Drawing the Shooting Star Components
    screen.create_polygon(shootingStarX,shootingStarY, shootingStarX+5,shootingStarY-25, shootingStarX+10,shootingStarY, smooth=True, fill="yellow")
    screen.create_polygon(shootingStarX+10,shootingStarY, shootingStarX+35,shootingStarY+5, shootingStarX+10,shootingStarY+10, smooth=True, fill="yellow")

    screen.create_polygon(shootingStarX+10,shootingStarY+10, shootingStarX+5,shootingStarY+35, shootingStarX,shootingStarY+10, smooth=True, fill="yellow")
    screen.create_polygon(shootingStarX,shootingStarY+10, shootingStarX-25,shootingStarY+5, shootingStarX,shootingStarY, smooth=True, fill="yellow")

    screen.create_oval(shootingStarX-5,shootingStarY-5, shootingStarX+15,shootingStarY+15, fill="yellow", outline="yellow")

#Create initial planet properties
for planetInfo in range(1, len(planets)):
    #Finding planet properties
    planets[planetInfo].append(2*pi/planets[planetInfo][1])
    planets[planetInfo].append(100*planetInfo*cos((i%planets[planetInfo][1])*planets[planetInfo][2])+900)
    planets[planetInfo].append(100*planetInfo*sin((i%planets[planetInfo][1])*planets[planetInfo][2])+height/2)
    planetOrbit.append(100*planetInfo)

    #Creating orbital path
    screen.create_oval(900-planetOrbit[planetInfo-1],height/2-planetOrbit[planetInfo-1], 900+planetOrbit[planetInfo-1],height/2+planetOrbit[planetInfo-1], outline="white")

#Creating planet image array
for planetImage in range(len(planets)):
    planetImg.append(PhotoImage(file=(planets[planetImage][0]+fileExtension)))

#Fining delta time for FPS
def deltaTime(startTime):
    delta = datetime.now() - startTime
    return delta.total_seconds()

#Callign the exit call
def exitCall(event):
    if event.keysym == "Escape":
        root.destroy()

#While time passed is less than desired number of years
while years*planets[3][1]+initialI > i:
    i+=1

    #Drawing the Stars
    for drawStars in range(numStars):
        #Appending stars to star array
        starsObj.append(screen.create_oval(stars[drawStars][0], stars[drawStars][1], stars[drawStars][0]+stars[drawStars][4], stars[drawStars][1]+stars[drawStars][4],
                                           fill="white", outline=stars[drawStars%len(starColours)][5]))

        #Adding star speed to create new x/y value
        stars[drawStars][0] += stars[drawStars][2]
        stars[drawStars][1] += stars[drawStars][3]

        #If star goes off the screen
        if stars[drawStars][0] <= 0:
            stars[drawStars][0] = width

        if stars[drawStars][1] >= height:
            stars[drawStars][1] = 0

    #Drawing the planets
    for planetDraw in range(1, len(planets)):
        #Finding planets x and y value
        planets[planetDraw][3] = (100*planetDraw*cos((i%planets[planetDraw][1])*planets[planetDraw][2])+900)
        planets[planetDraw][4] = (100*planetDraw*sin((i%planets[planetDraw][1])*planets[planetDraw][2])+height/2)

        #Appending planets to planet array
        planetObj.append(screen.create_image(planets[planetDraw][3], planets[planetDraw][4], image=planetImg[planetDraw]))

    #Drawing the sun
    Sun = screen.create_image(900, height/2, image=planetImg[0])

    #Displaying days passed
    dayLabel = screen.create_text(width/2, 25, text="Day " + str(i-initialI), fill="white", font="Helvetica 30")

    #Finding elapsed time
    elapsedTime = deltaTime(startTime)

    #Calculating sleep time
    sleepTime = (1/targetFPS) - elapsedTime

    if sleepTime < 0:
        sleepTime = 0

    #Displaying the FPS
    fpsLabel = screen.create_text(35, height-20, text = "FPS: " + str(int(1/(sleepTime+elapsedTime))), fill="white")

    #Update
    screen.update()

    #Sleep
    sleep(sleepTime)

    #New Start Time
    startTime = datetime.now()

    #Deleting stars, planets, fpsLabel, Sun and dayLabel
    for deleteStars in range(len(starsObj)):
        screen.delete(starsObj[deleteStars])
    for deletePlanets in range(len(planetObj)):
        screen.delete(planetObj[deletePlanets])

    screen.delete(fpsLabel, Sun, dayLabel)

    #Seleting arrays: planetObj and starsObj
    del planetObj[:]
    del starsObj[:]

    #Binding escape key to exitCall
    root.bind("<Key>", exitCall)

#When animation is over delete screen and display days passed
screen.delete("all")
screen.create_text(width/2, height/2, text="You have Travelled " + daysBetween + " days in Outer Space", fill="white", font="Helvetica 50")

#END
