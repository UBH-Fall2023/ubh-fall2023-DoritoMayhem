import pygame

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

def main():
    running = True
    background = pygame.image.load("space-background.jpg").convert()

# Create Rect objects for the background and screen
    bg_rect = background.get_rect()
    screen_rect = window.get_rect()

# Set the initial position of the background image
    bg_rect.bottom = screen_rect.bottom

# Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Update the position of the background image
    bg_rect.bottom = screen_rect.bottom
    bg_rect.move_ip(0, 5)
    while running:
    # for loop through the event queue
        for event in pygame.event.get(): # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False
    # If the background image goes off the screen, reset its position to the top of the screen
        window.blit(background, bg_rect)
    # Update the position of the background image and reset image
        bg_rect.move_ip(0, 5)
        if bg_rect.top >= screen_rect.bottom:
            bg_rect.bottom = 0
        # Update the display
        pygame.display.update()
    # calls asteroid and laser functions
    asteroid()
    laser()

      # adds a clock and limits the frames per second
    clock = pygame.time.Clock()
    clock.tick(60)

    pygame.quit()  

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