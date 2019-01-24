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
import math
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
step = 0
WHITE = (255,255,255)
DATPINK = (249,119,188)
DATBLUE = (0,204,204)
pygame.mixer.init()
Cambria = pygame.font.SysFont("Cambria",24)



class egg:
        def __init__(self): #init
                self.hitsLeft = random.randint(3,5)
                self.eggpos = pygame.mouse.get_pos()

        def hitEgg(self,step):  #Updates egg when hit
                print("hit egg")
                self.hitsLeft -= 1
                if self.hitsLeft <=0:
                        return self.crack(step)
                else:
                        return 0
                     
        def drawEgg(self): #Draws the egg in pygame
                self.eggpos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, WHITE, self.eggpos, 15,0)
                
        def crack(self,stage): #Egg has cracked, set to next step
                print("egg cracked")
                stage =1
                return stage



class milk:
        milkLeft = 0
        def __init__(self): #init
                self.milkLeft = 500
                self.milkpos = pygame.mouse.get_pos()
                self.angle = 0
                self.rightDown = False
                self.leftDown = False 
        def drawMilk(self): #Draws milk carton on screen
                self.milkpos = pygame.mouse.get_pos()
                pygame.draw.rect(screen,DATPINK,(self.milkpos[0],self.milkpos[1],150,300))
        def rotateLeft(self): #rotates left
                self.angle = self.angle+1
                if self.angle >= 180:
                        self.angle = -179
        def rotateRight(self): # rotates right
                self.angle -=1
                if self.angle <= -180:
                        self.angle = 179
        def pourMilk(self): #Pours milk 
                if self.milkLeft > 0:
                        self.milkLeft -=5
                if self.milkLeft < 0:
                        self.milkLeft = 0
        
class milkDrop:
        def __init__(self):
                self.speed = 0
        def fall():
                self.speed += 3
class flour:
        def __init__():
                flourLeft = 5

class filling:
        quality = 0
                

class pie:
        quality = 0

class bowl:
        def drawbowl():
                pygame.draw.rect(screen, DATBLUE,(250,400,250,50) ) #draws bowl at fixed location with fixed size

Egg = egg()
Milk = milk() #Delcare class objects outside of game loop to prevent redeclaring every loop (can be better?) 
print(Egg.hitsLeft)

while keep_going == True:
        for event in pygame.event.get(): #Loop to check for user quiting game
                if event.type == pygame.QUIT:
                        keep_going = False
                        
        screen.fill((0,0,0)) #Removes old sprites
        bowl.drawbowl()
        if step == 0: #egg stage 
                Egg.drawEgg()
                EggString = "Crack the egg!"
                text = Cambria.render(EggString, True,WHITE)
                textBox = text.get_rect()
                textBox.centerx = screen.get_rect().centerx
                screen.blit(text,textBox)
                speed = math.sqrt(pygame.mouse.get_rel()[0]**2 + pygame.mouse.get_rel()[1]**2) #Converts vector into scalar
                if speed > 20 and Egg.eggpos[0] > 250 and Egg.eggpos[0] < 500 and Egg.eggpos[1]>400 and Egg.eggpos[1] < 450: #Ugly collision and speed check
                        step = Egg.hitEgg(step)
        if step == 1: #Milk step
                Milk.drawMilk()
                MilkString = "Pour the Milk! Milk left: " + str(Milk.milkLeft)
                Milktext = Cambria.render(MilkString, True, WHITE)
                textBox = Milktext.get_rect()
                textBox.centerx = screen.get_rect().centerx
                screen.blit(Milktext,textBox)
                if pygame.key.get_pressed()[pygame.K_RIGHT]: #Checks if right arrow key is pressed down
                        Milk.rotateRight()
                        print("angle: ", Milk.angle)
                if pygame.key.get_pressed()[pygame.K_LEFT]: #Checks if left arrow key is pressed down
                        Milk.rotateLeft()
                        print("angle: ", Milk.angle)
                if (Milk.angle > 90 or Milk.angle < -90) and Milk.milkLeft > 0: #Pours milk if carton is tilted enough (Move into Milk class?)
                        Milk.pourMilk()
                        print("Milk left: ", Milk.milkLeft)
        pygame.display.update() #Updates display

		
pygame.quit()
