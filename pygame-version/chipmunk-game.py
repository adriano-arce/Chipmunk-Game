import pygame, sys
from pygame.locals import *
from chipmunk import Chipmunk

# Set up the frame rate.
FPS = 30

# Each cell in the grid is a square with side length CELL_SIDE pixels.
# GRID_SIZE measures the dimensions of the grid in terms of cells.
# SCREEN_SIZE scales GRID_SIZE by the CELL_SIDE.
CELL_SIDE = 30
GRID_SIZE = (GRID_WIDTH, GRID_HEIGHT) = (32, 20)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = tuple(CELL_SIDE*dim for dim in GRID_SIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
DARK_GRAY = ( 40,  40,  40)
BG_COLOUR   = BLACK
LINE_COLOUR = DARK_GRAY


def terminate():
    """
    Terminates the program.
    """
    pygame.quit()
    sys.exit()


def draw_grid(screen):
    """
    Draws a grid to the screen.
    """
    # Draw the vertical lines.
    for x in range(0, SCREEN_WIDTH, CELL_SIDE):
        pygame.draw.line(screen, LINE_COLOUR, (x, 0), (x, SCREEN_HEIGHT))
    # Draw the horizontal lines.
    for y in range(0, SCREEN_HEIGHT, CELL_SIDE):
        pygame.draw.line(screen, LINE_COLOUR, (0, y), (SCREEN_WIDTH, y))



def main():
    """
    The main game loop.
    """
    pygame.init()

    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Chipmunk Game")
    player = Chipmunk()

    while True:
        screen.fill(BG_COLOUR)
        draw_grid(screen)

        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)

if __name__ == "__main__":
    main()