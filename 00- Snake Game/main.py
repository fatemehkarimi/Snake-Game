import pygame
from game_settings import GameSettings
from board import Board
from food import Food

def main():
    g_settings = GameSettings()
    screen = pygame.display.set_mode(g_settings.window_size)
    screen.fill(g_settings.background_color)
    pygame.display.set_caption('Snake Game')

    board = Board(g_settings)
    food = Food(g_settings)

    board.draw(screen)
    food.draw(screen, board)
    pygame.display.flip()

    running = True
    while running:
        pygame.time.wait(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()