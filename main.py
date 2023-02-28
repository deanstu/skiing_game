import pygame
from os import path
import game_constants as c
from skier import Skier

WIN = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("Skiing Simulator")


SKIER_IMAGE = pygame.image.load(path.join('assets', 'images', 'placeholder.jpg'))
SKIER = pygame.transform.scale(SKIER_IMAGE, (c.SKIER_WIDTH, c.SKIER_HEIGHT))

VERT_MIDDLE_TEST = pygame.Rect(c.WIDTH//2 - 1, 0, 2, c.HEIGHT)


def movement(keys, skier):
    if keys[pygame.K_a] and skier.x - c.SKIER_VEL > 0:  # LEFT
        skier.x -= c.SKIER_VEL
    if keys[pygame.K_d] and skier.x + c.SKIER_VEL + skier.width < c.WIDTH:  # RIGHT
        skier.x += c.SKIER_VEL


def draw_mountain(player):
     WIN.fill(c.WHITE) # white background

     pygame.draw.rect(WIN, c.GRAY, VERT_MIDDLE_TEST)

     skier = pygame.Rect(round(player.x),round(player.y), c.SKIER_WIDTH, c.SKIER_HEIGHT)

     WIN.blit(SKIER, (skier.x,skier.y))

     pygame.display.update()

def main():
    player = Skier(c.SKIER_INIT_X, c.SKIER_INIT_Y)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()


        
        keys_pressed = pygame.key.get_pressed()
        movement(keys_pressed, player)            
                    
        draw_mountain(player)

    main()

if __name__ == "__main__":
     main()
