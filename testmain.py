import random
import pygame as py
import math
FrameHeight = 600
FrameWidth = 1000
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
        
            

   # makes asteroids go boom
def hit():
   pass

def main():
    py.init() 
    clock = py.time.Clock() 
    lasers = []
    laserVelocity = 5
    
    
    scroll = 0

    py.display.set_caption("My Game") 
    screen = py.display.set_mode((FrameWidth, FrameHeight))  
    bg = py.image.load("./images/space-background.jpg").convert() 
    laserImage = py.image.load("./images/laser.jpg").convert()  
    asteroidImage = py.image.load("./images/medium rock.png").convert() 

    player = Player()
    asteroids =[]
    

    for _ in range(1):
        asteroid = py.Rect(random.randint(FrameWidth, FrameWidth + 100),
                       random.randint(0, FrameHeight - 20), 20, 20)
        asteroids.append(asteroid)

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
        
        for asteroid in asteroids:
            if player.rect.colliderect(asteroid):
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
            for asteroid in asteroids:
                screen.blit(asteroidImage, asteroid.topleft)
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