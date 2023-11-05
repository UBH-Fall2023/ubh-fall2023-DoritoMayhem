import random
import pygame as py
import math
FrameHeight = 600
FrameWidth = 1000
high = [0]

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("images/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.lives = 3

    def update(self, keys):
        if keys[py.K_UP] and self.rect.y >0:
            self.rect.y -= 5
        if keys[py.K_DOWN] and self.rect.y <500:
            self.rect.y += 5
        if keys[py.K_LEFT] and self.rect.x >0:
            self.rect.x -= 5
        if keys[py.K_RIGHT] and self.rect.x < 900:
            self.rect.x += 5
        
class Score(object):
    def __init__(self):
        self.white = 255,255,255
        self.count = 0
        self.high = high[0]
        self.lifecount = 3
        self.font = py.font.SysFont("comicsans",20, True , True)
        self.text = self.font.render("Score : "+str(self.count),1,self.white)
        self.live = self.font.render("Lives:"+str(self.lifecount),1,self.white)
        self.highscore = self.font.render("High Score:"+str(self.high),1,self.white)

    def show_score(self, screen):
        screen.blit(self.text, (0 ,0))
        screen.blit(self.live, (0,100))
        screen.blit(self.highscore, (0,50))
    def score_up(self):
        self.count += 1
        self.text = self.font.render("Score : "+str(self.count),1,self.white)
    def life_down(self):
        self.lifecount -= .5
        self.live = self.font.render("Lives:"+str(int(self.lifecount)),1,self.white )


def main():
    py.init()
    clock = py.time.Clock()
    lasers = []
    asteroids = []
    laserVelocity = 5
    asteroidVelocity = 4
    asteroid_add_timer = 0
    asteroid_add_interval = 1000
    scroll = 0
    score = Score()
    maxlasers =6
    font = py.font.SysFont("comicsans",20, True , True)
    txt = font.render("Game Over\nPress r to restart",1,(255,255,255))
    py.display.set_caption("My Game")
    screen = py.display.set_mode((FrameWidth, FrameHeight))
    bg = py.image.load("./images/space-background.jpg").convert()
    laserImage = py.image.load("./images/laser.jpg").convert_alpha()
    laserMask = py.mask.from_surface(py.image.load("./images/laser.jpg").convert_alpha())
    asteroidImages = [py.image.load("./images/small rock.png").convert_alpha(),
                                                                    py.image.load("./images/medium rock.png").convert_alpha(),
                                                                    py.image.load("./images/large rock.png").convert_alpha()]
    asteroid_masks = [py.mask.from_surface(image) for image in asteroidImages]
    player = Player()
    player_mask = py.mask.from_surface(player.image)
    tiles = math.ceil(FrameWidth / bg.get_width()) + 1
    asteroid_add_timer = py.time.get_ticks()
    game_over = False
    asteroids_to_remove = []
    # MAIN LOOP
    while not game_over:
        # frames per second
        clock.tick(60)
        currentTime = py.time.get_ticks()
        time_elapsed = currentTime - asteroid_add_timer
        if player.lives == 0:
            if score.count > score.high:
                high[0] = score.count
            game_over = True
        # background stuff
        i = 0
        while i < tiles:
            screen.blit(bg, (bg.get_width() * i + scroll, 0))
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
        if time_elapsed >= asteroid_add_interval:
            for _ in range(2):
                integer = random.randint(0, 2)
                image = asteroidImages[integer]
                mask = asteroid_masks[integer]
                asteroid = image.get_rect()
                asteroid.x = random.randint(FrameWidth, FrameWidth + 100)
                asteroid.y = random.randint(0, FrameHeight - 20)
                asteroids.append((asteroid, image, mask))
                """asteroid = py.Rect(random.randint(FrameWidth, FrameWidth + 100),
                                   random.randint(0, FrameHeight - 20), width, height )"""
                asteroids.append((asteroid,image,mask))

            # Update the asteroid_add_timer
            asteroid_add_timer = currentTime
        # Looks for the events that are happening
        for event in py.event.get():
            # Closes the program when exited
            if event.type == py.QUIT:
                py.quit()
            # Create a new bullet at the player's position with a maximum of whatever is maxlasers
            if event.type == py.KEYDOWN and event.key == py.K_SPACE and len(lasers) <maxlasers:
                laser = py.Rect(int(player.rect.x) + 100, int(player.rect.y) + 50, 10, 5)
                lasers.append(laser)
        
    
       # Detects for collisions and causes its affects
        for laser in lasers:
            laser.x += laserVelocity
            screen.blit(laserImage, laser.topleft)
            if laser.left > 950:
                lasers.remove(laser)
        for asteroid,image,mask in asteroids:
            asteroid.x -= asteroidVelocity
            screen.blit(image, asteroid.topleft)
            if asteroid.right < 0:
                asteroids.remove((asteroid,image,mask))
            if mask.overlap_area(player_mask, (player.rect.x - asteroid.x, player.rect.y - asteroid.y)) > 0:
                asteroids.remove((asteroid,image,mask))
                player.lives -=.5
                score.life_down()
                
            for laser in lasers:
                if mask.overlap_area(laserMask, (laser.x - asteroid.x, laser.y - asteroid.y)) > 0:
                    asteroids_to_remove.append((asteroid, image, mask))
                    lasers.remove(laser)
                    score.score_up()
        for asteroid_data in asteroids_to_remove:
            if asteroid_data in asteroids:
                asteroids.remove(asteroid_data)
        score.show_score(screen)
        py.display.update()
    while game_over:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN and event.key == py.K_r:
                main()  # Restart the game
        screen.blit(txt, (350, 250))
        py.display.update()
   



if __name__ == "__main__":
    main()