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


#Start setup 
import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
step = 0

#Colours below
WHITE = (255,255,255)
DATPINK = (249,119,188)
DATBLUE = (0,204,204)
#End Colours

pygame.mixer.init()
clock = pygame.time.Clock()
Cambria = pygame.font.SysFont("Cambria",24)
MilkCarton = pygame.image.load("Milkcarton.bmp").convert_alpha()
sprite_list = pygame.sprite.Group()
FlourCloud = pygame.image.load("Flourcloud.png").convert_alpha()
Flourbag = pygame.image.load("Flourbag.png").convert_alpha()
Knife = pygame.image.load("knife.png").convert_alpha()
RollingPin = pygame.image.load("Rollingpin.png").convert_alpha()

apple = pygame.image.load("Apple.png").convert_alpha()
pumpkin = pygame.image.load("Pumpkin.png").convert_alpha()
berry = pygame.image.load("Berry.png").convert_alpha()
lemon = pygame.image.load("Lemon.png").convert_alpha()

doughball = pygame.image.load("Doughball.png").convert_alpha()
rolleddough = pygame.image.load("RolledDough.png").convert_alpha()
PieTin = pygame.image.load("PieTin.png")
fullPieTin = pygame.image.load("fullPieTin.png")


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

#End egg class


class milk(pygame.sprite.Sprite):
        def __init__(self): #init, sets up sprite
                pygame.sprite.Sprite.__init__(self)
                self.milkLeft = 500
                self.milkpos = (-50,-50)
                self.OGimage = MilkCarton
                self.image = MilkCarton
                self.rect = self.image.get_rect()
                self.rect.x = self.milkpos[0]
                self.rect.y = self.milkpos[1]
                self.angle = 0
                self.rightDown = False #What dis for? 
                self.leftDown = False 
                sprite_list.add(self)

                
        def drawMilk(self): #Draws milk carton on screen
                self.milkpos = pygame.mouse.get_pos()
                self.rect.x = self.milkpos[0]
                self.rect.y = self.milkpos[1]
                #pygame.draw.rect(screen,DATPINK,(self.milkpos[0],self.milkpos[1],150,300))

                
        def rotateLeft(self): #rotates left
                self.image = pygame.transform.rotate(self.OGimage,self.angle)  #See note in rotateLeft below about code source
                self.angle = self.angle+1 %360
                if self.angle >359:
                        self.angle = 0

                        
        def rotateRight(self): # rotates right
                self.image = pygame.transform.rotate(self.OGimage,self.angle)    #first 2 Rotation code implemented from Stack Overflow user Ted Klein Bergman https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
                self.angle = self.angle-1 %360
                if self.angle < -359:
                        self.angle = 0
                

                        
        def pourMilk(self, array): #Pours milk 
                if self.milkLeft > 0:
                        self.milkLeft -=5
                        Drop = milkDrop(self)
                        array.append(Drop)
                        
                if self.milkLeft < 0:
                        self.milkLeft = 0
        def Removeself(self): #Removes sprite instance
                self.kill()

# End milk class


        
class milkDrop: #Class for falling milk drops. Yet to be impletmented
        def __init__(self,milk):
                self.speed = 0
                self.droppos = milk.milkpos
        def fall(self, bowl,array,index): #Updates drop as it falls
                self.droppos = (self.droppos[0],int(self.droppos[1]+speed)) 
                self.speed += 3
                pygame.draw.circle(screen, WHITE, self.droppos, 5,0)
                if self.droppos[0] < bowl.X+bowl.width and self.droppos[0] > bowl.X and self.droppos[1] > bowl.Y and self.droppos[1] < bowl.Y + bowl.height : #If collides with bowl, update bowl then delete instance
                        bowl.milkrequired -= 5
                        self.selfDestruct(array,index)
                if self.droppos[1] > 600: #If reached bottom of screen, delete instance. CHANGE TO VARIABLE SCREEN SIZES!!!
                        self.selfDestruct(array,index)
        def selfDestruct(self,array,index): #Deletes instance
                del array[index]


#End Milk Drop class 

                
class flour(pygame.sprite.Sprite):
        def __init__(self): #Initilizes sprite instance
                pygame.sprite.Sprite.__init__(self)
                self.flourLeft = 500
                self.OGimage = Flourbag
                self.image = Flourbag
                self.flourpos = (-50, 200)
                self.rect = self.image.get_rect()
                self.rect.x = self.flourpos[0]
                self.rect.y = self.flourpos[1]
                self.angle = 0
                sprite_list.add(self)

        def drawFlour(self): #Updates flour sprite 
                self.flourpos = pygame.mouse.get_pos()
                self.rect.x = self.flourpos[0]
                self.rect.y = self.flourpos[1]
                
        def pourFlour(self, array): #Creates flour_float objects
                if self.flourLeft > 0:
                        size = random.randint(1,10)
                        if size > self.flourLeft:
                                size = self.flourLeft
                        self.flourLeft -= size
                        Cloud = flour_float(size,self)
                        array.append(Cloud)
                if self.flourLeft < 0:
                        self.flourLeft = 0
                

        def rotateLeft(self): #rotates left
                self.image = pygame.transform.rotate(self.OGimage,self.angle)  #See note in rotateLeft below about code source
                self.angle = self.angle+1 %360
                if self.angle >359:
                        self.angle = 0

        def rotateRight(self): # rotates right
                self.image = pygame.transform.rotate(self.OGimage,self.angle)    #first 2 Rotation code implemented from Stack Overflow user Ted Klein Bergman https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
                self.angle = self.angle-1 %360
                if self.angle < -359:
                        self.angle = 0





#End flour Class




class flour_float(pygame.sprite.Sprite):
        def __init__(self, size, flour): #init function, cretes the sprite instance
                pygame.sprite.Sprite.__init__(self)
                self.image = FlourCloud
                self.size = size
                self.floatpos = flour.flourpos
                self.rect = self.image.get_rect()
                self.rect.x = self.floatpos[0]
                self.rect.y = self.floatpos[1]
                self.floatright = True
                self.step = 0
                sprite_list.add(self)
                
        def float(self,bowl,array, index): # Updates sprite as it floats down
                if self.floatright == True:
                        self.floatpos = (self.floatpos[0]+3,self.floatpos[1]+3)
                else:
                        self.floatpos = (self.floatpos[0]-3,self.floatpos[1]+3)
                self.step += 1
                if self.step >= 5:
                        if self.floatright == True:
                                self.floatright = False
                                step = 0
                        else:
                                self.floatright = True
                                step = 0
                self.rect.x = self.floatpos[0]
                self.rect.y = self.floatpos[1]
                if self.floatpos[0] < bowl.X+bowl.width and self.floatpos[0] > bowl.X and self.floatpos[1] > bowl.Y and self.floatpos[1] < bowl.Y + bowl.height : #If collides with bowl, update bowl then delete instance
                        bowl.flourrequired -= self.size
                        self.selfDestruct(array,index)
                if self.floatpos[1] > 600: #If reached bottom of screen, delete instance. CHANGE TO VARIABLE SCREEN SIZES!!!
                        self.selfDestruct(array,index)
  
        def selfDestruct(self,array,index): #Destroys sprite instance 
                del array[index]
                self.kill()


#End flour_float class




class filling(pygame.sprite.Sprite):

        #Block of universal class constants
        ScreenString = "What type of pie would you like to make?"
        ScreenText = Cambria.render(ScreenString,True, WHITE)
        textbox = ScreenText.get_rect()
        textbox.centerx = screen.get_rect().centerx
        AppleString = "Apple"
        AppleText = Cambria.render(AppleString,True,WHITE)
        Applebox = AppleText.get_rect()
        PumpkinString = "Pumpkin"
        PumpkinText = Cambria.render(PumpkinString,True,WHITE)
        PumpkinBox = PumpkinText.get_rect()
        Berry = "Berry"
        BerryText = Cambria.render(Berry,True,WHITE)
        BerryBox = BerryText.get_rect()
        LemonMeraine = "Lemon maraine"
        LemonText = Cambria.render(LemonMeraine,True,WHITE)
        LemonBox = LemonText.get_rect()
        #End of class universals
        def __init__(self):
                self.type = "null"
                self.step = 0
        def ChooseFilling(self, Mouseclick):  #Deterimes what type of pie to make. Takes a boolean to determine when the mouse was clicked
                screen.blit(filling.ScreenText,filling.textbox)
                AppleButton = button(filling.AppleText,WHITE,(200,200))
                if AppleButton.drawButton(Mouseclick) == True:
                        self.type = "Apple"
                        print("Apple")
                PumpkinButton = button(filling.PumpkinText, WHITE, (500,200))
                if PumpkinButton.drawButton(Mouseclick) == True:
                        self.type = "Pumpkin"
                        print("Pumpkin")
                BerryButton = button(filling.BerryText, WHITE, (200, 250))
                if BerryButton.drawButton(Mouseclick) == True:
                        self.type = "Berry"
                        print("Berry")
                LemonButton = button(filling.LemonText, WHITE, (500, 250))
                if LemonButton.drawButton(Mouseclick) == True:
                        
                        self.type = "Lemon"
                        print("Lemon")
                if self.type != "null": #Returns true to show choice has been made
                        return True
        def Make_Filling(self,knife): #Where the pie filling is made
                if self.step == 0:
                        if self.type == "Apple":
                                self.FruitSprite = fruit("Apple",(250,250))
                                self.step = 1
                        if self.type == "Pumpkin":
                                self.FruitSprite = fruit("Pumpkin",(250,250))
                                self.step = 1
                        if self.type == "Berry":
                                self.FruitSprite = fruit("Berry",(250,250))
                                self.step = 1
                        if self.type == "Lemon":
                                print("We'll make a Lemon Meraine pie")
                                self.FruitSprite = fruit("Lemon",(250,250))
                                self.step = 1 
                elif self.step == 1:
                        if self.FruitSprite.cut(knife) == True:
                                self.step = 2
                elif self.step == 2:
                        print("add sugar")
                        return True
                        
                          
#End filling Class

class knife(pygame.sprite.Sprite):
        def __init__(self, pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = Knife
                self.OGimage = Knife
                self.pos = pos
                self.rect = self.image.get_rect()
                self.rect.x=pos[0]
                self.rect.y=pos[1]
                sprite_list.add(self)
                
        def move(self,pos):
                self.rect.x = pos[0]
                self.rect.y = pos[1]


#End knife class


class fruit(pygame.sprite.Sprite):
        def __init__(self,fruit,pos): #init function, chooses what type of fruit it is (maybe subclasses would be better?
                if fruit == "Apple":
                        self.type = Apple(pos)
                if fruit == "Pumpkin":
                        self.type = Pumpkin(pos)
                if fruit == "Berry":
                        self.type = Berry(pos)
                if fruit == "Lemon":
                        self.type = Lemon(pos)
        def move(self,pos):
                self.type.move(pos)
        def cut(self,knife):
                self.type.cut(knife)
                
#start fruit subclasses      
                        
class Apple(fruit): #Class for Apple objects 
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = apple
                self.OGimage = apple
                self.pos = pos
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                self.stage = 0
                sprite_list.add(self)
                self.HP = random.randint(4,10)
        def move(self,pos):
                self.rect.x = pos[0]
                self.rect.y = pos[1]
        def cut(self,knife):
                if self.rect.colliderect(knife.rect) and self.stage == 0:
                        self.HP -= 1
                        if self.HP <= 0:
                                print("Apple Cut")
                                self.stage = 1
                        else:
                                return False
                if self.stage == 1:
                        self.kill()
                        return True
        
                

class Pumpkin(fruit): #Class for Pumpkin objects
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = pumpkin
                self.OGimage = pumpkin
                self.pos = pos
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                sprite_list.add(self)
        def move(self,pos):
                self.rect.x = pos[0]
                self.rect.y = pos[1]

class Berry(fruit): #Class for berry objects
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = berry
                self.OGimage = berry
                self.pos = pos
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                sprite_list.add(self)
        def move(self, pos):
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                
class Lemon(fruit): #Class for Lemon objects
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = lemon
                self.OGimage = lemon
                self.pos = pos
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                sprite_list.add(self)
        def move(self, pos):
                self.rect.x = pos[0]
                self.rect.y = pos[1]

#End fruit subclasses

class button: #Class used to make buttons
        def __init__(self,text,colour,pos):
                self.text = text
                self.colour = colour
                self.textbox = text.get_rect()
                self.textbox.centerx = pos[0]
                self.textbox.centery = pos[1]
        def drawButton(self, Mouseclick): #Draws a button and deterimes if it was clicked. Returns a boolean value
                screen.blit(self.text,self.textbox)
                mousepos = pygame.mouse.get_pos()
                if mousepos[0] > self.textbox.x and mousepos[0] < self.textbox.x+self.textbox.width and mousepos[1] > self.textbox.y and mousepos[1] < self.textbox.y + self.textbox.height: #Checks if mouse is in bounds of the button
                        if Mouseclick == True:
                                return True
                
#End button class


class rollingPin:
        def __init__(self):
                pygame.sprite.Sprite.__init__(self, pos)
                self.image = RollingPin
                self.OGimage = RollingPin
                
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                sprite_list.add(self)
        def move(self,pos): #Moves rolling pin sprite
                self.rect.x = pos[0]
                self.rect.y = pos[1]

class pietin:
        def __init__(self,pos):
                pygame.sprite.Sprite.__init__(self)
                self.image = PieTin
                self.OGimage = PieTin
                self.rect = self.image.get_rect()
                self.rect.x = pos[0]
                self.rect.y = pos[1]
                self.has_dough = False
                sprite_list.add(self)
        def adddough(self): # Adds dough to the pie tin
                self.image = fullPieTin
                self.has_dough = True

class pie:
        def __init__(self, filling):
                self.quality = 0
                self.doughstep = 0
                self.isBaked = False
        def MakeDough(self): #Goes through steps to roll the dough
                if self.doughstep == 0:
                        pygame.sprite.Sprite.__init__(self, pos)
                        self.pin = rollingPin()
                        self.image = doughball
                        self.OGimage = doughball
                        self.doughstep = 1
                        
                elif self.doughstep == 1:
                        self.pin.move(pygame.mouse.get_pos())
                        #if pin collides with doughball, roll it a bit
                elif self.doughstep == 2:
                        self.image = rolleddough
                        
                #step 3:
                        #now we put in the filling
        def BakePie(): #Pie is put into the oven and then baked 
                #set image to unbaked pie
                #make oven asset
                #Put pie in oven
                #turn it on
                #take it out
                #Yay pie
                self.placeholder = 1 
                


#End pie Class

class bowl:
        def __init__(self):
                self.milkrequired = 300
                self.flourrequired = 250
                self.X = 250
                self.Y = 400
                self.width = 250
                self.height = 100
        def drawbowl(self): #Draws the bowl on screen
                pygame.draw.rect(screen, DATBLUE,(self.X,self.Y,self.width,self.height) ) #draws bowl


#End bowl class 







Egg = egg()
Bowl = bowl()
Milk = milk() #Delcare class objects outside of game loop to prevent redeclaring every loop (can be better?) 
print(Egg.hitsLeft)
Milkdrops=[]
Flour = flour()
Flourclouds = []
Filling = filling()
MouseClicked = False
CuttingKnife = knife((0,0))
Pie = pie(Filling)
#end of setup



# Start Main game loop

while keep_going == True:
        
        for event in pygame.event.get(): #Loop to check for user quiting game
                if event.type == pygame.QUIT:
                        keep_going = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        MouseClicked = True
                        print("mouse click detected")
                        
                        
        screen.fill((0,0,0)) #Removes old sprites
        Bowl.drawbowl()
        if step == 0: #egg stage 
                Egg.drawEgg()
                EggString = "Crack the egg!"
                text = Cambria.render(EggString, True,WHITE) #Writes text in pygame window
                textBox = text.get_rect()
                textBox.centerx = screen.get_rect().centerx
                screen.blit(text,textBox)
                speed = math.sqrt(pygame.mouse.get_rel()[0]**2 + pygame.mouse.get_rel()[1]**2) #Converts vector into scalar
                if speed > 20 and Egg.eggpos[0] > 250 and Egg.eggpos[0] < 500 and Egg.eggpos[1]>400 and Egg.eggpos[1] < 450: #Ugly collision and speed check
                        step = Egg.hitEgg(step)

                        
        if step == 1: #Milk step
                
                Milk.drawMilk()
                
                MilkString = "Pour the Milk! Milk left: " + str(Milk.milkLeft)+ " Milk needed: " + str(Bowl.milkrequired) #Writes text in pygame window
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
                        Milk.pourMilk(Milkdrops)
                        print("Milk left: ", Milk.milkLeft)
                dropidx = 0 
                for drop in Milkdrops: #Tracks list of milk drops
                        drop.fall(Bowl,Milkdrops,dropidx)
                        dropidx += 1
                if (Bowl.milkrequired <= 0 and Milkdrops == []) or (Milk.milkLeft <= 0 and Milkdrops == []):
                        Milk.Removeself()
                        step = 2

                        
        if step == 2: #Flour step
                Flour.drawFlour()

                FlourString = "Pour the flour! Flour left: " + str(Flour.flourLeft) + " Flour needed: " + str(Bowl.flourrequired)
                Flourtext = Cambria.render(FlourString, True, WHITE)
                textbox = Flourtext.get_rect()
                textbox.centerx = screen.get_rect().centerx
                screen.blit(Flourtext,textbox)

                if pygame.key.get_pressed()[pygame.K_RIGHT]: #Checks if right arrow key is pressed down
                        Flour.rotateRight()
                        print("angle: ", Flour.angle)
                if pygame.key.get_pressed()[pygame.K_LEFT]: #Checks if left arrow key is pressed down
                        Flour.rotateLeft()
                        print("angle: ", Flour.angle)
                if (Flour.angle > 90 or Flour.angle < -90) and Flour.flourLeft > 0: #Pours flour if bag is tilted enough (Move into flour class?)
                        Flour.pourFlour(Flourclouds)
                        print("Flour left: ", Flour.flourLeft)
                dropidx = 0 
                for cloud in Flourclouds: #Tracks list of flour clouds
                        cloud.float(Bowl,Flourclouds,dropidx)
                        dropidx += 1
                if (Bowl.flourrequired <= 0 and Flourclouds == []) or (Flour.flourLeft <= 0 and Flourclouds == []):
                        print("Step 3 reached")
                        Flour.kill()
                        step = 3 

        if step == 3:
                if Filling.ChooseFilling(MouseClicked) == True:
                        step = 4
        if step == 4:
                if Filling.Make_Filling(CuttingKnife) == True:
                        step = 5
                CuttingKnife.move(pygame.mouse.get_pos())
        if step == 5:
                Pie.MakeDough()
                
        MouseClicked = False
        sprite_list.update()
        sprite_list.draw(screen)
        pygame.display.update() #Updates display
        clock.tick(60)
		
pygame.quit()
