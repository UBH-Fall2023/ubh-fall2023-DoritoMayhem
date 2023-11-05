import random
import pygame as py
import math

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("images/spaceship.png").convert()
        self.rect = self.image.get_rect()
        
        self.laserList = []
        self.maxlasers = 100
    def update(self, keys):
        if keys[py.K_UP]:
            self.rect.y -= 5
        if keys[py.K_DOWN]:
            self.rect.y += 5
        if keys[py.K_LEFT]:
            self.rect.x -= 5
        if keys[py.K_RIGHT]:
            self.rect.x += 5
        
            
            
class Asteroid(py.sprite.Sprite):
    def init(self,FrameWidth, FrameHeight):
        super().init()
        self.image = py.image.load("images/medium rock.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800)
        self.rect.y = random.randint(0, 600)
        self.speed = random.uniform(1.0, 3.0)
        self.FrameWidth = FrameWidth
        self.FrameHeight = FrameHeight

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.rect.x = self.FrameWidth
            self.rect.y = random.randint(0, self.FrameHeight - self.rect.height)
   # makes asteroids go boom
def hit():
   pass

def main():
    py.init() 
    clock = py.time.Clock() 
    lasers = []
    laserVelocity = 5
    
    FrameHeight = 600
    FrameWidth = 1000
    scroll = 0

    py.display.set_caption("My Game") 
    screen = py.display.set_mode((FrameWidth, FrameHeight))  
    bg = py.image.load("./images/space-background.jpg").convert() 
    laserImage = py.image.load("./images/laser.jpg").convert()  

    player = Player()
    asteroids = py.sprite.Group()
    

    for _ in range(5): # Add 5 asteroids to the group
        asteroid = Asteroid(FrameWidth=FrameWidth, FrameHeight = FrameHeight)
        asteroid.rect.x = random.randint(0, FrameWidth)
        asteroid.rect.y = random.randint(0, FrameHeight)
        asteroids.add(asteroid)

    tiles = math.ceil(FrameWidth / bg.get_width()) + 1
    
    # MAIN LOOP 
    while True: 
        # frames per second
        clock.tick(60) 

        # background stuff
        i = 0
        while(i < tiles): 
            screen.blit(bg, (bg.get_width()*i + scroll, 0)) 
            i += 1
        # This also affects the speed of the scrolling
        scroll -= 3
        if abs(scroll) > bg.get_width(): 
            scroll = 0
        
        # player handling
        keys = py.key.get_pressed()
        player.update(keys)
        screen.blit(player.image, player.rect)

        # Update asteroids and check for collisions
        asteroids.update()
        for asteroid in asteroids:
            if py.sprite.collide_rect(player, asteroid):
                hit() # asteroid hits the player

        # Close the game
            for event in py.event.get(): 
                if event.type == py.QUIT: 
                    py.quit() 
                if event.type == py.KEYDOWN and event.key == py.K_SPACE:
                # Create a new bullet at the player's position
                    laser = py.Rect(int(player.rect.x) + 100, int(player.rect.y) + 50,10,5)
                    lasers.append(laser)
            
            for laser in lasers:
                laser.x += laserVelocity
            for laser in lasers:
                screen.blit(laserImage, laser.topleft)
        py.display.update() 
    


   # makes asteroids go boom
def hit():
   pass


  # how the asteroid acts
def asteroid():
   pass


  # laser from spaceship and how it acts (travel route)



if __name__ == "__main__":
    main()