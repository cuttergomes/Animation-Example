import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


pygame.init()
screen_y = 500
screen_x = 500
snow_list = []
for i in range(50):
    snow_list.append([random.randint(0, screen_x), random.randint(0, screen_y)])
size = (500, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


color_list = []
for i in range(50):
    randcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color_list.append(randcolor)
    
done = False


clock = pygame.time.Clock()


while(not done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    randcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    screen.fill(BLACK)
    
    for i in range(len(snow_list)):
        
        x = snow_list[i][0]
        y = snow_list[i][1]
        
        for b in range(100):
            pygame.draw.circle(screen, (color_list[i][0], color_list[i][1],color_list[i][2]), [x - b, y - b], 1)
        
        snow_list[i][1] += 2
        snow_list[i][0] += 2
        
        if(snow_list[i][1] >= screen_y + b):
            snow_list[i][1] = 0
            snow_list[i][0] = random.randint(0, screen_x)
            randcolor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color_list[i] = randcolor
            
        if(snow_list[i][0] >= screen_x + b):
            snow_list[i][0] = 0
            snow_list[i][1] = random.randint(0, screen_y)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()