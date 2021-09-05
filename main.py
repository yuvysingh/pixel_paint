import pygame
from grid_sys import Grid, Box
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Screen variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Pygame variable
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (251, 236, 93)
ORANGE = (255, 127, 80)
PURPLE = (128, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

colors = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, BLACK, WHITE]


color_boxs = []


x = 3
dif = x * 2
change = (SCREEN_WIDTH - dif) // len(colors)


# Each box has a different color
for color in colors:

    # Create box and add to list
    box = Box(x, 640, color)
    box.side = change
    box.rect = pygame.Rect((box.x, box.y), (box.side, box.side))
    color_boxs.append(box)

    # Change pos
    x += change


# Grid of pixels
grid = Grid()


# Draw the paintscreen
def draw_screen(screen, grid):

    screen.fill(WHITE)
    grid.draw(screen)

    mouse_pos = pygame.mouse.get_pos()

    return mouse_pos


def paint():

    player_color = WHITE

    # Variable to see if the game should close
    running = True
    while running:

        # Controls frame rate
        clock.tick(30)

        # looks at all game events
        for event in pygame.event.get():

            # checks for user input
            if event.type == KEYDOWN:

                # checks if it was the escape key
                if event.key == K_ESCAPE:

                    # stops the application
                    running = False

            # was the close button hit
            elif event.type == QUIT:

                # stops the application
                running = False

        mouse_pos = draw_screen(screen, grid)

        for box in color_boxs:

            pygame.draw.rect(screen, box.color, box.rect)
            box.draw_border(screen)

            if box.rect.collidepoint(mouse_pos):

                if pygame.mouse.get_pressed()[0] == 1:

                    player_color = box.color

        if mouse_pos[0] <= 600 and mouse_pos[1] <= 600:

            if pygame.mouse.get_pressed()[0] == 1:

                for box in grid.boxes:

                    if box.rect.collidepoint(mouse_pos):

                        box.color = player_color

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    paint()
