import pygame as pyg
import random
pyg.init()



# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,255,0)
blue=(0,0,255)
# Creating window
screen_width = 1080
screen_height = 720
gamewindow = pyg.display.set_mode((screen_width, screen_height))

# Game Title
pyg.display.set_caption("Snakes")
pyg.display.update()

# Game specific variables
exit_game = False
game_over = False

# snake position
x=45
y=45

#score
scr=0

#snake lenghi\t

l2=list()

#food positiion
fx =random.randint(50,screen_width-50)
fy =random.randint(50,screen_height-50)
#snake size
sx=30
sy=30
#position changer
velocityx=5
velocityy=0
# frame per second
fps=60
#CLOCK
clock = pyg.time.Clock()
# Game Loop
while not exit_game:
    for event in pyg.event.get():
        
        if event.type == pyg.QUIT:
            exit_game = True

        if event.type == pyg.KEYDOWN:
            if event.key==pyg.K_RIGHT:
                velocityx=5
                velocityy=0

            if event.key==pyg.K_LEFT:
                velocityx=-5
                velocityy=0

            if event.key==pyg.K_UP:
                velocityx=0
                velocityy=-5

            if event.key==pyg.K_DOWN:
                velocityx=0
                velocityy=5
            if event.key==pyg.K_p:
                velocityx=0
                velocityy=0

    if (x-fx)<20 and (x-fx)>-20 and(y-fy)<20 and (y-fy)>-20 :
        fx=random.randint(80,screen_width-100)
        fy=random.randint(50,screen_height-80)
        scr=scr+1

    

    x=x+velocityx
    y=y+velocityy

    gamewindow.fill(green)

    pyg.draw.rect(gamewindow, blue, [80,50,920,640])
    


    pyg.draw.rect(gamewindow, black, [x,y,sx,sy])
    pyg.draw.rect(gamewindow, white, [x+5,y+5,20,20])
    pyg.draw.rect(gamewindow, red, [fx,fy,sx,sy])
    
    

    pyg.display.update()
    clock.tick(fps)

pyg.quit()
quit()
