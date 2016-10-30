import pygame
import random
import math
import time
pygame.init()

PI = 3.141592693
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHTBLUE = (100, 100, 255)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
BROWN = (70, 20, 20)
YELLOW = (255, 255, 0)
DARKYELLOW = (204, 204, 0)
changecolor = 0
RANDCOLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

pixel_size = 10

color_list = []
line_loc_list = []
x_position = 0
y_position = 0
x_speed = 1
y_speed = 1
screen_x = 1000
screen_y = 700

headup = 1
headcount = 0

size = (screen_x, screen_y)
screen =  pygame.display.set_mode(size)

pygame.display.set_caption("SQUIRTMAN 2.0")
screen.fill(WHITE)

continuing = True

clock = pygame.time.Clock()

while(continuing == True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuing = False  
    
    changecolor += 1
    memecolor = (changecolor, changecolor, changecolor) 
    randcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    color_list.append(randcolor)
    line_loc_list.append([random.randint(0, screen_x), random.randint(0, screen_y), random.randint(0, screen_x), random.randint(0, screen_y)])
    
    screen.fill(WHITE)
    
    for i in range(len(color_list)):
        pygame.draw.line(screen, color_list[i], [line_loc_list[i][0], line_loc_list[i][1]], [line_loc_list[i][2], line_loc_list[i][3]], 5)
    
    pygame.draw.rect(screen, BLACK, [x_position, 2 * pixel_size + y_position, pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BLACK, [1 * pixel_size + x_position, 1 * pixel_size + y_position, pixel_size, pixel_size])
    pygame.draw.rect(screen, BLACK, [2 * pixel_size + x_position, (0 * pixel_size) + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [5 * pixel_size + x_position, 1 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [6 * pixel_size + x_position, 2 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [7 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [8 * pixel_size + x_position, 3 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, DARKYELLOW, [9 * pixel_size + x_position, 11 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, YELLOW, [10 * pixel_size + x_position, 12 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, DARKYELLOW, [10 * pixel_size + x_position, 13 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, DARKYELLOW, [13 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, YELLOW, [13 * pixel_size + x_position, 11 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, YELLOW, [14 * pixel_size + x_position, 10 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])    
    pygame.draw.rect(screen, BROWN, [6 * pixel_size + x_position, 7 * pixel_size + y_position, 2 * pixel_size, 5 * pixel_size])
    pygame.draw.rect(screen, BROWN, [7 * pixel_size + x_position, 5 * pixel_size + y_position, 2 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BROWN, [8 * pixel_size + x_position, 4 * pixel_size + y_position, 2 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BROWN, [10 * pixel_size + x_position, 3 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])    
    pygame.draw.rect(screen, BLACK, [10 * pixel_size + x_position, 2 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [17 * pixel_size + x_position, 9 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [19 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [17 * pixel_size + x_position, 8 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [18 * pixel_size + x_position, 9 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [16 * pixel_size + x_position, 10 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size]) 
    
    #HeadBob
    if(headup == -1):
        y_position += +pixel_size
    pygame.draw.rect(screen, BLACK, [11 * pixel_size + x_position, 2 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [12 * pixel_size + x_position, 1 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [14 * pixel_size + x_position, (0 * pixel_size) + y_position, 4 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [18 * pixel_size + x_position, 1 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [19 * pixel_size + x_position, 2 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [20 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BLACK, [19 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])    
    pygame.draw.rect(screen, BLACK, [13 * pixel_size + x_position, 9 * pixel_size + y_position, 4 * pixel_size, 1 * pixel_size])
    if(headup == -1):
        pygame.draw.rect(screen, BLACK, [17 * pixel_size + x_position, 8 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])

    pygame.draw.rect(screen, BLUE, [11 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 4 * pixel_size])
    pygame.draw.rect(screen, BLUE, [12 * pixel_size + x_position, 6 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLUE, [13 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLUE, [14 * pixel_size + x_position, 8 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [17 * pixel_size + x_position, 7 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [19 * pixel_size + x_position, 6 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])  
    pygame.draw.rect(screen, LIGHTBLUE, [12 * pixel_size + x_position, 2 * pixel_size + y_position, 7 * pixel_size, 4 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [14 * pixel_size + x_position, 1 * pixel_size + y_position, 4 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [13 * pixel_size + x_position, 6 * pixel_size + y_position, 6 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [12 * pixel_size + x_position, 4 * pixel_size + y_position, 8 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [16 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])  
    pygame.draw.rect(screen, BLACK, [14 * pixel_size + x_position, 5 * pixel_size + y_position, 2 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, WHITE, [15 * pixel_size + x_position, 5 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BROWN, [14 * pixel_size + x_position, 6 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BROWN, [19 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])        
    if(headup == -1):
        y_position += -pixel_size

    pygame.draw.rect(screen, BLACK, [13 * pixel_size + x_position, 9 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [10 * pixel_size + x_position, 11 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [9 * pixel_size + x_position, 10 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [11 * pixel_size + x_position, 8 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [10 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [15 * pixel_size + x_position, 11 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [14 * pixel_size + x_position, 12 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [15 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [12 * pixel_size + x_position, 13 * pixel_size + y_position, 4 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [10 * pixel_size + x_position, 14 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [11 * pixel_size + x_position, 15 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [8 * pixel_size + x_position, 16 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [8 * pixel_size + x_position, 15 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [9 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BLACK, [8 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BLACK, [7 * pixel_size + x_position, 14 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [6 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [5 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 5 * pixel_size])
    pygame.draw.rect(screen, BLACK, [4 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [2 * pixel_size + x_position, 6 * pixel_size + y_position, 3 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [1 * pixel_size + x_position, 5 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [3 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLACK, [2 * pixel_size + x_position, 3 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [1 * pixel_size + x_position, 2 * pixel_size + y_position, 1 * pixel_size, 3 * pixel_size])
    pygame.draw.rect(screen, BLUE, [2 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [2 * pixel_size + x_position, 1 * pixel_size + y_position, 3 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLUE, [3 * pixel_size + x_position, 3 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [4 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [4 * pixel_size + x_position, 3 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLACK, [6 * pixel_size + x_position, 5 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLUE, [5 * pixel_size + x_position, 6 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [5 * pixel_size + x_position, 2 * pixel_size + y_position, 1 * pixel_size, 4 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [6 * pixel_size + x_position, 4 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [9 * pixel_size + x_position, 8 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, LIGHTBLUE, [10 * pixel_size + x_position, 9 * pixel_size + y_position, 3 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, BLUE, [9 * pixel_size + x_position, 9 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, BLUE, [10 * pixel_size + x_position, 10 * pixel_size + y_position, 2 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, WHITE, [10 * pixel_size + x_position, 5 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    pygame.draw.rect(screen, WHITE, [9 * pixel_size + x_position, 7 * pixel_size + y_position, 1 * pixel_size, 1 * pixel_size])
    pygame.draw.rect(screen, WHITE, [8 * pixel_size + x_position, 8 * pixel_size + y_position, 1 * pixel_size, 4 * pixel_size])
    pygame.draw.rect(screen, WHITE, [7 * pixel_size + x_position, 12 * pixel_size + y_position, 1 * pixel_size, 2 * pixel_size])
    
    if(headcount == 30):
        headcount = 0
        headup = headup * -1
    else:
        headcount += 1
    x_position += x_speed
    y_position += y_speed
    if(x_position >= screen_x and y_position >= screen_y):
        x_position
    pygame.display.flip()
    
    clock.tick(round(600 / pixel_size))
        
pygame.quit()    