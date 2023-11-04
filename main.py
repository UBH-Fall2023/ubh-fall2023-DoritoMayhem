import random
import pygame as py
import math

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("images/spaceship.png").convert()
        self.rect = self.image.get_rect()

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
    def __init__(self):
        super().__init__()
        self.image = py.image.load("images/medium rock.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        pass # Move the asteroid towards the player

def background(bg_rect, screen_rect):
    ...
   # makes asteroids go boom
def hit():
   pass

def main():
    py.init() 
    clock = py.time.Clock() 
    
    FrameHeight = 600
    FrameWidth = 1000
    scroll = 0

    py.display.set_caption("My Game") 
    screen = py.display.set_mode((FrameWidth, FrameHeight))  
    bg = py.image.load("./images/space-background.jpg").convert() 

    player = Player()
    asteroids = py.sprite.Group()

    for _ in range(5): # Add 5 asteroids to the group
        asteroid = Asteroid()
        asteroid.rect.x = random.randint(0, FrameWidth)
        asteroid.rect.y = random.randint(0, FrameHeight)
        asteroids.add(asteroid)

    tiles = math.ceil(FrameWidth / bg.get_width()) + 1
    
    # MAIN LOOP 
    while True: 
        # clock for the speed of the scrolling
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
                quit() 
    
        py.display.update() 
    py.quit() 

def background(bg_rect, screen_rect):
    ...
   # makes asteroids go boom
def hit():
   pass


  # how the asteroid acts
def asteroid():
   pass


  # laser from spaceship and how it acts (travel route)
def laser():
   pass


if __name__ == "__main__":
    main()