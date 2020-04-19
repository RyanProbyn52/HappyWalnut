import pygame
import random

pygame.init()

dis_width = 500
dis_height = 500

win = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Happy Walnut")

run = True
jump = False
start = True

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)

def initialise():
    walnut = pygame.image.load('walnut2.png')
    x = 60
    y = 350
    height = 40
    width = 40
    counter = 0
    y_bar = random.randint(100, 200)
    bar_pos = 0
    highscore = 0
    score = 0
    return walnut, x, y, height, width, counter, y_bar, bar_pos, highscore, score

def text_object(text, font, colour):
    textSurf = font.render(text, True, colour)
    return textSurf, textSurf.get_rect()

def message_display(text, font_size, x_coord, y_coord, colour):
    font = pygame.font.Font('freesansbold.ttf', font_size) 
    textSurf, textRect = text_object(text, font, colour) 
    textRect.center = (x_coord, y_coord)
    win.blit(textSurf, textRect)
    
def reset(score, highscore):
    if score > highscore:
        highscore = score        
    jump = False 
    start = True        
    y = 350
    counter = 0
    bar_pos = 0
    y_bar = random.randint(80, 280)
    return jump, start, y, counter, bar_pos, y_bar, score, highscore

def home_screen(start, jump, score, highscore):
    while start: 
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        keys = pygame.key.get_pressed() #pressing space will start game          
        if keys[pygame.K_SPACE]:
            jump = True
            start = False
            score = 0
            
        win.fill(black) #refreshing display
        message_display('Happy Walnut', 38, 250, 150, green)
        message_display('Highscore: %d'%highscore, 22, 250, 220, white)
        message_display('Previous score: %d'%score, 18, 250, 250, white)
        message_display('Press --space-- to begin', 26, 250, 420, white)
        win.blit(walnut,(x,y))
        pygame.display.update()
        
    return jump, start, score

def jump_func(y, counter):
    y -= (20 - counter)
    counter += 2
    
    return y, counter
    
  
#initialising variables
walnut, x, y, height, width, counter, y_bar, bar_pos, highscore, score = initialise()

while run:
    jump, start, score = home_screen(start, jump, score, highscore)
    pygame.time.delay(40)
    
    if jump:
        y, counter = jump_func(y, counter)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
  
    if keys[pygame.K_SPACE]:
        jump = True
        counter = 0
    win.fill((0,0,0))
    pygame.draw.rect(win, white, (500 - bar_pos,0,50,y_bar))
    pygame.draw.rect(win, white, (500 - bar_pos,y_bar + 150,50,500 - y_bar))

    if y < 0 or y > 600: #collision test for bottom and top
        jump, start, y, counter, bar_pos, y_bar, score, highscore = reset(score, highscore)
        
    if 500 - bar_pos < x + 35 and 500 - bar_pos > x - 5: #collision check for front edge of box
        if y < y_bar or y > y_bar + 130:
            jump, start, y, counter, bar_pos, y_bar, score, highscore = reset(score, highscore)
            
    if 500 - bar_pos < x - 5 and 500 - bar_pos > x - 45: #collision check for front edge of box
        if y < y_bar or y > y_bar + 130:
            jump, start, y, counter, bar_pos, y_bar, score, highscore = reset(score, highscore)
    

    win.blit(walnut,(x,y))
    message_display('score: %d'%score, 18, 450, 10, green)
    pygame.display.update()
    bar_pos += 8
    if bar_pos == 560:
        bar_pos = 0
        y_bar = random.randint(80, 280)
        score += 1
             
pygame.quit()