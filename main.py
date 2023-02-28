import pygame
from os import path

WIDTH, HEIGHT = 500, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Skiing Simulator")

SKIER_WIDTH, SKIER_HEIGHT = 45, 65

# colors used
WHITE = (235, 255, 255)
GRAY = (223, 222, 227)

SKIER_IMAGE = pygame.image.load(path.join('assets', 'images', 'placeholder.jpg'))
SKIER = pygame.transform.scale(SKIER_IMAGE, (SKIER_WIDTH, SKIER_HEIGHT))

VERT_MIDDLE_TEST = pygame.Rect(WIDTH//2 - 1, 0, 2, HEIGHT)

def draw_mountain(skier):
     WIN.fill(WHITE) # white background

     pygame.draw.rect(WIN, GRAY, VERT_MIDDLE_TEST)

     pygame.draw.rect(WIN, GRAY, skier)

     WIN.blit(SKIER, (skier.x,skier.y))

     pygame.display.update()

def main():
    skier = pygame.Rect(WIDTH//2 - SKIER_WIDTH//2, 200, SKIER_WIDTH, SKIER_HEIGHT)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()


        draw_mountain(skier)

    main()

if __name__ == "__main__":
     main()
