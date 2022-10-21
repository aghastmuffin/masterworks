import pygame
#we can add a verify account with discord for highscore/better web functions
pygame.init()
class player(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        #self.image will eventually be an image, but for now its a surface for a square
        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)
  
        pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
    def kmove():
        x = 0
        y = 0
        dist = 5
        #dist is movement speed.
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            y = y - dist
        if key[pygame.K_a]:
            x = x - dist
        if key[pygame.K_s]:
            y = y + dist
        if key[pygame.K_d]:
            x = x + dist 
while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
  