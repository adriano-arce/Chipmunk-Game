from random import randint
from chipmunk import *
from acorn import Acorn
from nest import Nest


def main():
    """The main entry point."""
    pygame.init()

    # Icon should be loaded before mode is set.
    icon = pygame.image.load("images/fake-icon.png")
    icon.set_colorkey(CELL_COLOUR)
    pygame.display.set_icon(icon)
    screen_surf = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("Chipmunk Game")

    msg_font = pygame.font.SysFont("consolas", 28)
    fps_clock = pygame.time.Clock()

    chipmunks = pygame.sprite.RenderUpdates()
    acorns = pygame.sprite.RenderUpdates()
    nests = pygame.sprite.RenderUpdates()
    Chipmunk.groups = chipmunks
    Acorn.groups = acorns
    Nest.groups = nests

    total_acorns = ACORN_INIT
    acorn_timer = randint(MIN_ACORN_SPAWN * FPS, MAX_ACORN_SPAWN * FPS)
    player = Chipmunk(msg_font)
    for __ in range(ACORN_INIT):
        Acorn()

    # The main game loop.
    while True:
        # The event handling loop.
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                else:
                    for direction in ALL_DIRS:
                        if event.key in direction.keys:
                            # Enqueue the direction.
                            player.dir_queue.appendleft(direction)
            elif event.type == KEYUP:
                for direction in ALL_DIRS:
                    if event.key in direction.keys:
                        # Remove the direction. Not quite a dequeue.
                        player.dir_queue.remove(direction)

        # Update all the things.
        player.update()
        for __ in pygame.sprite.spritecollide(player, acorns, True):
            player.acorn_count += 1
            total_acorns -= 1
        if total_acorns < ACORN_LIMIT:
            if acorn_timer < 0:
                Acorn()
                total_acorns += 1
                acorn_timer = randint(MIN_ACORN_SPAWN * FPS,
                                      MAX_ACORN_SPAWN * FPS)
            else:
                acorn_timer -= 1
        for nest in pygame.sprite.spritecollide(player, nests, False):
            nest.acorn_count += player.acorn_count
            player.acorn_count = 0
            nest.update()
        message = "Collected Acorns: {0}".format(player.acorn_count)
        text_surf = msg_font.render(message, True, FONT_COLOUR)

        # Draw all the things.
        screen_surf.fill(BKGD_COLOUR)
        draw_grid(screen_surf)
        nests.draw(screen_surf)  # Draw this before the chipmunks.
        chipmunks.draw(screen_surf)
        acorns.draw(screen_surf)
        screen_surf.blit(text_surf, text_surf.get_rect())

        # Render the screen.
        pygame.display.update()
        fps_clock.tick(FPS)


if __name__ == "__main__":
    main()

    # Close the window on terminating the main game loop.
    pygame.quit()