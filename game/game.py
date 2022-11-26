
import pygame
#from pygame import mixer, font
from random import randint
import os
"""
Copyright © 2022 Kingve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#limit backward movement, or store old variable pos in x and use scroll like that
# GLOBAL VARIABLES
pygame.init()
RED = (255, 0, 0)
GREEN = (47, 120, 1)
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500
GREEN = (17, 186, 11)
LEVEL = (0)
jumping = 0
dash = 1
score = 0
precalrect = 0
curx = 0
# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width, img, imgpath):
        super().__init__()
        if img == 0:
            #loading a texture void sprite
            self.image = pygame.Surface([width, height])
            self.image.fill(SURFACE_COLOR)
            self.image.set_colorkey(COLOR)
            pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
            self.rect = self.image.get_rect()
        if img == 1:
            #loading a custom sprite
            self.image = imgpath
            self.rect = self.image.get_rect()
        else:
            print("Unexpected error with sprite texture (li. 48) img either 0 or 1 and int.")

  
  
    def outsidecam(self, var):
        global platformx
        global platform1x
        global platform2x
        rectprex = self.rect.x
        #redifining GLOBAL variabes
        if rectprex < -20:
            #we have to constantly recalculate the edges
            #randomly add at right side of screen
            # change values for random x placement as well as random y placement

#            self.rect.x = object_.rect.x + 475
            self.rect.y = randint(40, 70)
            if var == 1:
                platformx = platformx + 450

            if var == 2:
                platform1x = 0
                platform1x = platformx + randint(60, 80)
            
            if var == 3:
                platform2x = 0
                platform2x = platform1x + randint(60, 80)

        if rectprex > 500:

            self.rect.y = randint(40, 70)
            if var == 1:
                platformx = 0

            if var == 2:
                platform1x = randint(60, 80)

            if var == 3:
                platform1x = randint(80, 100)
        

    def ad(self, prex):
        global x
        global precalrect
        dist = 2
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            #instedddad of moving the player we make another keyboard for platform
            precalrect = prex
            self.rect.x = precalrect + x
            x = x - dist 
        if key[pygame.K_a]:
            x = x + dist

#we only want the x cord once, then we add to it We could try lists
#        precalrect = self.rect.x
#instead of defining the x in the function (which causes sliding), we instead ask the sprite to provide their spawn x cord, which does cause a little more jumble, but in might actually finally please work.
            precalrect = prex
            self.rect.x = precalrect + x
    def keyboard(self):
        key = pygame.key.get_pressed()
        dist = 5
        #defining globals
        global y
        global x 
        global gravset
        global gravity2
        global jumping
        global dash
        global score
        gravset = 1
        dev = 0
        if dev:
            if key[pygame.K_w]:
                y = y - dist
                gravset = 0
                gravity2 = 0
            if key[pygame.K_s]:
                #for s we make it so the platforms move, instead of the player
                y = y + dist
        if key[pygame.K_x]:
            if jumping:
                if dash == 1: 
                    x = x - 80
                    dash = 0
                #make more balanced also cooldown, but overall dash is a good idea
            else:
                dash = 1
        if key[pygame.K_SPACE]:
            score = score + 1
            if jumping == 0:
                jumping = 1
                y = y - dist
#                gravset = 0
                gravity2 = 4
#160, 500
        collide1 = pygame.Rect.colliderect(self.rect, platform.rect)
        collide2 = pygame.Rect.colliderect(self.rect, platform1.rect)
        collide3 = pygame.Rect.colliderect(self.rect, platform2.rect)
        collide = 0 + collide1 + collide2 + collide3
        if gravset == 1:
            #implies to python that collide = 1, so if you're touching any platform it will return a one if none are being touched it gives a 0
            if collide:
                #if we touch then execute:
                jumping = 0
                dash = 1
            else:
                #if we aren't currently touching execute:
                gravity2 = gravity2 - 0.1
                #slowly build up gravity, then add the added gravity to the player's movement
                y = y - gravity2
#respawn loop, if you exit the bottom of the screen, then you are automatically put back to the start of the level
        global platformx
        if y > 500:
            x = platformx + 7
            jumping = 0
            y = 0
            pygame.display.update()
            gravity2 = 0
#            object_.rect.x = x
            object_.rect.y = y
        object_.rect.y = y
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
try:
    #player sprite
    spriteimage = pygame.image.load(os.path.join('c:/', 'Users', "levic", "Python_files", "Masterworks", "Assets", "player2.png" )).convert_alpha()
    cloudpng = pygame.image.load(os.path.join('c:/', 'Users', "levic", "Python_files", "Masterworks", "Assets", "cloud.png" )).convert_alpha()
except:
    print("PANIC --- ERROR::SPRITES NOT FOUND")
pygame.display.set_caption("IM LOSING MY MINDDD LETS GOOOO POGGIES OWOWOWOW HOW DOES GRAVITY VARIABLES NOT WORK")
all_sprites_list = pygame.sprite.Group() 
#define sprites
object_ = Sprite(RED, 20, 25, 1, spriteimage)
all_sprites_list.add(object_)
platform = Sprite(GREEN, 20, 25, 0, "")
platformx = 0
platform.rect.x = platformx
platform.rect.y = 100
all_sprites_list.add(platform)

platform1 = Sprite(GREEN, 10, 25, 0, "")
platform1x = randint(40, 70)
platform1.rect.x = platform1x
platform1.rect.y = randint(20, 70)
all_sprites_list.add(platform1)

platform2 = Sprite(GREEN, 10, 25, 0, "")
platform2x = platform1x + randint(40, 70)
platform2.rect.x = platform2x
platform2.rect.y = randint(20, 70)
all_sprites_list.add(platform2)

y = int(0)
x = int(0)
gravity2 = 0

gravity2 = 0
exit = True
clock = pygame.time.Clock()
gravset = 1

def varrun():
    object_.keyboard()
    #1 is for 1st platform 2 for second ect ect
    #we still move x so i need to constantly calculate edge of screen.
    platform.outsidecam(var=1)
    platform1.outsidecam(var=2)
    platform2.outsidecam(var=3)
    platform.ad(prex=platformx)
    platform1.ad(prex=platform1x)
    platform2.ad(prex=platform2x)
def regetxval():
    global platformx
    global platform1x
    platformx = platform.rect.x
    platform1x = platform1.rect.x
    
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    varrun()
    object_.rect.y = y
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    #or use pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
  
pygame.quit()
#check if it breaks after 13050 so after a little while of jumping if the game just stops putting the platforms, in which case we can use the reset to reset the game cords but not the acutal data from the game besides x and y right because we just spawn it back the begining one before the error happens so it looks infinite but it isn't too much for the computer to handle.
