#TODO: add code to have a wall, then an island below, and a wall slide || python -m PyInstaller --onefile --hidden-import=pygame addstory.py || start btn 80px by 40heightpx
#add so it makes a
try:
    import pygame
    #from pygame import mixer, font
    from random import randint
    import os
    import sys
    from time import sleep
    import threading
    import webbrowser
except:
    resetcode = "\033[0m"
    redcode = "\033[31m"
    boldcode = '\033[01m'
    yellowcode = '\033[93m'
    print(redcode, boldcode, "!!fatal error!!")
    print(yellowcode, "modules missing, to get more detailed versions the modules are listed below")
    #clean up color so console doesn't stay red or whatever color
    print(resetcode, "resetting console to default color")
    exit()
   
if sys.platform != "win32":
    print("only av for win")
    print("the system found your system was:", sys.platform())
    exit()
print("Copyright © 2022 Kingve Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
"""
Copyright © 2022 Kingve

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#limit backward movement, or store old variable pos in x and use scroll like that
# GLOBAL VARIABLES
pygame.init()
pygame.font.init()
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
musicstat = 1
shake = 0
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
            print("Unexpected error with sprite texture (li. 55) img either 0 or 1 and int, if this error is unexpected please contact AGHASTMUFFIN")

  
  
    def outsidecam(self, var):
        global platformx
        global platform1x
        global platform2x
        global platform3x
        global platform4x
        global platform5x
        rectprex = self.rect.x
        width1, h = pygame.display.get_surface().get_size()
        #redifining GLOBAL variabes
        if rectprex <= -40:
            #we have to constantly recalculate the edges
            #randomly add at right side of screen
            # change values for random x placement as well as random y placement

#            self.rect.x = object_.rect.x + 475
            self.rect.y = randint(40, 70)
            if var == 1:
                platformx = platformx + width1 - 50

            if var == 2:
                platform1x = 0
                platform1x = platformx + randint(60, 80)
            
            if var == 3:
                platform2x = 0
                platform2x = platform1x + randint(60, 80)
            
            if var == 4:
                platform3x = 0
                platform3x = platform2x + randint(60, 80)
            if var == 5:
                platform4x = 0
                platform4x = platform3x + randint(60, 80)
            if var == 6:
                platform5x = 0
                platform5x = platform4x + randint(60, 80)
        if rectprex > width1:

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
        dist = 1.33333333
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
        global shake
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
            #add a shake for dash
            if jumping:
                if dash == 1: 
                    shake = 1
                    x = x - 80
                    dash = 0
                #make more balanced also cooldown, but overall dash is a good idea
            else:
                dash = 1
        #jumping loop
        if key[pygame.K_SPACE]:
            if jumping == 0:
                y = y - dist
                gravset = 0
                gravity2 = 3
                jumping = 1
                
#collide checkr
        collide1 = pygame.Rect.colliderect(self.rect, platform.rect)
        collide2 = pygame.Rect.colliderect(self.rect, platform1.rect)
        collide3 = pygame.Rect.colliderect(self.rect, platform2.rect)
        collide4 = pygame.Rect.colliderect(self.rect, platform3.rect)
        collide5 = pygame.Rect.colliderect(self.rect, platform4.rect)
        collide6 = pygame.Rect.colliderect(self.rect, platform5.rect)
        #if any of them are 1 then that means I collided with a platform
        collide = 0 + collide1 + collide2 + collide3 + collide4 + collide5 + collide6
        #GRAVITY LOOP
        if gravset == 1:
            #implies to python that collide = 1, so if you're touching any platform it will return a one if none are being touched it gives a 0
            if collide:
                #if we touch then execute:
                jumping = 0
                dash = 1
            else:
                #if we aren't currently touching execute:
                if jumping == 1:
                    gravity2 = gravity2 - 0.112402
                    y = y - gravity2
                    return
                else:
                    #execute if currently jumping
                    gravity2 = gravity2 - 0.1
                    #slowly build up gravity, then add the added gravity to the player's movement
                    y = y - gravity2
#respawn loop, if you exit the bottom of the screen, then you are automatically put back to the first avail platform.
        global platformx
        if y > 500:
#            x = platformx + 7

            jumping = 0
            y = 0
            pygame.display.update()
            gravity2 = 0
#            object_.rect.x = x
            object_.rect.y = y
        object_.rect.y = y
            
#            self.kill()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
#add font and size, None is the base system font, therefore it is compatable !!CHANGE FONT LATER, MAKE SURE IS PACKED WITH GAME OR INSTALLER!!
basefont = pygame.font.Font(None, 32)
infofont = pygame.font.Font(None, 15)
try:
    #DEFINE SPRITE LOCATIONS
    #streamline to a more general path
    spriteimage = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "playernew.png" )).convert_alpha()
    platformimg = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "woodplat.png" )).convert_alpha()
    #startpng = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "start.png" )).convert_alpha()
    startpng1 = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "startbtn2.png" )).convert_alpha()
    startpng = pygame.transform.scale(startpng1, (80, 40))
    options1 = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "controlsbtn.png" )).convert_alpha()
    options = pygame.transform.scale(options1, (80, 40))
    background1 = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "backgroundnew.png" )).convert_alpha()
    background = pygame.transform.scale(background1, (WIDTH, HEIGHT))
    options.set_alpha(100) 
    pygamelogo = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "pygamelogo.png" )).convert_alpha()
    volumeon = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "volon.png" )).convert_alpha()
    volumeoff = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "voloff.png" )).convert_alpha()
    volume = volumeon
    coinimg = pygame.image.load(os.path.join('c:/', 'Users', "{0}".format(os.getlogin()), "Python_files", "Masterworks", "Assets", "coin.png" )).convert_alpha()
except:
    print("PANIC --- ERROR::SPRITES NOT FOUND // a sprite was not found")
pygame.display.set_caption("Splat")
all_sprites_list = pygame.sprite.Group() 
#define sprites
def defsprites():
    global started
    global object_
    global platform
    global platform1
    global platform2
    global platformx
    global platform1x
    global platform2x 
    global all_sprites_list
    global platform3x
    global platform3
    global platform4
    global platform5
    global platform4x
    global platform5x

    object_ = Sprite(RED, 20, 25, 1, spriteimage)
    all_sprites_list.add(object_)

    platform = Sprite(GREEN, 20, 25, 1, platformimg)
    platformx = 0
    platform.rect.x = platformx
    platform.rect.y = 100
    all_sprites_list.add(platform)

    platform1 = Sprite(GREEN, 10, 25, 1, platformimg)
    platform1x = randint(40, 70)
    platform1.rect.x = platform1x
    platform1.rect.y = randint(20, 70)
    all_sprites_list.add(platform1)

    platform2 = Sprite(GREEN, 10, 25, 1, platformimg)
    platform2x = platform1x + randint(40, 70)
    platform2.rect.x = platform2x
    platform2.rect.y = randint(20, 70)
    all_sprites_list.add(platform2)

    platform3 = Sprite(GREEN, 10, 25, 1, platformimg)
    platform3x = platform2x + randint(40, 70)
    platform3.rect.x = platform3x
    platform3.rect.y = randint(20, 70)
    all_sprites_list.add(platform3)

    platform4 = Sprite(GREEN, 10, 25, 1, platformimg)
    platform4x = platform3x + randint(40, 70)
    platform4.rect.x = platform4x
    platform4.rect.y = randint(20, 70)
    all_sprites_list.add(platform4)

    platform5 = Sprite(GREEN, 10, 25, 1, platformimg)
    platform5x = platform4x + randint(40, 70)
    platform5.rect.x = platform5x
    platform5.rect.y = randint(20, 70)
    all_sprites_list.add(platform5)

#    coin = Sprite(RED, 10, 25, 1, coinimg)

#    all_sprites_list.add(coin)

    

    started = started + 1
#start screen sprites
startbtn = Sprite(RED, 80, 40, 1, startpng)
all_sprites_list.add(startbtn)
volumebtn = Sprite(RED, 25, 25, 1, volume)
volstat = 0
all_sprites_list.add(volumebtn)
optionsbtn = Sprite(RED, 15, 30, 1, options)
all_sprites_list.add(optionsbtn)
optionsbtn.rect.x, optionsbtn.rect.y = 420, 460 
pglogo = Sprite(GREEN, 80, 40, 1, pygamelogo)
pglogo.rect.x, pglogo.rect.y = 0, 475 
all_sprites_list.add(pglogo)
#

y = int(0)
x = int(0)
gravity2 = 0


gravity2 = 0
exit = True
clock = pygame.time.Clock()
gravset = 1
def volumecheckr(volume):
    global musicstat
    moux, mouy = pygame.mouse.get_pos()
    mou = (pygame.Rect(moux, mouy, 1, 1))
    mouleft, moumiddle, mouright = pygame.mouse.get_pressed()
    if pygame.Rect.colliderect(volumebtn.rect, mou) and mouleft == True:
            print(volume) 
            if volume == volumeoff:
                musicstat = 0
                print(volumeoff)
                return volumeoff
            else:
                musicstat = 1
                return volumeon
        
def music(path):
    #this should ALWAYS run in threadded mode!
    print("attempting music playback via pygame.mixer.music.load, expect error if program failed.")
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        if musicstat == 1:
            pygame.mixer.music.pause()
        if musicstat == 0:
            pygame.mixer.music.unpause()
        return
    except:
        raise ConnectionRefusedError
def chshake():
    if shake == 1:
        if randint(1, 2) == 1:
            randomshakex = randint(-5, 5)
            pr = platform.rect.x
            pr1 = platform1.rect.x
            pr2 = platform2.rect.x
            pr3 = object_.rect.x
            platform.rect.x = platform.rect.x
            platform1.rect.x = platform1.rect.x
            platform2.rect.x = platform2.rect.x
            object_.rect.x = object_.rect.x
        else:
            randomshakey = randint(-5, 5)
            pr = platform.rect.y
            pr1 = platform1.rect.y
            pr2 = platform2.rect.y
            pr3 = object_.rect.y

        
def varrun():
    object_.keyboard()
    #1 is for 1st platform 2 for second ect ect
    #we still move x so i need to constantly calculate edge of screen.
    #moving WAY to fast
    platform.outsidecam(var=1)
    platform1.outsidecam(var=2)
    platform2.outsidecam(var=3)
    platform3.outsidecam(var=4)
    platform4.outsidecam(var=5)
    platform5.outsidecam(var=6)
    platform.ad(prex=platformx)
    platform1.ad(prex=platform1x)
    platform2.ad(prex=platform2x)
    platform3.ad(prex=platform3x)
    platform4.ad(prex=platform4x)
    platform5.ad(prex=platform5x)
def regetxval():
    global platformx
    global platform1x
    platformx = platform.rect.x
    platform1x = platform1.rect.x
started = 0
music("C:\\Users\\levic\\Python_files\\Masterworks\\Assets\\intro (1).mp3")
playmusic = threading.Thread(target=music("C:\\Users\\levic\\Python_files\\Masterworks\\Assets\\intro (1).mp3"))
playmusic.start()
playmusic.join()
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

    #SCREEN.fill clears the screen
    volume = volumecheckr(volume=volume)
    if started >= 1:
        if started == 1:
            try:
                pygame.music.mixer.stop()
            except:
                pass
            optionsbtn.kill()
            pglogo.kill()
            defsprites()  
        varrun()
#        screen.fill(SURFACE_COLOR)
        screen.blit(background, (0, 0))
        object_.rect.y = y
        txt = str(score)
        scoretxt = basefont.render(txt, True, (0,0,0))
        infotxt1 = infofont.render("Welcome to splat! use A and D to move and space to jump, and x to dash.", True, (0,0,0))
        screen.blit(scoretxt, (object_.rect.x + 440, 2))
        screen.blit(infotxt1, (5, 250))

    else:
        #startscreen
#        playmusic = threading.Thread(target=music("C:\\Users\\levic\\Python_files\\Masterworks\\Assets\\intro (1).mp3"))
#        playmusic.start()
#        playmusic.join()

        w, h = pygame.display.get_surface().get_size()
        screen.fill((0, 0, 0))
        message = ("Splat")
        messageli = list(message)
        messagelic = len(messageli) - 1
        cacheli = []
        num1 = -1
        while messagelic > -1:
            if messagelic > -1:
                num1 = num1 + 1
                cacheli.append(messageli[num1])
                messagerec = ''.join([str(elem) for elem in cacheli])
                messagelic -= 1
                begtxt = basefont.render(messagerec, True, (255, 255, 255))
#                sleep(0.1)
            scoremsg = bytes(str(score), 'utf-8')
            highscore = basefont.render(scoremsg, True, (255, 255, 255))
            screen.blit(highscore, (0,0))
            startbtn.rect.x = 5
            screen.blit(begtxt, (w / 2.6 + 11, h / 2.8 - 60))
            startbtn.rect.x = w / 2.6
            startbtn.rect.y = h / 2.8
            #check if btn pressed
            moux, mouy = pygame.mouse.get_pos()
            mou = (pygame.Rect(moux, mouy, 1, 1))
            mouleft, moumiddle, mouright = pygame.mouse.get_pressed()
            if pygame.Rect.colliderect(startbtn.rect, mou):
                startpng.set_alpha(100) 
                if mouleft == True:
                    startbtn.kill()
                    started = 1
            else:
                startpng.set_alpha(255) 
            if pygame.Rect.colliderect(pglogo.rect, mou):
                pygamelogo.set_alpha(100) 
                if mouleft == True:
                    webbrowser.open("https://www.pygame.org/news")
                    started = 1
            else:
                pygamelogo.set_alpha(255) 

            
#        started = 1
    #RUN EVERY TIME
#    fps = clock.get_fps()
#    TEXTRENDERERFINAL.tick()
#    fps1 = clock.get_fps()
#    usertext = TEXTRENDERERFINAL.text(text="Hello!", fps=fps1)
#    if usertext:
#        TEXTRENDERERFINAL.tick()
#        textsurface = basefont.render(usertext, True, (255,255,255))
#        screen.blit(textsurface,(0,0))
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    #or use pygame.display.update()
    pygame.display.update()
    #tick(MAXFRAMESPERSEC)
    clock.tick(60)
  
pygame.quit()
#check if it breaks after 13050 so after a little while of jumping if the game just stops putting the platforms, in which case we can use the reset to reset the game cords but not the acutal data from the game besides x and y right because we just spawn it back the begining one before the error happens so it looks infinite but it isn't too much for the computer to handle.