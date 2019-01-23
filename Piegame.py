#Piegame.py  A game about making pie
#Cord Corcese  Jan 22, 2019

#Game design: Let's drag things to make a pie 
#Need sprites for pie slices, eggs, milk, flour, and filling. Also rolling pin (All can be coded??)
#So we're going to smash eggs onto a bowl 
#pour in milk
#dump flour
#roll dough
#make fillng 
#Throw in oven 

import pygame
import random
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
step = 0
WHITE = (255,255,255)

class egg():
        hitsLeft = 0
        def __init__(self):
                self.hitsLeft = random.randint(3,5)

        def hitEgg():
                hitsLeft -= 1
                if hitsLeft <=0:
                     crack()
        def drawEgg():
                eggpos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, WHITE, eggpos, 15,0)
        def crack():
                print("egg cracked")

class milk():
        milkLeft = 0
        def __init__():
                milkLeft = 5

class flour():
        flourLeft = 0
        def __init__():
                flourLeft = 5

class filling():
        quality = 0
                

class pie():
        quality = 0

Egg = egg

while keep_going == True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        keep_going = False
        screen.fill((0,0,0))
        if step == 0:
                egg.drawEgg()
        if step == 1:
                print("")
        pygame.display.update()
		
pygame.quit()
