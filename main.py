import pygame as py
import math
frameHeight = 800
frameWidth = 600
window = py.display.set_mode((frameHeight, frameWidth))
py.display.set_caption("My Game")

def main():
    py.init() 
  
    clock = py.time.Clock() 
    
    FrameHeight = 600
    FrameWidth = 1000
    
    # PYGAME FRAME WINDOW 
    py.display.set_caption("My Game") 
    screen = py.display.set_mode((FrameWidth, FrameHeight)) 
    
    # IMAGE 
    bg = py.image.load("./images/space-background.jpg").convert() 

    scroll = 0
    tiles = math.ceil(FrameWidth / bg.get_width()) + 1
    
    # MAIN LOOP 
    while True: 
        # clock for the speed of the scrolling
        clock.tick(60) 
        i = 0
        while(i < tiles): 
            screen.blit(bg, (bg.get_width()*i + scroll, 0)) 
            i += 1
        # FRAME FOR SCROLLING 
        scroll -= 3
    
        # RESET THE SCROLL FRAME 
        if abs(scroll) > bg.get_width(): 
            scroll = 0
        # CLOSINF THE FRAME OF SCROLLING 
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