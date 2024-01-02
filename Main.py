import pygame
import os
import sys

settings = [816, 816, 32]               # width, height, size_title
FPS = 60

class Tetris:
    def __init__(self):
        figures = ["O", "T", "L", "S", "J", "I", "Z"]    # возможные фигруы в тетрисе (игра создана изначально русским программистом на языке Pascal
                                                # ее название символично ведь каждая фигура состоит из 4 кваратов\

class Interface(pygame.sprite.Sprite):
    def __init__(self):             #отрисовка интерфейса при игре
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(pygame.Color("#38B2CE"))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = 1, 1
            pygame.draw.line(self.image, pygame.Color("white"), (0, 0), (50, 50))


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Tetris")
    icon = pygame.image.load("data\icon.png")
    pygame.display.set_icon(icon)
    size = width, height = settings[0], settings[1]
    tile_size = settings[2]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    gi = Interface()
    all_sprites.add(gi)
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


