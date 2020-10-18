import pygame
import time
import random
pygame.init()

display_width =800
display_height = 600
gray=(127,127,127)
black=(0,0,0)
green=(0,200,0)
bright_green=(0,255,0)
red=(200,0,0)
bright_red=(255,0,0)
gamedisplay =  pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("image/car game")
clock = pygame.time.Clock()
carimg = pygame.image.load('image/car.jpg')
bgimg = pygame.image.load('image/download12.jpg')
yellow_strip = pygame.image.load('image/yellow strip.jpg')
strip = pygame.image.load('image/strip.jpg')
start_bg = pygame.image.load('image/start_bg.jpg')
car_width = 56



def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.blit(start_bg,(0,0))
        largetext = pygame.font.SysFont('Broadway', 100)
        textsurf, textrect = text_object('ROAD RAGE', largetext)
        textrect.center = (400,100)
        gamedisplay.blit(textsurf, textrect)
        button('START',100,520,100,50,green,bright_green,"play")
        button('QUIT',210,520,100,50,red,bright_red,"quit")
        pygame.display.update()
        clock.tick(50)

def button(text,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action != None:
            if action == 'play':
                countdown()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
    smalltext = pygame.font.SysFont('Quicksand', 20)
    textsurf, textrect = text_object(text, smalltext)
    textrect.center = ((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(textsurf, textrect)

def score_system(passed,score):
    font = pygame.font.SysFont(None,25)
    text_passed = font.render('Passed : '+str(passed),True,black)
    text_score = font.render('Score : '+str(score),True,black)
    gamedisplay.blit(text_passed,(0,50))
    gamedisplay.blit(text_score, (0, 30))

def obstacle(obs_startx,obs_starty,obs):
    for i in range(6):
        if obs==i:
            obs_pic=pygame.image.load('image/car{}.jpg'.format(i))
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))

def text_object(text,font):
    textsurface = font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',60)
    textsurf,textrect = text_object(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    intro_loop()


def crash(str):
    message_display(str)

def countdown():
    countdown=True
    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            for i in range(3,-1,-1):
                if i == 0:
                    i = 'Go!!'
                gamedisplay.fill(gray)
                background()
                car(display_width*0.40,display_height*0.78)
                largetext = pygame.font.Font('freesansbold.ttf',90)
                textsurf, textrect = text_object(str(i),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplay.blit(textsurf,textrect)
                pygame.display.update()
                clock.tick(1)
            game_loop()


def background():
    gamedisplay.blit(bgimg,(0,0))
    gamedisplay.blit(bgimg,(700,0))
    gamedisplay.blit(yellow_strip, (400, 0))
    gamedisplay.blit(yellow_strip, (400, 100))
    gamedisplay.blit(yellow_strip, (400, 200))
    gamedisplay.blit(yellow_strip, (400, 300))
    gamedisplay.blit(yellow_strip, (400, 400))
    gamedisplay.blit(yellow_strip, (400, 500))
    gamedisplay.blit(strip, (120, 0))
    gamedisplay.blit(strip, (680, 0))

def car(x,y):
    gamedisplay.blit(carimg,(x,y))

def moving_image(rel_y):
    gamedisplay.blit(bgimg, (0, rel_y))
    gamedisplay.blit(bgimg, (700, rel_y))
    gamedisplay.blit(yellow_strip, (400, rel_y))
    gamedisplay.blit(yellow_strip, (400, rel_y + 100))
    gamedisplay.blit(yellow_strip, (400, rel_y + 200))
    gamedisplay.blit(yellow_strip, (400, rel_y + 300))
    gamedisplay.blit(yellow_strip, (400, rel_y + 400))
    gamedisplay.blit(yellow_strip, (400, rel_y + 500))
    gamedisplay.blit(yellow_strip, (400, rel_y - 100))
    gamedisplay.blit(strip, (120, rel_y - 200))
    gamedisplay.blit(strip, (120, rel_y + 20))
    gamedisplay.blit(strip, (120, rel_y + 30))
    gamedisplay.blit(strip, (680, rel_y - 100))
    gamedisplay.blit(strip, (680, rel_y + 20))
    gamedisplay.blit(strip, (680, rel_y + 30))

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.78)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200,(display_width-200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2=7

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change=5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0

        x += x_change
        gamedisplay.fill(gray)
        rel_y = y2%bgimg.get_rect().width
        gamedisplay.blit(bgimg,(0,rel_y-bgimg.get_rect().width))
        gamedisplay.blit(bgimg,(700,rel_y-bgimg.get_rect().width))
        if rel_y<800:
            moving_image(rel_y)
        y2 += obstacle_speed
        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash('Bsdk Road Pe Chala')
        if x>display_width-(car_width+110) or x<110:
            crash('Andha hai kya bsdk')
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx = random.randrange(170,(display_width-170))
            obs = random.randrange(0,6)
            passed += 1
            score = passed*10
            if int(passed)%10 == 0:
                level += 1
                obstacle_speed += 2
                largetext = pygame.font.Font('freesansbold.ttf', 60)
                textsurf, textrect = text_object('Level : '+str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplay.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx + obs_width or x+car_width>obs_startx and x+car_width <obs_startx+obs_width:
                crash('Andha hai kya bsdk')

        pygame.display.update()
        clock.tick(60)
intro_loop()

pygame.quit()
quit()