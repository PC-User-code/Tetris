import pygame
import os
import sys


settings = [816, 816, 32, 60]           # width, height, size_title, fps

class Tetris:
    def __init__(self):
        figures = ["T", "L", "S", "Lr", "I"]    # возможные фигруы в тетрисе (игра создана изначально русским программистом на языке Pascal
                                                # ее название символично ведь каждая фигура состоит из 4 кваратов)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris")
    icon = pygame.image.load("data\icon.png")
    pygame.display.set_icon(icon)
    size = width, height = settings[0], settings[1]
    tile_size = settings[2]
    FPS = settings[3]
    ui_sprite = pygame.sprite.Group()
    #надо сделать спрайт, как на картинке в папке data dendy.gif
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.update(events)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


